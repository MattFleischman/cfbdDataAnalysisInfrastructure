#data ingestion constants
cfbd_api_input_map = {'get_games': {'year': 'year', 'season_type': 'season_type', 'week': 'week'},
                      'get_team_game_stats': {'year': 'year', 'season_type': 'season_type', 'week': 'week'},
                      'get_advanced_team_game_stats': {'year': 'year', 'season_type': 'season_type', 'week': 'week'},
                      'get_fbs_teams': {'year': 'year'},
                      'get_lines': {'year': 'year', 'week': 'week'},
                      'get_player_season_stats': {'year': 'year', 'season_type': 'season_type', 'start_week': 'week', 'end_week': 'week'},
                      'get_plays': {'year': 'year', 'season_type': 'season_type', 'week': 'week'},
                      'get_transfer_portal': {'year': 'year'},
                      'get_roster': {'year': 'year'},
                      'get_recruiting_groups': {'start_year': 'year', 'end_year': 'year'},
                      'get_recruiting_players': {'year': 'year'}
                      }



cfbd_prefix = "CFBD_Analysis/"
archive_prefix = "archive/"
extract_prefix = "data_extract"
txt_ext = ".txt"

cfbd_archive = archive_prefix + cfbd_prefix
extract_append = extract_prefix+txt_ext

#pre_pred_transformations constants
df_get_games_trimmed_columns = ['id', 'season', 'week', 'season_type', 'start_date', 'completed', 'neutral_site', 'conference_game',
             'attendance', 'venue_id', 'venue', 'home_id', 'home_team', 'home_conference', 'home_division',
             'home_points',
             'home_pregame_elo', 'away_id', 'away_team', 'away_conference', 'away_division', 'away_points',
             'away_pregame_elo', 'excitement_index']

df_get_games_home_columns = ['id', 'season', 'week', 'season_type', 'start_date', 'completed',
                                                  'neutral_site', 'conference_game', 'attendance', 'venue_id', 'venue',
                                                  'home_id', 'home_team', 'away_team', 'home_conference',
                                                  'home_division',
                                                  'home_points', 'away_points', 'home_pregame_elo', 'away_pregame_elo',
                                                  'excitement_index']

df_get_games_home_rename_dict = {'home_id': 'team_id', 'home_team': 'team', 'home_conference': 'conference',
                                 'home_division': 'division',
                                 'home_points': 'points', 'home_pregame_elo': 'pregame_elo', 'away_team': 'opponent',
                                 'away_points': 'opponent_points', 'away_pregame_elo': 'opponent_pregame_elo'}

df_get_games_away_columns = ['id', 'season', 'week', 'season_type', 'start_date', 'completed',
                                                  'neutral_site', 'conference_game', 'attendance', 'venue_id', 'venue',
                                                  'away_id', 'away_team', 'home_team',
                                                  'away_conference', 'away_division', 'away_points', 'home_points',
                                                  'away_pregame_elo', 'home_pregame_elo', 'excitement_index']

df_get_games_away_rename_dict = {'away_id': 'team_id', 'away_team': 'team', 'away_conference': 'conference',
                                 'away_division': 'division',
                                 'away_points': 'points', 'away_pregame_elo': 'pregame_elo', 'home_team': 'opponent',
                                 'home_points': 'opponent_points', 'home_pregame_elo': 'opponent_pregame_elo'}

advanced_team_enriched_games_data_columns = ['id_x', 'home_away_x', 'season_x', 'week_x', 'season_type', 'completed', 'team_id', 'school_x',
         'conference_team', 'conference_opponent',
         'division_x', 'points_x', 'opponent_points', 'pregame_elo',
         'opponent_x', 'stars_team', 'rating_team', 'logo_primary', 'logo_alt',
         'abbreviation_team', 'abbreviation_opponent',
         'group_average_rating_team', 'opponent_pregame_elo',
         'group_average_stars_team', 'stars_opponent', 'rating_opponent', 'group_average_rating_opponent',
         'group_average_stars_opponent', 'stat_completionAttempts', 'stat_defensiveTDs', 'stat_firstDowns',
         'stat_fourthDownEff', 'stat_fumblesLost', 'stat_fumblesRecovered',
         'stat_interceptionTDs', 'stat_interceptionYards', 'stat_interceptions',
         'stat_kickReturnTDs', 'stat_kickReturnYards', 'stat_kickReturns',
         'stat_kickingPoints', 'stat_netPassingYards', 'stat_passesDeflected',
         'stat_passesIntercepted', 'stat_passingTDs', 'stat_possessionTime',
         'stat_puntReturnTDs', 'stat_puntReturnYards', 'stat_puntReturns',
         'stat_qbHurries', 'stat_rushingAttempts', 'stat_rushingTDs',
         'stat_rushingYards', 'stat_sacks', 'stat_tackles',
         'stat_tacklesForLoss', 'stat_thirdDownEff', 'stat_totalFumbles',
         'stat_totalPenaltiesYards', 'stat_totalYards', 'stat_turnovers',
         'stat_yardsPerPass', 'stat_yardsPerRushAttempt']

