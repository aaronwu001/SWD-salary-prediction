import streamlit as st
import pickle
import numpy as np 

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


def load_model():
  with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
  return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']
le_employment = data['le_employment']

def show_predict_page():
  st.title('Software Developer Salary Prediction')
  st.write("""### We need some information to predict the salary.""")
  
  countries = {"United States of America",
              "Germany",
              "United Kingdom of Great Britain and Northern Ireland",
              "Canada", 
              "India",
              "France", 
              "Netherlands",
              "Poland", 
              "Brazil",
              "Australia", 
              "Spain",
              "Sweden", 
              "Italy",
              "Switzerland",
              "Austria",
              "Denmark",
              "Czech Republic",
              "Norway",
              "Portugal",
              "Israel",
              "Belgium",
              "Finland",
              "Ukraine", 
              "New Zealand", 
              "Romania"
              }

  education = {
    'Bachelor’s degree', 
    'Less than Bechelors', 
    'Master’s degree',
    'Post grad'
  }

  employment = {
    'Employed', 
    'Independent', 
    'Other'
  }

  country = st.selectbox("Country", countries)
  education = st.selectbox("Education Level", education)
  experience = st.slider("Years of Experience", 0, 50, 3)
  employment = st.selectbox("Employment Status", employment)

  calculation_requested = st.button("Calculate Now")
  
  if calculation_requested:
    X = np.array([[country, education, experience, employment]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X[:, 3] = le_employment.transform(X[:,3])

    salary = regressor.predict(X)
    st.subheader(f"The estimated salary is USD${salary[0]:.2f}")
    

