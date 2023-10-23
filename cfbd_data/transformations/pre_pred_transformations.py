import pandas as pd
import cfbd_data.utilities.utility_functions as utilities
from cfbd_data.utilities.constants import *


def transform_game_details(input_df):

        df_get_games_trimmed = input_df[df_get_games_trimmed_columns]

        df_get_games_away = df_get_games_trimmed[df_get_games_away_columns]\
                                .rename( columns=df_get_games_away_rename_dict)\
                                .assign(home_away='away')
        df_get_games_home = df_get_games_trimmed[df_get_games_home_columns]\
                                .rename(columns=df_get_games_home_rename_dict)\
                                .assign(home_away='home')

        df_get_games_all = pd.concat([df_get_games_home, df_get_games_away], axis=0).reset_index()
        return df_get_games_all

def recruiting_transformation(df_player_stats, df_roster,
                              df_recruits, df_transfer_portal,
                              df_get_recruiting_groups, year):

    team_recruiting_avgs = df_get_recruiting_groups.loc[
        df_get_recruiting_groups['position_group'] == 'All Positions', ['team',
                                                                        'average_rating', 'commits',
                                                                        'average_stars']]
    team_recruiting_avgs = team_recruiting_avgs.groupby(['team']).mean().reset_index()

    team_recruiting_avgs.rename(columns={'average_rating': 'group_average_rating',
                                         'commits': 'group_avg_annual_commits',
                                         'average_stars': 'group_average_stars'}, inplace=True)

    df_roster['first_recruit_id'] = df_roster['recruit_ids'].apply(
        lambda x: x[1:-1].split(',')[0] if (len(x[1:-1].split(',')) > 1) else x[1:-1])

    df_recruits['first_name'] = df_recruits['name'].str.split(' ', expand=True)[0]
    df_recruits['last_name'] = df_recruits['name'].str.split(' ', expand=True)[1]
    df_recruits['id'] = df_recruits['id'].apply(str)

    df_recruits = df_recruits[
        ['name', 'first_name', 'last_name', 'id', 'athlete_id', 'recruit_type', 'year', 'ranking', 'stars', 'rating', 'committed_to',
         'state_province']]

    df_transfer_portal['id'] = None
    df_transfer_portal['athlete_id'] = None
    df_transfer_portal['recruit_type'] = None
    df_transfer_portal['ranking'] = None
    df_transfer_portal['state_province'] = None

    df_transfer_portal['name'] = df_transfer_portal['first_name'] + " " + df_transfer_portal['last_name']
    df_transfer_portal = df_transfer_portal[
        ['name', 'first_name', 'last_name', 'id', 'athlete_id', 'recruit_type', 'season', 'ranking', 'stars', 'rating', 'destination',
         'state_province']]
    df_transfer_portal.rename({'season': 'year', 'destination': 'committed_to'}, inplace=True)

    df_recruits_expanded = pd.concat([df_recruits, df_transfer_portal], ignore_index=True)

    roster_missing_id = df_roster.loc[df_roster['first_recruit_id'] == '']
    roster_including_id = df_roster.loc[df_roster['first_recruit_id'] != '']

    main_recruiting_rosters_df = roster_including_id.merge(df_recruits_expanded, 'inner',
                                                           left_on=['team', 'first_recruit_id'],
                                                           right_on=['committed_to', 'id'])

    secondary_recruiting_rosters_df = roster_missing_id.merge(df_recruits_expanded, 'inner',
                                                              left_on=['team', 'last_name', 'first_name'],
                                                              right_on=['committed_to', 'last_name', 'first_name'])

    combined_recruiting_rosters_df_new = pd.concat([main_recruiting_rosters_df, secondary_recruiting_rosters_df],
                                                   ignore_index=True)

    print(df_player_stats.columns)
    recruited_players_w_stats = combined_recruiting_rosters_df_new.loc[
        combined_recruiting_rosters_df_new.id_x.isin(df_player_stats.player_id.values.tolist())]

    recruited_players_w_stats_sum = recruited_players_w_stats[
        ['team', 'position', 'stars', 'rating', 'ranking']].groupby(['team']).mean()

    total_recruiting_stats = recruited_players_w_stats_sum.merge(team_recruiting_avgs, on=['team'])
    total_recruiting_stats['year'] = year

    return total_recruiting_stats

def apply_rolling_lookback(input_df, group_by_col, return_cols,
                           sort_col=None, rename_dict=None, lookback_periods=3):
    input_df_lookback = input_df[
        advanced_team_enriched_games_data_lookback_columns].sort_values(
        by=sort_col).groupby([group_by_col]).transform(lambda x: x.rolling(3, 1, closed='left').mean()) \
        .rename(columns=rename_dict)
    # TODO need to test that the above lookback works as expected
    return input_df_lookback[return_cols]

