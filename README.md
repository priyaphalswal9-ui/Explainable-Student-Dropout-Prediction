#  Explainable Student Dropout Prediction using XGBoost & SHAP

### Early Behavioral Risk Detection in Online Learning using Machine Learning and Explainable AI

![Python](https://img.shields.io/badge/Python-3.13-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-green)
![SHAP](https://img.shields.io/badge/Explainable%20AI-SHAP-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

##  Project Overview

One of the main problems with online learning is that students are likely to drop out at a steady pace over time rather than all at once. Early identification enables schools to offer early assistance, and enhances student retention.

This project aims to create an end-to-end Machine Learning pipeline for predicting the drop-out of students based on Demographic, Academic, Registration, Assessment and interaction data in the Virtual Learning Environment (VLE) of students. In addition to prediction, the project incorporates Explainable AI (SHAP) to give educators a clear explanation of what led to each prediction, so they can better understand what is at play in determining whether a student is at risk of dropping out.

##  Problem Statement

It is difficult to detect students who are slowly dropping out of online courses and ultimately quitting. It is important to note that delayed identification reduces the window of opportunity for timely academic support and intervention.

This project develops an early student dropout prediction system using demographic information, assessment performance, registration details, and student learning behavior. The model integrates Explainable AI (SHAP) to explain why a student has been identified as being at risk, enabling educators to make informed intervention decisions.

##  Domain
- Education Technology (EdTech)
- Learning Analytics
- Machine Learning
- Explainable Artificial Intelligence (XAI)

##  Key Features

- End-to-end machine learning pipeline
- Multi-table feature engineering using the OULAD dataset
- Student behavioral analysis using Virtual Learning Environment (VLE) interaction data
- Comparison of multiple machine learning algorithms
- Hyperparameter tuning using GridSearchCV
- Explainable AI using SHAP
- Individual student prediction explanations
- Interactive Streamlit dashboard *(under development)*
- Support for early intervention strategies

##  Project Workflow

```text
Student Data
      │
Data Cleaning
      │
Feature Engineering
      │
Model Training
      │
Hyperparameter Tuning
      │
XGBoost Model
      │
SHAP Explainability
      │
Student Risk Prediction
      │
Streamlit Dashboard
```
##  Dataset

This project is built using the **Open University Learning Analytics Dataset (OULAD)**, a publicly available educational dataset containing information about student demographics, course registrations, assessments, and interactions with the Virtual Learning Environment (VLE).

### Dataset Components

| Dataset | Description |
|----------|-------------|
| studentInfo | Student demographic information and final results |
| studentRegistration | Registration and unregistration records |
| studentAssessment | Student assessment scores |
| assessments | Assessment details and weightage |
| studentVle | Student interaction logs with the VLE |
| vle | Metadata of learning resources |
| courses | Course and presentation information |

**Official Dataset:** Open University Learning Analytics Dataset (OULAD)
https://analyse.kmi.open.ac.uk/open_dataset

##  Feature Engineering

Instead of directly training the model on the raw OULAD tables, meaningful features were engineered by merging multiple relational datasets.

### Assessment Features

- Average assessment score
- Maximum score
- Minimum score
- Total assessments attempted
- Average assessment weight
- Total assessment weight
- Average submission day

### Student Engagement Features

- Total VLE clicks
- Average clicks
- Maximum clicks
- Active learning days
- Number of unique resources accessed
- First activity day
- Last activity day

### Activity-wise Engagement Features

The project also captures interaction with different learning resources, including:

- Homepage
- Course Content
- Forum
- Quiz
- Resource
- URL
- Wiki
- Page
- Questionnaire
- Folder
- Glossary
- Other VLE activities

These engineered features allow the model to learn both academic performance and behavioral engagement patterns.

##  Machine Learning Pipeline

The following machine learning workflow was implemented:

- Data Cleaning and Missing Value Handling
- Feature Engineering
- One-Hot Encoding
- Train-Test Split (80:20)
- Model Training
- Hyperparameter Tuning
- Cross Validation
- Model Evaluation
- Feature Importance Analysis
- Explainable AI using SHAP

##  Model Performance Comparison

Several machine learning algorithms were trained and evaluated to identify the most suitable model for student dropout prediction.

Since the primary objective of this project is **early identification of at-risk students**, **Recall** was considered the most important evaluation metric. Missing a student who is likely to drop out (False Negative) is more costly than incorrectly flagging a student who is not at risk (False Positive).

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|---------:|----------:|--------:|---------:|--------:|
| Logistic Regression | 86.34% | 76.33% | 81.27% | 78.73% | 94.06% |
| Decision Tree | 83.49% | 74.00% | 72.28% | 73.13% | 80.41% |
| Random Forest | 87.30% | 77.07% | 84.19% | 80.47% | 94.83% |
| XGBoost | 87.16% | 77.76% | 82.21% | 79.92% | 94.97% |
| **Tuned Random Forest** | 87.59% | 76.07% | 87.65% | 81.45% | 94.94% |
| **Tuned XGBoost**  | **86.90%** | **73.79%** | **89.72%** | **80.98%** | **94.58%** |

##  Final Model Selection

Although multiple models achieved competitive performance, the **Tuned XGBoost** model was selected as the final model.

### Why XGBoost?

- Highest Recall (**89.72%**)
- Excellent overall performance across all evaluation metrics
- Strong generalization after hyperparameter tuning
- Robust performance on engineered behavioral features
- Compatible with SHAP for model explainability

The model was selected based on the project objective of **identifying as many at-risk students as possible**, making Recall the deciding evaluation metric.

##  Explainable AI (SHAP)

To improve model transparency, SHAP (SHapley Additive exPlanations) was integrated with the final XGBoost model.

Unlike traditional feature importance, SHAP explains **why** a prediction was made by showing how each feature contributes to the prediction for an individual student.

### SHAP Analysis Included

- Global Feature Importance
- SHAP Beeswarm Plot
- SHAP Waterfall Plot
- SHAP Dependence Plot

The explainability analysis showed that student engagement, assessment performance, and learning behavior were among the strongest indicators of dropout risk.

##  Explainability Results

> Screenshots of SHAP visualizations will be added after deployment.

##  Business Impact

This project demonstrates how machine learning and Explainable AI can support educational institutions in improving student retention.

### Potential Applications

- Early identification of students at risk of dropping out.
- Support academic advisors with data-driven intervention strategies.
- Monitor student engagement throughout the course.
- Improve resource allocation by focusing support on high-risk students.
- Increase transparency in machine learning predictions using SHAP explanations.

By combining predictive analytics with Explainable AI, the system helps educators make informed decisions rather than relying solely on prediction scores.

##  Future Work

- Develop an interactive Streamlit dashboard for real-time predictions.
- Provide personalized intervention recommendations based on SHAP explanations.
- Save the complete preprocessing pipeline for deployment.
- Integrate live educational datasets.
- Extend the model to support multi-class academic risk prediction.
- Deploy the application on Streamlit Cloud for public access.

##  Live Demo

**Streamlit Application:**  
https://explainable-student-dropout-prediction-lq2i6rbbgwcx4ncb5xgpfb.streamlit.app/