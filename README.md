# 🐱🐶 Cat vs Dog Image Classifier

A deep learning image classification system built using **TensorFlow** and **Keras** that classifies images as **Cats** or **Dogs** using a Convolutional Neural Network (CNN). The project supports model training, evaluation, and prediction on custom images through a simple command-line interface.

---

## 🚀 Features

- 🧠 CNN built from scratch using TensorFlow/Keras
- 📂 Image preprocessing and normalization
- 🎯 Binary classification (Cat vs Dog)
- 💾 Save and load trained model
- 🔍 Predict custom images from the terminal
- 📈 Evaluate model accuracy
- 📊 Confusion Matrix & Classification Report
- 🖥️ Simple CLI interface

---

# 📸 Screenshots

![Cat Prediction](screenshots/cat_prediction.png)

![Dog Prediction](screenshots/dog_prediction.png)
---

---

## 🛠️ Tech Stack

- Python 3.12
- TensorFlow
- Keras
- NumPy
- Pillow
- Matplotlib
- Scikit-learn

---

## 📂 Project Structure

```text
cat-dog-classifier/
│
├── dataset/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── models/
│   └── cat_dog_classifier.keras
│
├── screenshots/
│   ├── project-structure.png
│   ├── training.png
│   ├── cat-prediction.png
│   ├── dog-prediction.png
│   └── evaluation.png
│
├── train.py
├── predict.py
├── evaluate.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 CNN Architecture

- Rescaling Layer
- Conv2D (16 Filters, ReLU)
- MaxPooling2D
- Conv2D (32 Filters, ReLU)
- MaxPooling2D
- Flatten
- Dense (128, ReLU)
- Output Layer (Sigmoid)

---

## 📊 Model Performance

| Metric | Score |
|---------|------:|
| Training Accuracy | ~85% |
| Validation Accuracy | ~79% |

> Results may vary slightly after retraining.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/cat-dog-classifier.git

cd cat-dog-classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📥 Dataset

The dataset is **not included** in this repository because of GitHub file size limits.

Expected folder structure:

```text
dataset/
├── train/
│   ├── cats/
│   └── dogs/
├── validation/
│   ├── cats/
│   └── dogs/
└── test/
    ├── cats/
    └── dogs/
```

---

## 🚀 Train the Model

```bash
python train.py
```

The trained model will be saved as:

```text
models/cat_dog_classifier.keras
```

---

## 🔍 Predict a Custom Image

Run:

```bash
python predict.py
```

Example:

```text
Enter image path:
dataset/test/dogs/dog_test_00008.jpg

Prediction: Dog
Confidence: 98.74%
```

---

## 📈 Evaluate the Model

Run:

```bash
python evaluate.py
```

Outputs include:

- Test Accuracy
- Confusion Matrix
- Classification Report

---

## 📦 Requirements

Install all required packages:

```bash
pip install -r requirements.txt
```

---

## 🎓 Concepts Demonstrated

- Deep Learning
- Convolutional Neural Networks (CNN)
- Image Classification
- Image Preprocessing
- TensorFlow/Keras
- Model Evaluation
- Binary Classification
- Saving & Loading Models
- Command Line Interface (CLI)

---

## 🚀 Future Improvements

- Transfer Learning (MobileNetV2 / ResNet50)
- Flask / FastAPI Web API
- Streamlit Web Application
- Docker Deployment
- Grad-CAM Explainability
- Hugging Face Deployment
- LLM-powered image explanation pipeline

---

## 👨‍💻 Author

**Ananya**

Built as part of my Machine Learning & Deep Learning portfolio to demonstrate end-to-end image classification using CNNs.

---

## ⭐ If you found this project useful

Feel free to **star ⭐ the repository** and share your feedback!
