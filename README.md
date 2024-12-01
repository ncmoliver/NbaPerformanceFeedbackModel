![Alt text](download.jpg)
# 🏀 NBA Stats Conversational AI: Natural Language to SQL and Back!

## 🌟 Project Overview
This project is designed to redefine how we interact with basketball statistics by using the power of Natural Language Processing (NLP) and SQL. This project also incorporates a user-friendly Gradio front-end, allowing natural language queries to be seamlessly translated into SQL commands using Llama LLM, executed against a database, and returned as user-friendly results. 
This model will:
- Translate the question into an SQL query to pull data from a structured database.
- Provide a natural language response with the results.

Whether you're a basketball analyst, an NBA enthusiast, or a curious data scientist, this project makes NBA stats more accessible and engaging!

---

## 🎯 Project Goals
- Accept natural language questions about NBA statistics.
- Convert questions into SQL queries to fetch relevant data.
- Generate natural language responses to answer user queries intuitively.

---

## Key Features
- **Advanced ML Analytics**: Analyze player performance using state-of-the-art transformer models and NLP techniques.
- **Dynamic Query Translation**: Transform natural language queries into SQL commands with high accuracy using Llama LLM.
- **Interactive Front-End**: A Gradio-based interface for smooth interaction, data querying, and visualization.
- **Comprehensive Dataset Integration**:
Kaggle Dataset: 1991–2021 NBA Stats
Kaggle Dataset: NBA Stats Dataset for the Last 10 Years
Exploration of New Technologies: Integration of SQL as a database querying tool not covered previously in the course.

---

## 🛠️ Preprocessing Steps
To make the system highly effective and context-aware, we performed extensive preprocessing, including:

### 1. Team Name Mapping
We mapped abbreviated team names (e.g., `OKC`, `LAL`) to their full names (e.g., `Oklahoma City Thunder`, `Los Angeles Lakers`) to provide more context to the model and improve query accuracy.

### 2. Column Renaming
All database columns were renamed to more descriptive names for clarity and relevance. For example:
- `PTS` → `POINTS`
- `FG_PCT` → `FIELD_GOAL_PERCENTAGE`
- `REB` → `TOTAL_REBOUNDS`

### 3. Database Restructuring
The original dataset was restructured into three normalized tables for efficient querying:
- **`players`**: Contains player details and their team affiliations.
- **`teams`**: Stores information about NBA teams.
- **`stats`**: Holds detailed player statistics for various seasons.

This design ensures faster queries, better organization, and a user-friendly schema for the AI model.

---

### **References**
- [1991–2021 NBA Stats Dataset](https://www.kaggle.com/datasets)
- [NBA Stats for the Last 10 Years](https://www.kaggle.com/datasets)

___

## 💡 How It Works
### **Input:**
Users ask questions like:
- "Who scored the most points for the Lakers in 2020?"
- "Which player had the highest assists for the Miami Heat in 2021?"

### **Processing:**
The question is converted into a structured SQL query:
```sql
SELECT PLAYER_NAME, POINTS 
FROM stats 
JOIN teams ON stats.TEAM_ID = teams.TEAM_ID 
WHERE TEAM_NAME = 'Los Angeles Lakers' AND YEAR = 2020 
ORDER BY POINTS DESC LIMIT 1;
