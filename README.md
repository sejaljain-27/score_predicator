# T20 First Innings Score Predictor
A Machine Learning project that predicts the final first-innings score in a T20 International cricket match using real-time match conditions.
## Project Overview
This project uses historical T20 International match data from Cricsheet to predict the final score of a batting team based on the current state of the innings. The model analyzes factors such as current score, wickets remaining, run rate, venue, and recent scoring trends to generate accurate score predictions.
## Features
* Predicts final first-innings T20 score
* Built using real-world Cricsheet match data
* Feature engineering from ball-by-ball match records
* Interactive Streamlit web application
* XGBoost Machine Learning model
* Real-time score prediction interface
## Dataset
Source: Cricsheet T20 International Dataset
Data includes:
* Batting Team
* Bowling Team
* Venue
* Current Score
* Balls Left
* Wickets Left
* Current Run Rate
* Runs Scored in Last Five Overs
## Tech Stack
* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
## Machine Learning Pipeline
1. Data Extraction from YAML files
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. Model Training using XGBoost
5. Deployment using Streamlit
## Model Performance
* R² Score: 0.96
* Mean Absolute Error (MAE): 2.75 Runs
##  Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
## Application Preview
The application allows users to select:
* Batting Team
* Bowling Team
* Venue
* Current Score
* Overs Completed
* Wickets Lost
* Runs Scored in Last Five Overs
and instantly predicts the final innings score.
Built using Machine Learning, Cricket Analytics, and Streamlit.
#live demo
https://score-predicator.onrender.com/
