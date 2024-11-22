# utils.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
from transformers import LlamaTokenizer, LlamaForCausalLM
import sqlite3


def reduce_positions(df):
    """
    Function Name: reduce_positions

    Description: This function takes in a dataframe and modifies the 'Pos' column by 
    splitting each value on the '-' character, which returns the primary position only. 
    After splitting, values that are too general (such as 'Forward' or 'Guard') are 
    removed due to their lack of specificity.

    Example: The value 'SF-SG' would be split to just 'SF'.

    Parameters / Input: A DataFrame with a column 'Pos'.

    Output: DataFrame with the 'Pos' column updated to contain only primary positions.
    """
    # Split each entry in the 'Pos' column by '-' and take the first part
    df['Pos'] = df['Pos'].str.split('-').str[0]
    return df


def reformat_columns(df):
    """
    Function Name: reformat_columns

    Description: This function reformats certain columns in the DataFrame. It replaces 
    any occurrences of '%20' with spaces and underscores with spaces in the 'Season_type' 
    column, extracts the base year from the 'year' column by removing additional 
    season information, and removes any columns with 'Unnamed' in the name.

    Example: The value '2012-13' in the 'year' column would be reformatted to '2012'.

    Parameters / Input: A DataFrame with columns 'Season_type' and 'year'.

    Output: A cleaned DataFrame with reformatted columns.
    """
    # Reformat the Season_type column to remove %20
    df['Season_type'] = df['Season_type'].str.replace('%20', ' ', regex=False).str.replace('_', ' ', regex=False)
    # Reformat the year column to use the base year `2012-13` to `2012`
    df['year'] = df['year'].str.split('-').str[0]
    # drop all columns with "unnamed"
    df = df.loc[:, ~df.columns.str.contains("Unnamed")]
        
    # Return the clean dataframe
    return df


# Create a function that reformats the dataframes and combines them into one dataframe
def combine_dataframes(list_of_dataframes):
    """
    Function Name: combine_dataframes

    Description: This function reformats and combines two DataFrames, one representing 
    regular season data and the other representing playoff data. Each DataFrame is 
    reformatted using the reformat_columns function and then combined vertically.

    Example: Combines two DataFrames containing 'Regular Season' and 'Playoff' data.

    Parameters / Input: A list of two DataFrames.

    Output: A single combined DataFrame with reformatted columns.
    """
    results = [reformat_columns(df) for df in list_of_dataframes]
    # Separate them back into individual sets
    regular_season_data = results[0]
    playoff_data = results[1]
    # Use pd.concat to combine the dataframe using axis=0
    combined_df = pd.concat([regular_season_data, playoff_data], axis=0, ignore_index=True)
    return combined_df



# Create a function to encode categorical columns
def encode_categorical_columns(df):
    """
    Function Name: encode_categorical_columns

    Description: This function encodes categorical columns in the DataFrame, including 
    season type, player, team, and position. The 'Season_type' column is encoded as 0 
    for Regular Season and 1 for Playoffs, while the player, team, and position columns 
    are label-encoded. Mappings for each encoding are saved for potential future decoding.

    Example: 'Regular Season' in the 'Season_type' column is encoded as 0, and player 
    names are encoded as integers.

    Parameters / Input: A DataFrame with columns 'Season_type', 'PLAYER', 'TEAM', and 'Pos'.

    Output: A tuple containing the updated DataFrame, along with dictionaries for 
    player, team, and position encodings.
    """
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
    df = df.drop(columns=['Pos', 'PLAYER', 'TEAM', 'PLAYER_ID', 'TEAM_ID', 'Season_type', 'AST_TOV', 'STL_TOV'])
    
    # Return the updated dataframe, player mappings, and  team mappings
    return df, player_mapping, team_mapping, position_mapping




def divide_by_games_played(df):
    """
    Function Name: divide_by_games_played

    Description: This function takes a DataFrame and divides each numerical column 
    by the 'games_played' column to calculate per-game statistics. It uses error 
    handling to avoid division by zero and replaces any infinite or NaN results with NaN. 
    After calculations, the 'games_played' column is dropped from the DataFrame.

    Example: Total points in the 'points' column are divided by 'games_played' to get 
    points per game.

    Parameters / Input: A DataFrame with a 'games_played' column and other numerical 
    columns representing totals.

    Output: A DataFrame with per-game statistics in place of totals.
    """
     
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


##############################################
# Function for the database calls
##############################################

# Step 1: Connect to the SQLite database
def connect_to_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

# Step 2: Query the database
def query_database(conn, user_query):
    cursor = conn.cursor()
    try:
        cursor.execute(user_query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return f"Database error: {e}"

# Step 3: Format results for the model
def format_results(results):
    formatted_text = "Query Results:\n"
    for row in results:
        formatted_text += " | ".join(map(str, row)) + "\n"
    return formatted_text

# Step 4: Load the Llama model
def load_llama_model(model_name, access_token):
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    model = LlamaForCausalLM.from_pretrained(model_name)
    return tokenizer, model

# Step 5: Generate response from the model
access_token = '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'
def query_llama_model(tokenizer, model, input_text):
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True,max_length=2048)
    outputs = model.generate(**inputs, max_new_tokens=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

