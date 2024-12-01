
# 🏀 NBA Stats Query Model: Natural Language to SQL 🔥

![Alt text](download.jpg)
## **Overview**
The **NBA Performance Feedback Model** is a tool designed to analyze individual NBA player performance by combining natural language processing (NLP), advanced machine learning (ML) techniques, and database querying through SQL. This project allows users to input natural language queries and retrieve meaningful insights from NBA datasets spanning decades, providing dynamic and interactive feedback on player statistics.

Key features include:
- Translating natural language queries into SQL commands using Llama LLM.
- Executing SQL queries against NBA datasets.
- Displaying results in an intuitive Gradio interface.

---

## **Features**
- **Advanced Analytics**: Leverage transformer models and NLP techniques to analyze player statistics.
- **Natural Language to SQL Translation**: Utilize Llama LLM for seamless query translation.
- **Gradio Front-End**: Interactive interface for smooth querying and result visualization.
- **Extensive Dataset Support**:
  - Kaggle Dataset: *1991–2021 NBA Stats*
  - Kaggle Dataset: *NBA Stats Dataset for the Last 10 Years*
- **Integration of New Technologies**: Incorporates SQL for database querying.

---

## **Project Workflow**

### **Gradio Front-End**
1. **Input**: Users provide natural language queries.
2. **Processing**:
   - Queries are translated into SQL using Llama LLM.
   - SQL commands are executed on the connected database.
3. **Output**: Results are displayed in a user-friendly format.

Example query:  
> "Show me the top 5 players with the highest points per game in the 2020 season."

---

## **Setup and Installation**

### **1. Prerequisites**
- Python 3.8 or higher
- Database software (PostgreSQL or SQLite recommended)
- Required Python libraries:
  - Gradio
  - SQLAlchemy
  - Transformers
  - Python-dotenv

### **2. Install Required Libraries**
Run the following command to install the dependencies:
```bash
pip install gradio sqlalchemy transformers python-dotenv



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
