
---

## 3. Fire vs No Fire Detection (CNN Project)

```markdown
# Fire vs No Fire Detection using CNN

## Project Overview
A deep learning project that uses Convolutional Neural Networks (CNN) to detect whether an image contains fire. This can be used for early fire detection in surveillance systems, forest monitoring, and safety applications.

## Problem Statement
Build an image classification model that accurately identifies whether a given image contains fire or not, to help in early fire detection and prevention.

## Dataset
- **Source**: Kaggle Fire Dataset
- **Distribution**:
  - With Fire: 755 images
  - Without Fire: 244 images
  - **Total**: 999 images
- **Note**: Dataset is imbalanced (handled using class weights)

## Methodology

### Image Preprocessing
1. Resize images to 128×128 pixels
2. Convert to RGB format
3. Convert to numpy arrays
4. Normalize pixel values (divide by 255)

### CNN Architecture


### Handling Imbalanced Data
- Used `compute_class_weight()` with 'balanced' strategy
- Applied class weights during model training

## Results

### Training Performance
| Epoch | Train Accuracy | Train Loss | Val Accuracy | Val Loss |
|-------|---------------|------------|--------------|----------|
| 1 | 77.19% | 0.4876 | 95.00% | 0.1187 |
| 5 | 93.32% | 0.1620 | 97.50% | 0.0740 |
| 10 | 97.50% | 0.0810 | 96.25% | 0.1570 |

### Final Test Accuracy
**95.50%**

### Sample Predictions
| Image | Prediction | Correct? |
|-------|------------|----------|
| Fire Image | Fire (99.99%) | Yes |
| Snowy Road | Fire | No (False Positive) |
| Children in Park | No Fire | Yes |
| Rooftop Garden | No Fire | Yes |

## Technologies Used
- Python 3.x
- TensorFlow / Keras
- OpenCV
- PIL (Pillow)
- NumPy, Matplotlib
- KaggleHub
