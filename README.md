💊 Forecasting the Optimal Dosage of Antidepressants on Patients with MDD Undergoing Monotherapy Using Machine Learning and AI Techniques
This repository contains the predictive model and code for the research project: Forecasting the Optimal Dosage of Antidepressants on Patients with MDD Undergoing Monotherapy Using Machine Learning and AI Techniques, by Prisha Malik.

The project develops a machine learning model to predict the optimal dosage of a single antidepressant (monotherapy) for patients diagnosed with Major Depressive Disorder (MDD), based on their physical and mental characteristics.

Getting Started
This section outlines how to set up the environment, obtain the necessary data, and run the predictive model and Streamlit application.

Prerequisites
Python 3.x

Anaconda-Navigator (Recommended for environment management)

1. Installation
Clone the repository and install the required libraries:
# Clone the repository
git clone [repository_url]
cd [repository_name]

# Install required Python libraries
pip install pandas scikit-learn streamlit

That's a great adjustment for a practical GitHub repository! A focus on the code, data, and methodology is essential.

Here is the revised, code-centric README focusing on setup, methodology, and variables, while condensing the background and removing the bibliography/future research sections.

💊 Forecasting the Optimal Dosage of Antidepressants on Patients with MDD Undergoing Monotherapy Using Machine Learning and AI Techniques
This repository contains the predictive model and code for the research project: Forecasting the Optimal Dosage of Antidepressants on Patients with MDD Undergoing Monotherapy Using Machine Learning and AI Techniques, by Prisha Malik.

The project develops a machine learning model to predict the optimal dosage of a single antidepressant (monotherapy) for patients diagnosed with Major Depressive Disorder (MDD), based on their physical and mental characteristics.

Getting Started
This section outlines how to set up the environment, obtain the necessary data, and run the predictive model and Streamlit application.

Prerequisites
Python 3.x

Anaconda-Navigator (Recommended for environment management)

1. Installation
Clone the repository and install the required libraries:

Bash

# Clone the repository
git clone [repository_url]
cd [repository_name]

# Install required Python libraries
pip install pandas scikit-learn streamlit
2. Data Acquisition
The model is trained on the Medical Expenditure Panel Survey (MEPS) public dataset.

Source: MEPS (2010 to 2020)

Required Data Files:

Prescribed Medicines files

Full Year Population Characteristics files

Medical Conditions files

Note: The raw MEPS data files (often in ASCII format) must be downloaded individually for the years 2010 through 2020 and placed into a designated data/raw directory within this repository structure for the data pipeline script to run successfully.

3. Running the Application
Execute the Streamlit application to interact with the trained predictive model:
streamlit run app.py

The app provides a user interface where a patient's demographics can be input to receive a forecasted optimal dosage.

Model & Data Methodology
The research uses a structured pipeline to prepare the data and train a two-stage regression model.

Variables (Features & Target)
The model is trained to predict the dosage based on the following input features:

Category: 
- Target:
    - Feature: Dosage Amount (Numerical)
    - Description: The optimal dosage to be predicted.
- Physical:
    - Feature: Age, Sex, BMI
    - Description: Patient demographics.
 - Mental:
     - Feature: Co-occurring Mental Illnesses
     - Description: Binary presence/type of other diagnoses besides MDD.
- Medication:
    - Feature: Antidepressant Type
    - Description: The specific monotherapy drug used (e.g., SSRIs, SNRIs).

Data Pre-processing Pipeline
The data preparation is handled by a dedicated Python script (e.g., data_pipeline.py) using Pandas.

1. Merge: Combined all three data files across the years 2010-2020.

2. Filter (Monotherapy): Eliminated any subjects who used 2 or more antidepressants at a given time.

3. Feature Selection: Limited features to Age, Sex, BMI, Mental Illnesses, and Antidepressant Type.

4. Cleaning: Missing data was replaced using computed mean, median, or mode.

5. Encoding: Categorical data (Sex, Antidepressant Type, etc.) was converted to numerical format using One-Hot Encoding.

Predictive Model Training
 The model uses the scikit-learn library and follows a two-step process:

1.  Classification Model (Logistic Regression): Used initially to determine if a dosage is likely suboptimal/optimal (boolean output).

2. Regression Model (Linear Regression): Uses the output of the classification step and the patient features to predict the final numerical dosage amount.

The training set was 80% of the data while the testing set was 20%
Used a 10-fold Cross Validation 
For optimization: Trained with various feature combinations; halted when validation error increased to prevent overfitting.


