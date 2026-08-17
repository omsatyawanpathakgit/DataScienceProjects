
---

## 5. Laptop Price Predictor

```markdown
# Laptop Price Predictor

## Project Overview
A comprehensive machine learning project that predicts laptop prices based on various specifications and features. The project includes extensive Exploratory Data Analysis (EDA), feature engineering, and multiple regression models to find the best predictor.

## Problem Statement
Build a regression model that accurately predicts the price of a laptop based on its specifications including company, type, screen size, RAM, storage, GPU, operating system, and other features.

## Dataset
- **Source**: Laptop pricing dataset
- **Records**: 1,303 laptops
- **Features**: 12 columns (after cleaning and feature engineering)

### Original Features
- Company, TypeName, Inches, ScreenResolution, CPU, RAM, Memory, GPU, OpSys, Weight, Price

## Feature Engineering

### New Features Created
1. **Touchscreen** (Binary): Extracted from ScreenResolution
2. **IPS** (Binary): Extracted from ScreenResolution
3. **X_res, Y_res** (Integer): Screen resolution dimensions
4. **PPI** (Float): Pixels Per Inch = √(X_res² + Y_res²) / Inches
5. **CPU Brand** (Categorical): Extracted from CPU column
6. **GPU Brand** (Categorical): Extracted from GPU column
7. **OS Category** (Categorical): Simplified OS categories
8. **HDD, SSD, Hybrid, Flash_Storage** (Integer): Storage type capacities

## Exploratory Data Analysis

### Key Insights
- **Most Sold RAM**: 8GB
- **Most Common Company**: HP (approx. 200 laptops)
- **Most Popular OS**: Windows 10 (1,072 laptops)
- **Touchscreen Laptops**: Only 192 out of 1,303 (14.7%)
- **Correlation with Price**:
  - RAM: 0.743 (strong positive)
  - SSD: 0.671 (strong positive)
  - PPI: 0.475 (moderate positive)

## Model Development

### Models Tested
| Model | R² Score | MAE |
|-------|----------|-----|
| **Voting Regressor** | **0.8909** | **0.1574** |
| Random Forest | 0.8873 | 0.1586 |
| Extra Trees | 0.8851 | 0.1615 |
| Gradient Boost | 0.8827 | 0.1596 |
| XGBoost | 0.8771 | 0.1626 |
| Ridge Regression | 0.8127 | 0.2093 |
| Linear Regression | 0.8073 | 0.2102 |
| Decision Tree | 0.8411 | 0.1821 |
| SVR | 0.8083 | 0.2024 |

### Best Model: Voting Regressor
- **Base Estimators**: Random Forest, Gradient Boosting, XGBoost, Extra Trees
- **Weights**: [5, 1, 1, 1]
- **Ensemble Method**: Voting (weighted average)

## Technologies Used
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn
- Pickle (for model export)
