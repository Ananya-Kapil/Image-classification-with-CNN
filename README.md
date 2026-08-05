# 🐱🐶 Cat vs Dog Image Classifier

A Convolutional Neural Network (CNN) built using TensorFlow/Keras to classify images of cats and dogs.

## Features

- Image preprocessing
- CNN built from scratch
- Model training
- Accuracy evaluation
- Confusion Matrix
- CLI image prediction

## Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Pillow
- Scikit-learn

## Dataset

Custom Cats vs Dogs dataset

Folder Structure:

dataset/
├── train/
│ ├── cats/
│ └── dogs/
├── validation/
│ ├── cats/
│ └── dogs/
└── test/
├── cats/
└── dogs/

## Model Architecture

- Rescaling
- Conv2D (16 filters)
- MaxPooling
- Conv2D (32 filters)
- MaxPooling
- Flatten
- Dense (128)
- Output (Sigmoid)

## Results

Training Accuracy: **~91%**

Validation Accuracy: **~79%**

## How to Run

Train the model

```bash
python train.py
```

Predict an image

```bash
python predict.py
```

## Future Improvements

- Data Augmentation
- Transfer Learning (MobileNetV2)
- Streamlit Web App
- REST API using FastAPI
- LLM-powered explanation pipeline
- Docker Deployment

## Author

Ananya