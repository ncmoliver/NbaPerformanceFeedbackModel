# 🏀 NBA Stats Query Model: Natural Language to SQL 🔥

![Alt text](download.jpg)

## Overview

In this project we will collaboratively provide feedback based on individual game statistics analyze using advanced Machine Learning methodologies to find how individuals perform in the NBA. Our statistics will incorporate transformer models, natural language processing (NLP) techniques, and other tools acquired throughout the course, in addition to at least one new technology SQL that we haven’t covered together.

Welcome to the NBA Stats Query Model, an intelligent system designed to revolutionize how we interact with basketball data! This project bridges the gap between casual NBA fans, data analysts, and AI by enabling users to ask natural language questions about NBA stats and receive accurate, natural language responses. The system seamlessly translates user questions into SQL queries and retrieves relevant data to provide insightful answers.

# 🚀 Features

**Natural Language Input:** Users can ask questions in plain English (e.g., "Who scored the most points in 2020?").  
**SQL Query Generation**: Automatically converts questions into optimized SQL queries.  
**Accurate Responses**: Provides natural language responses based on the retrieved data.  
**Contextual Understanding**: The model leverages enriched and preprocessed data to enhance the quality and relevance of its answers.

# 🛠️ Preprocessing Steps

To ensure the model operates effectively, the data underwent meticulous preprocessing:

## 1. Team Name Mapping:

- Abbreviated team names (e.g., OKC, LAL) were mapped to their full names (e.g., Oklahoma City Thunder, Los Angeles Lakers).
- This added context improves the model’s ability to handle queries referencing specific teams.

## 2. Column Renaming:

- All column names in the database were renamed to descriptive, user-friendly formats.
- Example: PTS → POINTS, FG_PCT → FIELD_GOAL_PERCENTAGE.
- This step ensures clarity and relevance when parsing and querying data.

## 3. Database Restructuring:

- The original database was normalized into three key tables:
  1. Players: Contains player details and their team affiliations.
  2. Teams: Includes team information such as names and IDs.
  3. Stats: Holds statistical data for players across seasons.
- This structure optimizes the database for efficient querying and retrieval.

# 🎯 Goal

The primary goal of this project is to:

Enable Natural Language Processing (NLP): Understand user queries and convert them into SQL.
Deliver Human-Like Responses: Provide accurate and engaging natural language answers to user questions.
Empower Data Accessibility: Simplify access to complex NBA stats for fans and analysts alike.

1. Take natural language query from
2. Translate (using code LLM) the natural language query from #1 into SQL command
3. Run the query from #2 against the db

#GRADIO FRONT-END
We want to build a Gradio front-end that:

Takes a natural language query from the user.
Translates it into an SQL query using Llama LLM.
Executes the SQL query against your database and shows the results.
I'll guide you in setting up this interface.

Overview of What We’ll Do
Install Required Libraries.
Set Up Environment Variables.
Write the Gradio Interface Code.
Run and Test the Gradio Interface.

# References

#### Datasets

[Kaggle Dataset - 1991-2021 NBA Stats](https://www.kaggle.com/datasets/vivovinco/19912021-nba-stats?select=players.csv)  
[Kaggle Dataset - NBA STATS Dataset for last 10 years](https://www.kaggle.com/datasets/shivamkumar121215/nba-stats-dataset-for-last-10-years)
