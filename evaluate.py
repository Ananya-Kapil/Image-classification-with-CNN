import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

# Load trained model
model = keras.models.load_model("models/cat_dog_classifier.keras")

# Load test dataset
test_ds = tf.keras.utils.image_dataset_from_directory(
    "dataset/test",
    image_size=(128, 128),
    batch_size=32,
    shuffle=False
)

class_names = test_ds.class_names
print("Classes:", class_names)

y_true = []
y_pred = []

for images, labels in test_ds:
    predictions = model.predict(images, verbose=0)

    predictions = (predictions > 0.5).astype(int).flatten()

    y_true.extend(labels.numpy())
    y_pred.extend(predictions)

# Print report
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, target_names=class_names))

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=class_names
)

disp.plot(cmap="Blues")

plt.title("Confusion Matrix")
plt.show()