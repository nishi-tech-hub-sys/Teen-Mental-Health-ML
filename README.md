# Teen Mental Health Prediction using Machine Learning

## Overview
This project is based on predicting the mental health condition of teenagers using machine learning techniques. The main aim is to understand how different factors like stress, sleep, and lifestyle affect mental health.

## Dataset
- Source: Kaggle  
- The dataset contains information about teenagers such as their habits, stress level, sleep patterns, etc.  
- It has more than 500 records and multiple features.

## Problem Type
This is a **supervised learning (classification)** problem because the dataset contains a target variable which we are trying to predict.

## Model Used
I have used:
- Random Forest Classifier (main model)

Also tried:
- Decision Tree (for comparison)

Random Forest gave better accuracy and more stable results.

## Steps Performed
- Data cleaning (removed missing values)
- Encoding categorical data
- Feature scaling
- Train-test split
- Model training
- Cross-validation
- Evaluation using different metrics

## Evaluation Metrics
The model was evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Results
The model performed well on the dataset with good accuracy and balanced precision-recall values. Cross-validation scores were also consistent, which shows the model generalizes well.

## Tools & Technologies
- Python
- Scikit-learn
- Pandas, NumPy
- Matplotlib, Seaborn
- Google Colab

## How to Run
1. Open the notebook in Google Colab  
2. Upload the dataset file  
3. Run all the cells step by step  

## Conclusion
This project helped me understand the complete machine learning pipeline including preprocessing, model training, evaluation, and performance analysis.
