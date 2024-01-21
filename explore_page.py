import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 

def shorten_categories(categories, cutoff):
    """
    discard the data whose category has fewer than <cutoff> number of data
    """
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x == 'More than 50 years':
        return 50.0
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Post grad'
    return 'Less than Bechelors'


def clean_employment(x):
    if 'Employed' in x:
        return 'Employed'
    if 'Independent' in x:
        return 'Independent'
    return 'Other'


@st.cache_data
def load_data():
  df = pd.read_csv("survey_results_public_file2.csv")
  df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
  df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
  df = df.dropna()
  
  country_map = shorten_categories(df.Country.value_counts(), 400)
  df['Country'] = df['Country'].map(country_map)

  df = df[df['Salary'] <= 250000]
  df = df[df['Salary'] >= 5000]
  df = df[df['Country'] != 'Other']

  df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
  df['EdLevel'] = df['EdLevel'].apply(clean_education)
  df['Employment'] = df['Employment'].apply(clean_employment)
  return df

df = load_data()

def show_explore_page():
  st.title("Explore Software Engineer Salaries")
  st.write(
    """
  ### Stack Overflow Developer Survey 2023
  """
  )
  

  # writing bar chart for mean salary

  st.write(
      """
  ### Mean Salary Based On Country
  """
  )

  data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
  st.bar_chart(data)


  # writing line chart
  st.write(
      """
  ### Mean Salary Based On Experience (Years)
  """
  )
  data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
  st.line_chart(data)
  

  # writing pie chart
  
  data = df["Country"].value_counts()

  fig1, ax1 = plt.subplots()
  # ax1.pie(data, labels=data.index, autopct='%1.0f%%', shadow=True, startangle=90, pctdistance=1.0)
  ax1.pie(data, labels=data.index, autopct='%.1f%%', shadow=False, startangle=90, pctdistance=0.9)
  ax1.axis("equal") # Equal aspect ratio ensures that pie is drawn as a circle

  st.write("""#### Number of Data from different countries""")
  st.pyplot(fig1)

