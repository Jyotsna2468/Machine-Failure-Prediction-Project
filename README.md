# Machine-Failure-Prediction-Project
# ⚙️ Machine Failure Prediction Using Machine Learning

## 📌 Project Overview

Machine Failure Prediction is a Machine Learning classification project that predicts whether a machine is likely to fail based on its operating conditions and sensor-related data.

The project focuses on analyzing machine data, preprocessing features, training classification models, evaluating model performance, and deploying the final model through an interactive Streamlit web application.

## 🚀 Live Deployment

Try the deployed application here:

🔗 **[Machine Failure Prediction – Live Streamlit App](https://machine-failure-prediction-project-eex5xvjtwbmsbdvdthkjvm.streamlit.app/)**

## 🎯 Project Objectives

- Predict machine failure using Machine Learning.
- Analyze machine operating conditions and sensor data.
- Clean and preprocess the dataset.
- Perform Exploratory Data Analysis (EDA).
- Train and evaluate classification models.
- Identify patterns associated with machine failures.
- Deploy the trained model using Streamlit.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and cleaning
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Seaborn** – Exploratory data analysis
- **Scikit-learn** – Machine Learning algorithms and evaluation
- **Streamlit** – Web application and deployment
- **Joblib** – Saving and loading trained models

## 🔄 Project Workflow

### Step 1: Data Gathering
Collected the machine failure dataset containing machine operating measurements, sensor readings, and the target variable indicating whether a machine failure occurred.

### Step 2: Data Understanding
- Checked the number of rows and columns using `df.shape`.
- Inspected column names and data types.
- Viewed sample records using `df.head()`.
- Identified the target variable and input features.

### Step 3: Data Cleaning
- Checked for missing values.
- Handled missing values using suitable techniques.
- Checked for duplicate records.
- Corrected data types where necessary.
- Verified the dataset before further processing.

### Step 4: Exploratory Data Analysis (EDA)
- Analyzed the distribution of machine failures.
- Examined the relationship between input features and machine failure.
- Identified patterns and potential outliers.
- Used visualizations to understand the data.

### Step 5: Data Preprocessing
- Separated independent variables (`X`) and the target variable (`y`).
- Selected relevant features for prediction.
- Encoded categorical features if present.
- Scaled numerical features when required by the selected model.
- Prepared the dataset for Machine Learning.

### Step 6: Train-Test Split
Split the dataset into training and testing sets to train the model and evaluate its ability to predict failures on unseen data.

### Step 7: Model Building
Trained classification algorithms to predict whether a machine would fail.

The project uses a Gradient Boosting model as the prediction model, subject to the final model selected during experimentation.

### Step 8: Model Evaluation
Evaluated the model using suitable classification metrics, such as:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics help assess how effectively the model identifies machine failures and avoids incorrect predictions.

### Step 9: Model Saving
Saved the trained model and required preprocessing object using Joblib so that the application can load them for predictions.

Example model files:

- `gradient_boosting_model.joblib`
- `preprocessor.joblib`

### Step 10: Streamlit Application Development
Developed an interactive Streamlit application that accepts machine operating values as input and displays the predicted machine failure status.

### Step 11: GitHub Repository Setup
Uploaded the application code, dependency file, trained model, and preprocessing files to GitHub so that the deployment platform can access the required project files.

### Step 12: Model Deployment
Deployed the Streamlit application online, allowing users to access the Machine Failure Prediction system through a web browser.

🌐 **Live Application:** [Machine Failure Prediction](https://machine-failure-prediction-project-eex5xvjtwbmsbdvdthkjvm.streamlit.app/)

## ✨ Key Features

- Machine failure classification
- Data cleaning and preprocessing
- Exploratory data analysis
- Gradient Boosting-based prediction
- Interactive Streamlit interface
- Saved model and preprocessing pipeline
- Online deployment

## 📂 Project Structure

```text
Machine-Failure-Prediction/
│
├── app.py
├── requirements.txt
├── gradient_boosting_model.joblib
├── preprocessor.joblib
└── README.md
```

*The file names and structure above are examples. Keep the names consistent with your actual GitHub repository and the paths used in `app.py`.*

## 💻 How to Run the Project Locally

**1. Clone the repository**

```bash
git clone <your-github-repository-url>
```

**2. Navigate to the project folder**

```bash
cd Machine-Failure-Prediction
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run app.py
```

## 📚 Learning Outcomes

- Learned the end-to-end Machine Learning workflow.
- Practiced data cleaning and preprocessing.
- Performed exploratory data analysis.
- Developed a classification model.
- Evaluated model performance using classification metrics.
- Learned to save and load trained models using Joblib.
- Gained practical experience deploying a Machine Learning application with Streamlit.

## 👩‍💻 Author

**Jyotsna Shinde**

Project: Machine Failure Prediction Using Machine Learning

## 📝 Conclusion

This project demonstrates how Machine Learning can help identify potential machine failures from operating data. It covers the complete process, from data gathering and preprocessing to model training, evaluation, and deployment.

**Disclaimer:** This project is intended for educational and demonstration purposes. Predictions should be validated before being used in real industrial maintenance decisions.

