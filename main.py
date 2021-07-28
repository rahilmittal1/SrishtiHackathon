from keras.models import Model
import streamlit as st
import pickle


  

st.write('# AUTO FOOD RECOMMENDATION SYSTEM')

@st.cache() 
def load_model():    
    # load the recommender model
    return 'C:/Users/Owner/Desktop/code/Hackathon final food rec ML/model.py'

model = load_model()

meal_size = st.sidebar.selectbox(
    'Select size of meal',
    ('small', 'medium', 'large')
)

time = st.sidebar.selectbox(
    'Select time of the day you want to eat the meal',
    ('morning', 'afternoon', 'evening')
)

preference = st.sidebar.selectbox(
    'Select preference',
    ('veg', 'nonveg')
)



clicked = st.button('recommend food')

if clicked:
  st.write('RECOMMENDED FOOD:' + model.output)
