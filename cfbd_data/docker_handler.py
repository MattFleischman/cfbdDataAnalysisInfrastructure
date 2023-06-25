import json
import boto3
import os
import datetime
import logging
import cfbd_data.utilities.utility_functions as utilities
from cfbd_data.utilities.constants import *
import cfbd_data.forecasting.linear_regression_forecasting as lin_reg_forecast


logger = logging.getLogger()
logger.setLevel(logging.INFO)
lambda_client = boto3.client('lambda')
s3_client = boto3.client('s3')


def apply_ppa_attribution(event, context):
    s3_bucket = os.environ['s3_source_bucket']
    output_file = event.get('output_prefix', adjusted_ppa_path)
    year_input = event.get('year', None)
    year = year_input if year_input else datetime.datetime.now().strftime('%Y')
    season_type = event.get('season_type', None)
    week = event.get('week', None)

    # pull source data
    ingest_file_prefix = utilities.ingest_file_prefix_string(year, season_type, week)

    df_team = utilities.dataframe_from_s3(
        f"{cfbd_prefix}TeamsApi_get_fbs_teams/year_{year}/", s3_bucket)
    df_game = utilities.dataframe_from_s3(
        f"{cfbd_prefix}GamesApi_get_games/{ingest_file_prefix}", s3_bucket)
    df_pbp = utilities.dataframe_from_s3(
        f"{cfbd_prefix}PlaysApi_get_plays/{ingest_file_prefix}", s3_bucket, columns=get_plays_columns)

    #apply regression
    ppa_regression = lin_reg_forecast.opponent_adjustment_regression_wrapper(df_team, df_game, df_pbp, year)
    print(f"ppa_regression: {ppa_regression}")

    #output regression df
    utilities.output_df_by_index(ppa_regression, s3_bucket, output_file, year, week, season_type)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Request completed successfully",
            }
        ),
    }

def apply_prediction(event, context):
    s3_bucket = os.environ['s3_source_bucket']
    output_prefix = event.get('output_file', forecast_output_path)
    year_input = event.get('year', None)
    year = year_input if year_input else datetime.datetime.now().strftime('%Y')
    season_type = event.get('season_type', None)
    week = event.get('week', None)

    #pull forecast dependencies - need to pull full year
    enriched_games_filtered_df = utilities.dataframe_from_s3(
        f"{cfbd_prefix}{default_forecasting_path}year_{year}/", s3_bucket).reset_index()

    #run linear regression for points prediction
    raw_prediction_df = lin_reg_forecast.apply_multiple_linear_regression(enriched_games_filtered_df, week, season_type)

    # output to s3
    utilities.output_df_by_index(raw_prediction_df, s3_bucket, output_prefix,
                                 year, week, season_type)

    print("test completed") #TODO: delete line

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Request completed successfully",
            }
        ),
    }