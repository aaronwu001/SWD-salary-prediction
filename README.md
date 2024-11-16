# SWD Salary Prediction

This project predicts the salary of software developers based on various factors, such as education level, years of experience, employment status, and country of residence. The model is built using machine learning algorithms and a dataset from the Stack Overflow Developer Survey.

The application is built using **Streamlit** for an interactive user interface and leverages multiple regression models, including **Linear Regression**, **Decision Tree**, and **Random Forest**, to predict the salary.

---

## 🚀 Project Overview

The main goal of this project is to create a tool that predicts software developer salaries based on personal attributes. It provides both an exploration interface for visualizing salary distributions and a prediction interface for estimating salaries based on user input.

---

## 🛠 Features

### **Core Functionalities**
1. **Explore Salaries**:
   - View visualizations of average salaries based on various attributes, including country and years of experience.
   - Interactive charts, such as bar charts, line charts, and pie charts, to explore salary trends.
   
2. **Salary Prediction**:
   - Predict the salary of a software developer by providing input values for country, education level, years of experience, and employment status.
   - The prediction model is based on several machine learning models, including **Linear Regression**, **Decision Tree**, and **Random Forest**.

---

## 🛠 Tech Stack

- **Backend**:
  - Python 3.12
  - **Streamlit** for the frontend UI.
  - **scikit-learn** for building machine learning models.
  - **pandas** for data manipulation.
  - **matplotlib** for data visualization.

- **Machine Learning Models**:
  - **Linear Regression**
  - **Decision Tree Regressor**
  - **Random Forest Regressor**

---

## Installation Steps 

Clone the repo:
```bash
git clone https://github.com/aaronwu001/SWD-salary-prediction.git
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the app:
```bash
streamlit run application.py
```

View the app:
Access it on http://localhost:8501.

## 🌟 What the Project Does

1. **Data Preprocessing**:
   - The dataset is cleaned, and categorical features like country, education level, and employment status are encoded.
   - Outliers and invalid data points (like extremely high salaries) are filtered.

2. **Model Training**:
   - The project uses multiple machine learning models to predict the salary based on input features:
     - **Linear Regression**: A simple regression model.
     - **Decision Tree**: A more complex, non-linear model.
     - **Random Forest**: An ensemble model built on decision trees.

3. **Prediction**:
   - After training the models, the user can input values for country, education, experience, and employment status to predict a salary.
   
4. **Exploration**:
   - Users can explore salary distributions based on country, education, and experience using various charts.

---

## 📊 Visualizations

### **Mean Salary Based On Country**:
A bar chart that shows the average salary for developers from different countries.

### **Mean Salary Based On Experience**:
A line chart displaying how salary increases with years of professional experience.

### **Country Distribution**:
A pie chart showing the distribution of developers based on the country.

---

## 📚 Lessons Learned

### Challenges:
- Handling categorical features and transforming them into numerical values.
- Ensuring accurate predictions by tuning models and dealing with overfitting.

### Lessons:
- **Data preprocessing** is crucial for machine learning tasks, especially when dealing with categorical variables.
- **Model evaluation** using metrics such as **mean squared error** is essential to understand model performance.

---

## 🔮 Future Improvements

1. **Model Enhancement**:
   - Use hyperparameter tuning (GridSearchCV) for optimizing the models.
   - Experiment with other machine learning models such as **XGBoost** or **SVR**.

2. **User Interface**:
   - Improve the UI by adding more interactive elements and visualizations for better user experience.

3. **Expanded Data**:
   - Integrate additional features such as job role, company size, and geographic location within the country for more detailed predictions.

---

## 🛠 Acknowledgments

- This project was inspired by the **Stack Overflow Developer Survey** dataset.
- **Streamlit** for creating the interactive application.
- **scikit-learn** for providing a powerful library for machine learning models.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 🌐 Additional Resources

- **Streamlit Documentation**: [Streamlit Docs](https://docs.streamlit.io/)
- **scikit-learn Documentation**: [scikit-learn Docs](https://scikit-learn.org/)
- **Matplotlib Documentation**: [Matplotlib Docs](https://matplotlib.org/)
- **pandas Documentation**: [pandas Docs](https://pandas.pydata.org/)
