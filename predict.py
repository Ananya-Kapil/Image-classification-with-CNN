import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

# Load the trained model
model = keras.models.load_model("models/cat_dog_classifier.keras")

# Ask user for image path
image_path = input("Enter image path: ")

# Open image
img = Image.open(image_path).convert("RGB")
img = img.resize((128, 128))

# Convert image to array
img_array = np.array(img)
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array, verbose=0)[0][0]

# Print result
if prediction > 0.5:
    print(f"\n🐶 Dog ({prediction*100:.2f}% confidence)")
else:
    print(f"\n🐱 Cat ({(1-prediction)*100:.2f}% confidence)")