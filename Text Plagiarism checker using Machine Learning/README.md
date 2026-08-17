
---

## 2. Content Plagiarism Detection (NLP Project)

```markdown
# Content Plagiarism Detection

## Project Overview
A Natural Language Processing (NLP) project that detects plagiarism by comparing source text and plagiarized text. Using machine learning with TF-IDF vectorization, this system can identify whether a given text is plagiarized or original.

## Problem Statement
Build a classification model that determines whether a text passage is plagiarized by analyzing text similarity patterns between source and plagiarized content.

## Dataset
- **Source**: Custom dataset with paired text samples
- **Records**: 370 text pairs (187 original, 183 plagiarized)
- **Features**: Source text, Plagiarized text, Label (0=Original, 1=Plagiarized)

## Methodology

### Text Preprocessing
1. Remove punctuation marks
2. Convert to lowercase
3. Remove stop words

### Feature Engineering
- Combined source_text and plagiarized_text
- Applied TF-IDF vectorization
- Used machine learning pipelines

### Models Tested
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Random Forest
- Extra Trees
- AdaBoost
- XGBoost

## Results

### Model Performance Comparison

| Model | CV Accuracy | CV F1 Score |
|-------|-------------|-------------|
| Logistic Regression | **88.50%** | **88.48%** |
| AdaBoost | 83.45% | 83.13% |
| KNN | 81.76% | 81.56% |
| Random Forest | 81.09% | 80.30% |
| Extra Trees | 79.73% | 79.21% |
| XGBoost | 67.22% | 63.24% |

### Best Model Performance (Logistic Regression)
- **Accuracy**: 89.19%
- **Precision**: 89.19%
- **Recall**: 89.19%
- **F1 Score**: 89.19%

### Confusion Matrix
