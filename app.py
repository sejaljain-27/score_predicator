import streamlit as st
import pickle
import pandas as pd
import numpy as np
pipe=pickle.load(open('pipe.pkl','rb'))
teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Pakistan',
    'Sri Lanka'
]
venue=['R Premadasa Stadium',
 'Shere Bangla National Stadium',
 'Dubai International Cricket Stadium',
 'New Wanderers Stadium',
 'Pallekele International Cricket Stadium',
 'Sylhet Stadium',
 'Kensington Oval, Bridgetown',
 'Beausejour Stadium, Gros Islet',
 'Newlands',
 'County Ground',
 'Kennington Oval',
 'Melbourne Cricket Ground',
 'Galle International Stadium',
 'Kingsmead',
 'Eden Park',
 'Trent Bridge',
 'Feroz Shah Kotla',
 'Zahur Ahmed Chowdhury Stadium',
 'M Chinnaswamy Stadium',
 'Westpac Stadium',
 'Seddon Park',
 'Old Trafford',
 'The Rose Bowl',
 'Sharjah Cricket Stadium',
 'Senwes Park',
 'Eden Gardens',
 "Lord's",
 'SuperSport Park',
 'Wankhede Stadium',
 'Sydney Cricket Ground',
 'Vidarbha Cricket Association Stadium, Jamtha',
 'Stadium Australia',
 'Edgbaston',
 'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa',
 'Rawalpindi Cricket Stadium',
 'Haslegrave Ground',
 'Sheikh Zayed Stadium',
 'Punjab Cricket Association IS Bindra Stadium, Mohali',
 'Narendra Modi Stadium, Ahmedabad',
 'Bir Sreshtho Flight Lieutenant Matiur Rahman Stadium, Chattogram',
 'Kerrydale Oval',
 'Himachal Pradesh Cricket Association Stadium',
 'Gaddafi Stadium, Lahore',
 'MA Chidambaram Stadium, Chepauk',
 'Central Broward Regional Park Stadium Turf Ground',
 'Sophia Gardens',
 'Guanggong International Cricket Stadium',
 'Arnos Vale Ground, Kingstown, St Vincent',
 'Greenfield International Stadium, Thiruvananthapuram',
 'Adelaide Oval',
 'Brisbane Cricket Ground, Woolloongabba',
 'AMI Stadium',
 'R Premadasa Stadium, Colombo',
 'Riverside Ground',
 "National Cricket Stadium, St George's, Grenada"]
st.title("cricket score predicator")
col1,col2=st.columns(2)
with col1:
  batting_team=st.selectbox('select batting team',sorted(teams))
with col2:
  bowling_team=st.selectbox('select bowling team',sorted(teams))
venue=st.selectbox("select city",sorted(venue))  
col3,col4,col5=st.columns(3)
with col3:
  current_score=st.number_input("current score")
with col4:
  overs=st.number_input("overs done")  
with col5:
  wickets=st.number_input("wickets")
last_five=st.number_input("run scored in last five overs")
if st.button('Predict Score'):
    balls_left = 120 - (overs*6)
    wickets_left = 10 -wickets
    current_rr = current_score/overs

    input_df = pd.DataFrame(
     {'batting_team': [batting_team], 'bowling_team': [bowling_team],'venue':venue, 'current_score': [current_score],'balls_left': [balls_left], 'wickets_left': [wickets], 'current_rr': [current_rr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
    st.write(f"Predicted Score Range: {int(result[0]-8)} - {int(result[0]+8)}")

