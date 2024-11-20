# utils.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()


def reduce_positions(df):
    # Split each entry in the 'Pos' column by '-' and take the first part
    df['Pos'] = df['Pos'].str.split('-').str[0]
    return df


def reformat_columns(df):
    # Reformat the Season_type column to remove %20
    df['Season_type'] = df['Season_type'].str.replace('%20', ' ', regex=False).str.replace('_', ' ', regex=False)
    # Reformat the year column to use the base year `2012-13` to `2012`
    df['year'] = df['year'].str.split('-').str[0]
    # drop all columns with "unnamed"
    df = df.loc[:, ~df.columns.str.contains("Unnamed")]
        
    # Return the clean dataframe
    return df

def combine_dataframes(list_of_dataframes):
    results = [reformat_columns(df) for df in list_of_dataframes]
    # Separate them back into individual sets
    regular_season_data = results[0]
    playoff_data = results[1]
    # Use pd.concat to combine the dataframe using axis=0
    combined_df = pd.concat([regular_season_data, playoff_data], axis=0, ignore_index=True)
    return combined_df

# Create a function to encode categorical columns
def encode_categorical_columns(df):

    ## Encode the `Season_type` columns, 0 for Regular Season games and 1 for Playoff games
    df['season_type_encoded'] = df['Season_type'].apply(lambda x: 0 if x == 'Regular Season' else 1)
    
    # Initialize LabelEncoder for players and teams column
    player_encoder = LabelEncoder()
    team_encoder = LabelEncoder()
    position_encoder = LabelEncoder()


    ## Use LabelEncoder to encode the `PLAYER`, `TEAM`, `POSITION` columns
    df['player_encoded'] = player_encoder.fit_transform(df['PLAYER'])
    df['team_encoded'] = team_encoder.fit_transform(df['TEAM'])
    df['position_encoded'] = position_encoder.fit_transform(df['Pos'])
    
    # Save mappings to decode later
    player_mapping = dict(zip(player_encoder.classes_, player_encoder.transform(player_encoder.classes_)))
    team_mapping = dict(zip(team_encoder.classes_, team_encoder.transform(team_encoder.classes_)))
    position_mapping = dict(zip(team_encoder.classes_, team_encoder.transform(team_encoder.classes_)))

    # Drop original player, team, and position columns
    df = df.drop(columns=['Pos', 'PLAYER', 'TEAM', 'PLAYER_ID', 'TEAM_ID', 'Season_type'])
    
    # Return the updated dataframe, player mappings, and  team mappings
    return df, player_mapping, team_mapping, position_mapping


def divide_by_games_played(df):
    # Check if 'games_played' column exists in the DataFrame
    if 'games_played' not in df.columns:
        raise ValueError("The DataFrame does not contain a 'games_played' column.")
    
    # Divide each numerical column by the 'games_played' column
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        if col != 'games_played':  # Exclude 'games_played' from the division
            with np.errstate(divide='ignore', invalid='ignore'):
                df[col] = round(df[col] / df['games_played'],1)
                # Replace any infinite or NaN values (from division by zero) with NaN
                df[col] = df[col].replace([np.inf, -np.inf], np.nan)
    
    df = df.drop(columns=('games_played'))
    
    return df


def calculate_shooting_production(df):
    two_made_weight = float(os.getenv('TWO_POINTS_MADE',1))
    two_missed_weight = float(os.getenv('TWO_POINTS_MISSED',1))
    three_made_weight = float(os.getenv('THREE_POINTS_MADE', 1))
    three_missed_weight = float(os.getenv('THREE_POINTS_MISSED', 1))
    

    # Calculate missed shots
    df['FGMI'] = df['FGA'] - df['FGM']
    df['FG3MI'] = df['FG3A'] - df['FG3M']
    df['FTMI'] = df['FTA'] - df['FTM']
    
    # Calculate two, three, and ft production
    df['two_production'] = (df['FGM'] * two_made_weight) - (df['FGMI'] * two_missed_weight)
    df['three_production'] = (df['FG3M'] * three_made_weight) - (df['FG3MI'] * three_missed_weight)
    df['ft_production'] = df['FTM'] - df['FTMI']
    
    df['total_shooting_production'] = df['two_production'] + df['three_production'] + df['ft_production']
    return df


def calculate_offensive_anx(df):
    # Retrieve and convert weights from environment variables
    or_weight = float(os.getenv('OFF_REBOUND', 0))
    ast_weight = float(os.getenv('AST', 0))
    to_weight = float(os.getenv('TO', 0))
    
    # Ensure numeric data in relevant columns
    df['OREB'] = pd.to_numeric(df['OREB'], errors='coerce')
    df['AST'] = pd.to_numeric(df['AST'], errors='coerce')
    df['TOV'] = pd.to_numeric(df['TOV'], errors='coerce')

    # Calculate weighted values
    df['weighted_or'] = df['OREB'] * or_weight
    df['weighted_ast'] = df['AST'] * ast_weight
    df['weighted_to'] = df['TOV'] * (to_weight)
    
    # Calculate Total Offensive Anx
    df['total_offensive_anx'] = df['weighted_or'] + df['weighted_ast'] + df['weighted_to'] 
    return df



def calculate_defensive_anx(df):
    # Retrieve and convert weights from environment variables
    dreb_weight = float(os.getenv('DEF_REBOUND', 0))
    stl_weight = float(os.getenv('STL', 0))
    blk_weight = float(os.getenv('BLK', 0))
    pf_weight = float(os.getenv('PF', 0))
    
    # Ensure numeric data in relevant columns
    df['DREB'] = pd.to_numeric(df['DREB'], errors='coerce')
    df['STL'] = pd.to_numeric(df['STL'], errors='coerce')
    df['BLK'] = pd.to_numeric(df['BLK'], errors='coerce')
    df['PF'] = pd.to_numeric(df['PF'], errors='coerce')

    # Calculate weighted values
    df['weighted_dr'] = df['DREB'] * dreb_weight
    df['weighted_stl'] = df['STL'] * stl_weight
    df['weighted_blk'] = df['BLK'] * blk_weight
    df['weighted_pf'] = df['PF'] * pf_weight
    
    # Calculate Total Defensive Anx
    df['total_defensive_anx'] = df['weighted_dr'] + df['weighted_stl'] + df['weighted_blk'] + df['weighted_pf']
    return df

# Calculate Total Production
def calculate_total_player_production(df):
    df['total_production'] = df['total_shooting_production'] + df['total_offensive_anx'] + df['total_defensive_anx']
    return df

