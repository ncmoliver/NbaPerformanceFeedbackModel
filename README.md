![Alt text](download.jpg)
# 🏀 NBA Stats Conversational AI: Natural Language to SQL and Back! 🚀

## 🌟 Project Overview
This project is designed to redefine how we interact with basketball statistics by using the power of Natural Language Processing (NLP) and SQL. Users can ask natural language questions about NBA stats, and the model will:
- Translate the question into an SQL query to pull data from a structured database.
- Provide a natural language response with the results.

Whether you're a basketball analyst, an NBA enthusiast, or a curious data scientist, this project makes NBA stats more accessible and engaging!

---

## 🎯 Project Goals
- Accept natural language questions about NBA statistics.
- Convert questions into SQL queries to fetch relevant data.
- Generate natural language responses to answer user queries intuitively.

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