get_plays_columns = ['game_id', 'home', 'away', 'offense', 'defense', 'ppa']

advanced_team_enriched_games_data_rename_dict = {'id_x': 'game_id', 'season_x': 'season', 'home_away_x': 'home_away',
                                                 'week_x': 'week', 'division_x': 'division',
                                                 'school_x': 'team', 'conference_team': 'conference',
                                                 'points_x': 'points', 'stars_team': 'team_stat_earning_ply_stars',
                                                 'rating_team': 'team_stat_earning_ply_rating', 'opponent_x': 'opponent'}

advanced_team_enriched_games_data_lookback_columns = ['team', 'adjusted_week', 'total_offense_yards', 'third_down_pct', 'stat_firstDowns', 'points']

advanced_team_enriched_games_data_lookback_rename_dict = {'total_offense_yards': '3M_lookback_offyards', 'stat_firstDowns': '3M_lookback_firstDowns',
                                                            'third_down_pct': '3M_lookback_third_down_pct', 'points': '3M_lookback_points_scored'}

lookback_enrichment_columns = ['3M_lookback_offyards', '3M_lookback_third_down_pct', '3M_lookback_points_scored', '3M_lookback_firstDowns']

game_lines_output_columns = ['game_id', 'week', 'home', 'away', 'home_logo', 'away_logo', 'home_elo', 'away_elo', 'home_talent_rating',
         'away_talent_rating', 'home_pred_points', 'away_pred_points', 'formatted_spread', 'over_under']
game_lines_output_rename_dict = {'formatted_spread': 'betting_spread', 'over_under': 'betting_o_u'}

filtered_betting_lines_columns = ['id', 'week', 'formatted_spread', 'over_under']


points_forecast_columns = ['game_id','completed','team', 'conference', 'abbreviation_team', 'week','season_type','home_away',
                           'logo_primary','logo_alt','opponent', 'conference_opponent', 'abbreviation_opponent', 'team_stat_earning_ply_rating',
                           'stat_firstDowns','rating_opponent','pregame_elo','opponent_pregame_elo',
                           'total_offense_yards','third_down_pct','points','adjusted_week',
                           '3M_lookback_offyards','3M_lookback_third_down_pct','3M_lookback_points_scored',
                           '3M_lookback_firstDowns','talent_rating_differential','elo_differential','adjOff',
                           'adjDef','predicted_score']

#TODO: add below fields below: 3M_lookback_firstDowns', '3M_lookback_points_scored|', '3M_lookback_third_down_pct|', '3M_lookback_offyards|','total_offense_yards|','third_down_pct|'
prediction_output_data_set_home_columns = ['game_id', 'week', 'team', 'logo_primary', 'conference', 'abbreviation_team', 'pregame_elo',
                                          'team_stat_earning_ply_rating', 'predicted_score','3M_lookback_firstDowns',
                                           '3M_lookback_points_scored', '3M_lookback_third_down_pct',
                                           '3M_lookback_offyards','total_offense_yards','third_down_pct',
                                           'adjOff','adjDef', 'points']

prediction_output_data_set_home_rename_dict = {'team': 'home','logo_primary': 'home_logo', 'conference': 'home_conference',
                                               'abbreviation_team': 'home_abbreviation','pregame_elo': 'home_elo',
                 'team_stat_earning_ply_rating': 'home_talent_rating','predicted_score': 'home_pred_points',
                  '3M_lookback_firstDowns': 'home_3W_lookback_firstDowns', '3M_lookback_points_scored': 'home_3W_lookback_points_scored',
                  '3M_lookback_third_down_pct': 'home_3W_lookback_third_down_pct', '3M_lookback_offyards': 'home_3W_lookback_offyards',
                  'total_offense_yards': 'home_total_offense_yards','third_down_pct': 'home_third_down_pct','adjOff': 'home_adjOff',
                  'adjDef': 'away_adjDef', 'points': 'home_points_actual'}

