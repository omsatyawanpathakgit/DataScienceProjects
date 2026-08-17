
---

## 7. Credit Card Fraud Detection

```markdown
# Credit Card Fraud Detection

## Project Overview
A machine learning project that detects fraudulent credit card transactions using classification models. The project addresses the challenge of highly imbalanced data and implements multiple algorithms to achieve reliable fraud detection.

## Problem Statement
Credit card fraud is a major issue in the banking sector. Build classification models that can predict whether a transaction is fraudulent (1) or normal (0) to help financial institutions identify suspicious activity and reduce losses.

## Dataset
- **Source**: Credit Card Fraud Detection dataset
- **Records**: 284,807 transactions
- **Features**: 31 columns (Time, V1-V28, Amount, Class)
- **Class Distribution**:
  - Normal (0): 284,315 (99.83%)
  - Fraud (1): 492 (0.17%)
- **Note**: Highly imbalanced dataset

### Important Columns
- **Time**: Seconds elapsed between transaction and first transaction
- **Amount**: Transaction amount
- **V1-V28**: Anonymized PCA-transformed features
- **Class**: Target variable (0 = Normal, 1 = Fraud)

## Methodology

### Data Preprocessing
- No missing values
- No feature scaling required (PCA features already scaled)
- Duplicate values removed
- Handled class imbalance using SMOTE

### SMOTE (Synthetic Minority Over-sampling Technique)
- Applied to handle severe class imbalance
- Creates synthetic fraud samples to balance dataset
- Integrated into pipeline using imblearn

### Models Tested

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| **Random Forest** | **99.85%** | **55%** | **90%** | **69%** |
| Naive Bayes | 97.64% | 6% | 90% | 12% |
| Logistic Regression | 97.37% | 6% | 95% | 11% |

### Cross-Validation Results (5-Fold)

| Metric | Logistic Regression | Naive Bayes | Random Forest |
|--------|---------------------|-------------|---------------|
| Accuracy | 97.48% | 97.59% | **99.87%** |
| Precision | 5.93% | 5.88% | **58.25%** |
| Recall | 91.25% | 85.98% | **84.76%** |
| F1 Score | 11.14% | 11.00% | **69.01%** |

## Why Random Forest Performs Best
- Handles complex and non-linear relationships
- Works well with imbalanced datasets
- Reduces overfitting compared to single decision tree
- Provides high accuracy in real-world problems
- Minimal data preprocessing required

## Confusion Matrix (Random Forest):
- **True Negatives**: 5,686 (correctly predicted normal)
- **False Positives**: 0 (no false alarms)
- **True Positives**: 88 (correctly detected fraud)
- **False Negatives**: 10 (missed frauds)

## Technologies Used
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib, Seaborn
- Joblib (model export)