def prep_default_forecasting_dataset(pivoted_games_data, total_recruiting_stats,
                                     df_advanced_game_team_stats, df_get_games_all,
                                     weekly_adjusted_ppa_df, df_team):
    #TODO enable lookback to work effectively

    # merge game details, team game stats, and recruiting team data
    print(f"df_get_games_all: {df_get_games_all.loc[df_get_games_all.team == 'Washington']}")
    print(f"pivoted_games_data: {pivoted_games_data.loc[pivoted_games_data.school == 'Washington']}")
    basic_enriched_games_data = df_get_games_all.merge(pivoted_games_data, how='left', left_on=['id', 'team'],
                                                       right_on=['game_id', 'school'])

    print(f"basic_enriched_games_data: {basic_enriched_games_data.loc[basic_enriched_games_data.team == 'Washington']}")
    print(
        f"df_advanced_game_team_stats: {df_advanced_game_team_stats.loc[df_advanced_game_team_stats.team == 'Washington']}")
    advanced_enriched_games_data = basic_enriched_games_data.merge(df_advanced_game_team_stats, how='left',
                                                                   left_on=['id', 'team'], right_on=['game_id', 'team'])
    print(
        f"advanced_enriched_games_data: {advanced_enriched_games_data.loc[advanced_enriched_games_data.team == 'Washington']}")

    recruiting_enriched_team_attributes = df_team.merge(total_recruiting_stats, how='left',
                                                                              left_on=['school'], right_on=['team']).rename(columns=
        {'conference_x': 'conference'})

    print(
        f"advanced_enriched_games_data: {advanced_enriched_games_data.loc[advanced_enriched_games_data.team == 'Washington']}")
    print(
        f"recruiting_enriched_team_attributes: {recruiting_enriched_team_attributes.loc[recruiting_enriched_team_attributes.team == 'Washington']}")

    advanced_team_enriched_games_data = advanced_enriched_games_data.merge(recruiting_enriched_team_attributes,
                                                                           how='left', left_on=['team'],
                                                                           right_on=['school']) \
        .merge(
        recruiting_enriched_team_attributes[
            ['school', 'abbreviation', 'conference', 'group_average_rating', 'group_average_stars', 'stars', 'rating']],
        how='left', left_on=['opponent_x'], right_on=['school'], suffixes=['_team', '_opponent'])

    advanced_team_enriched_games_data = advanced_team_enriched_games_data[advanced_team_enriched_games_data_columns]\
                                        .rename(columns=advanced_team_enriched_games_data_rename_dict)

    print(f"advanced_team_enriched_games_data.loc[advanced_team_enriched_games_data.team == 'Washington']: {advanced_team_enriched_games_data.loc[advanced_team_enriched_games_data.team == 'Washington']}")
    advanced_team_enriched_games_data = advanced_team_enriched_games_data.assign(
        total_offense_yards=lambda x: x.stat_netPassingYards + x.stat_rushingYards)

    advanced_team_enriched_games_data['third_down_pct'] = None

    advanced_team_enriched_games_data.loc[(advanced_team_enriched_games_data.completed == True) & (
        ~advanced_team_enriched_games_data.stat_thirdDownEff.isnull()), 'third_down_pct'] \
        = advanced_team_enriched_games_data.loc[(advanced_team_enriched_games_data.completed == True) & (
        ~advanced_team_enriched_games_data.stat_thirdDownEff.isnull()), 'stat_thirdDownEff'] \
        .apply(lambda x: utilities.divide_string(x))


    #Adjusted week comments
    max_week = int(max(advanced_team_enriched_games_data['week']))
    advanced_team_enriched_games_data['adjusted_week'] = advanced_team_enriched_games_data['week']

    advanced_team_enriched_games_data.loc[
        advanced_team_enriched_games_data.season_type == 'postseason', ['adjusted_week']] += max_week

    #Filter out non-FBS schools
    advanced_team_enriched_games_data = advanced_team_enriched_games_data.loc[
        (advanced_team_enriched_games_data.team.isin(df_team.school.to_list())) & (
            advanced_team_enriched_games_data.opponent.isin(df_team.school.to_list()))]

    #Trim dataset and reset index, sorting in preparation for lookback calcs
    advanced_team_enriched_games_data = advanced_team_enriched_games_data[
        ['game_id', 'completed', 'team', 'conference', 'abbreviation_team', 'week', 'adjusted_week', 'season_type', 'home_away', 'logo_primary', 'logo_alt', 'opponent',
         'conference_opponent', 'abbreviation_opponent', 'team_stat_earning_ply_rating', 'stat_firstDowns', 'rating_opponent', 'pregame_elo', 'opponent_pregame_elo',
         'total_offense_yards', 'third_down_pct', 'points']]\
        .sort_values(by=['adjusted_week', 'team'])\
        .reset_index(drop=True)

    #apply lookback calcs
    advanced_team_enriched_games_data[lookback_enrichment_columns] = apply_rolling_lookback(advanced_team_enriched_games_data,
                                                                                            'team',
                                                                                            lookback_enrichment_columns,
                                                                                            'adjusted_week',
                                                                                            advanced_team_enriched_games_data_lookback_rename_dict)

    #Filter out first three weeks of data
    enriched_games_filtered = advanced_team_enriched_games_data.loc[advanced_team_enriched_games_data.adjusted_week > 3]
    print(
        f"enriched_games_filtered.loc[enriched_games_filtered.team == 'Washington']: {enriched_games_filtered.loc[enriched_games_filtered.team == 'Washington']}")

    enriched_games_filtered = enriched_games_filtered.assign(
        talent_rating_differential=lambda x: x.team_stat_earning_ply_rating - x.rating_opponent).assign(
        elo_differential=lambda x: x.pregame_elo - x.opponent_pregame_elo)

    fbs_enriched_games_filtered = enriched_games_filtered.merge(
        weekly_adjusted_ppa_df[['school', 'week', 'adjOff']], how='left', left_on=['team', 'week'],
        right_on=['school', 'week'])
    fbs_enriched_games_filtered = fbs_enriched_games_filtered.merge(
        weekly_adjusted_ppa_df[['school', 'week', 'adjDef']], how='left', left_on=['opponent', 'week'],
        right_on=['school', 'week']).drop(columns=['school_x', 'school_y'])
    fbs_enriched_games_filtered.dropna(subset=['talent_rating_differential', 'adjOff', 'adjDef'], inplace=True)

    return fbs_enriched_games_filtered



