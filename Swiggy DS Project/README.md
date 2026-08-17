# Swiggy Business Insights & Delivery Time Prediction

## Project Overview
This project analyzes Swiggy's restaurant data to derive business insights and build machine learning models for predicting delivery times and classifying restaurant segments. The analysis combines statistical hypothesis testing with predictive modeling to help Swiggy optimize its operations.

## Problem Statements
1. **Hypothesis Testing Questions**:
   - Is average delivery time significantly different from 45 minutes?
   - Do Indian and Chinese restaurants have different delivery times?
   - Are average customer ratings significantly different from 4.0?
   - Do Indian and Chinese restaurants have different ratings?
   - Do delivery times differ among Indian, Chinese, and Fast Food restaurants?
   - Is restaurant cuisine type associated with the city?

2. **Machine Learning Questions**:
   - Predict delivery time using restaurant features
   - Classify restaurants as fast/slow delivery
   - Classify restaurants as Premium/Budget segment

## Dataset
- **Source**: Swiggy restaurant data
- **Records**: 8,680 restaurants
- **Features**: Area, City, Restaurant name, Price, Ratings, Total ratings, Food type, Address, Delivery time

## Key Findings

### Hypothesis Testing Results
-  Average delivery time is **significantly different** from 45 minutes
-  No significant difference between Indian and Chinese restaurant delivery times
-  Average customer rating is **significantly different** from 4.0
-  Indian and Chinese restaurants have **significantly different** ratings
-  At least one cuisine type has **significantly different** delivery time
-  Food type is **significantly associated** with city

### Model Performance

**Delivery Time Prediction (Regression)**:
- **Best Model**: XGBoost
- **R² Score**: 0.675
- **MAE**: 6.41 minutes
- **RMSE**: 8.24 minutes

**Price Segment Classification**:
- **Best Model**: Logistic Regression
- **Accuracy**: 88.95%
- **Precision**: 61.22%
- **Recall**: 14.78%
- **F1 Score**: 23.81%

**Key Insights**:
- Expensive restaurants tend to deliver faster
- Higher-rated restaurants deliver faster
- Low-rated restaurants tend to deliver slower

## Technologies Used
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Statsmodels
- Matplotlib, Seaborn
