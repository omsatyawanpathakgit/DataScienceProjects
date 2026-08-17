
---

## 4. Face Mask Detection (CNN Project)

```markdown
# Face Mask Detection using CNN

## Project Overview
A deep learning project that uses Convolutional Neural Networks (CNN) to detect whether a person is wearing a face mask or not. This system can be deployed at public places, offices, and educational institutions for COVID-19 safety compliance.

## Problem Statement
Build an image classification model that accurately determines whether a person in an image is wearing a face mask, to support public health and safety measures.

## Dataset
- **Source**: Kaggle Face Mask Dataset
- **Distribution**:
  - With Mask: 3,725 images
  - Without Mask: 3,828 images
  - **Total**: 7,553 images

## Methodology

### Image Preprocessing
1. Resize images to 128×128 pixels
2. Convert to RGB format
3. Convert to numpy arrays
4. Normalize pixel values (divide by 255)
5. Split into training (80%) and testing (20%)

### CNN Architecture


## Results

### Training Performance
| Epoch | Train Accuracy | Train Loss | Val Accuracy | Val Loss |
|-------|---------------|------------|--------------|----------|
| 1 | 79.01% | 0.4720 | 90.08% | 0.2265 |
| 3 | 90.68% | 0.2310 | 93.72% | 0.1732 |
| 5 | 93.43% | 0.1749 | 93.88% | 0.1354 |

### Final Test Accuracy
**92.26%**

### Sample Predictions
| Image | Prediction | Correct? |
|-------|------------|----------|
| Person with Mask | Wearing Mask | ✅ |
| Person without Mask | Not Wearing Mask | ✅ |
| Person without Mask (3rd image) | Not Wearing Mask | ✅ |

## Training Details
- **Epochs**: 5
- **Backpropagation iterations**: 850 times (170 steps × 5 epochs)
- **Optimizer**: Adam
- **Loss Function**: Sparse Categorical Crossentropy
- **Validation Split**: 10%

## Technologies Used
- Python 3.x
- TensorFlow / Keras
- OpenCV
- PIL (Pillow)
- NumPy, Matplotlib
- KaggleHub

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/yourusername/face-mask-detection.git

# Install dependencies
pip install -r requirements.txt

# Download dataset (automatically via kagglehub)
# Run the notebook
jupyter notebook FaceMaskDetectionProject.ipynb
