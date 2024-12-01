# **NBA Performance Feedback Model**

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

NBA-Performance-Feedback-Model/
├── data/
│   ├── nba_1991_2021.csv
│   ├── nba_last_10_years.csv
├── scripts/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── gradio_interface.py
├── .env
├── app.py
├── requirements.txt
├── README.md

### **References**

#### **Datasets**
- [1991–2021 NBA Stats Dataset](https://www.kaggle.com/datasets)
- [NBA Stats for the Last 10 Years](https://www.kaggle.com/datasets)

#### **Technologies**
- [Llama LLM](https://github.com/) for natural language to SQL translation.
- [Gradio](https://gradio.app/) for creating the interactive front-end.