def seed_base_forecast_data(enriched_games_filtered_df,
                            enriched_games_filtered_pw_df,
                            df_get_games_all):
    enrich_games_plug_df = enriched_games_filtered_pw_df.loc[
        ~enriched_games_filtered_pw_df.team.isin(enriched_games_filtered_df['team'].unique())]

    enriched_games_plugged_df = pd.concat([enriched_games_filtered_df, enrich_games_plug_df])

    forecast_prep_df = enriched_games_plugged_df.drop(
        columns=['game_id', 'week', 'adjusted_week', 'season_type', 'completed',
                 'conference_opponent', 'abbreviation_opponent', 'opponent', 'rating_opponent',
                 'opponent_pregame_elo', 'talent_rating_differential', 'elo_differential', 'home_away', 'points',
                 'index'])


    games_df = df_get_games_all[
        ['id', 'week', 'team', 'season_type', 'home_away', 'completed', 'opponent', 'points']]

    seeding_game_stat_df = games_df.merge(forecast_prep_df, how='left', on='team').rename(
        columns={'id': 'game_id'}).dropna(subset=['abbreviation_team'])

    fill_df = seeding_game_stat_df[
        ['team', 'abbreviation_team', 'conference', 'team_stat_earning_ply_rating', 'pregame_elo']]

    seeded_games = seeding_game_stat_df.merge(fill_df, how='inner', left_on='opponent', right_on='team',
                                              suffixes=['_team', '_opponent']).drop(
        columns=['team_opponent']).rename(columns={'team_team': 'team', 'conference_team': 'conference',
                                                   'abbreviation_team_team': 'abbreviation_team',
                                                   'team_stat_earning_ply_rating_team': 'team_stat_earning_ply_rating',
                                                   'pregame_elo_team': 'pregame_elo',
                                                   'abbreviation_team_opponent': 'abbreviation_opponent',
                                                   'team_stat_earning_ply_rating_opponent': 'rating_opponent',
                                                   'pregame_elo_opponent': 'opponent_pregame_elo'})

    seeded_games['talent_rating_differential'] = seeded_games['team_stat_earning_ply_rating'] - seeded_games[
        'rating_opponent']
    seeded_games['elo_differential'] = seeded_games['pregame_elo'] - seeded_games['opponent_pregame_elo']
    seeded_games['adjusted_week'] = seeded_games['week']

    return seeded_games