#ajd defense relates to the opposing team

#TODO: add below fields below: 3M_lookback_firstDowns', '3M_lookback_points_scored|', '3M_lookback_third_down_pct|', '3M_lookback_offyards|','total_offense_yards|','third_down_pct|'
prediction_output_data_set_away_columns = ['game_id', 'week', 'team', 'conference', 'abbreviation_team', 'logo_primary', 'pregame_elo',
                                            'team_stat_earning_ply_rating', 'predicted_score','3M_lookback_firstDowns',
                                           '3M_lookback_points_scored', '3M_lookback_third_down_pct',
                                           '3M_lookback_offyards','total_offense_yards','third_down_pct',
                                           'adjOff','adjDef', 'points']


prediction_output_data_set_away_rename_dict = {'team': 'away','logo_primary': 'away_logo', 'conference': 'away_conference',
                                               'abbreviation_team': 'away_abbreviation', 'pregame_elo': 'away_elo',
                     'team_stat_earning_ply_rating': 'away_talent_rating','predicted_score': 'away_pred_points',
                      '3M_lookback_firstDowns': 'away_3W_lookback_firstDowns', '3M_lookback_points_scored': 'away_3W_lookback_points_scored',
                      '3M_lookback_third_down_pct': 'away_3W_lookback_third_down_pct', '3M_lookback_offyards': 'away_3W_lookback_offyards',
                      'total_offense_yards': 'away_total_offense_yards','third_down_pct': 'away_third_down_pct','adjOff': 'away_adjOff',
                      'adjDef': 'home_adjDef','points': 'away_points_actual'}
#ajd defense relates to the opposing team

prediction_output_df_columns = ['game_id', 'week', 'home', 'away', 'home_logo', 'away_logo', 'home_abbreviation', 'away_abbreviation',
                                'home_conference', 'away_conference', 'home_elo', 'away_elo', 'home_talent_rating',
         'away_talent_rating', 'home_pred_points', 'away_pred_points','formatted_spread', 'over_under', 'home_3W_lookback_offyards',
         'away_3W_lookback_offyards', 'home_3W_lookback_third_down_pct', 'away_3W_lookback_third_down_pct',
         'home_3W_lookback_points_scored', 'away_3W_lookback_points_scored', 'home_3W_lookback_firstDowns',
         'away_3W_lookback_firstDowns', 'home_adjOff', 'away_adjOff', 'home_adjDef', 'away_adjDef']

prediction_output_df_rename_dict = {'formatted_spread': 'betting_spread', 'over_under': 'betting_o_u'}

fit_data_set_columns = ['points', 'talent_rating_differential', 'elo_differential', 'adjOff', 'adjDef']

prediction_data_set_columns = ['talent_rating_differential', 'elo_differential', 'adjOff', 'adjDef']
player_season_stats_columns = ['player_id']

offStr = 'offense'  # Column of interest, the team/player we want to adjust
hfaStr = 'hfa'  # Homefield Advantage column name
defStr = 'defense'  # Opponent column name
stat = 'ppa'  # stat to adjust on

default_forecasting_path = "Transformed/default_forecasting_dataset/"
stacked_game_path = "Transformed/stacked_game_details/"
adjusted_ppa_path = "Transformed/opponent_adjusted_ppa/"
forecast_output_path = "Transformed/points_forecast_output/"
post_forecast_adjustments_path =  "Transformed/post_forecast_adjustments/"
transformed_recruiting_prefix = "Transformed/transformed_recruiting_stats/"
team_game_stats_prefix = "GamesApi_get_team_game_stats/"
advanced_team_game_stats_prefix = "StatsApi_get_advanced_team_game_stats/"
betting_line_path = "BettingApi_get_lines/"
fbs_teams_path = "TeamsApi_get_fbs_teams/"
aggregate_output_prefix = "output/"
game_summary_prediction_file_name = "output_prediction.txt"
