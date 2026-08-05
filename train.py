import os
import tensorflow as tf
from tensorflow.keras import layers, models

# =========================
# Load Datasets
# =========================

train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/train",
    image_size=(128, 128),
    batch_size=32
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/validation",
    image_size=(128, 128),
    batch_size=32
)

test_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/test",
    image_size=(128, 128),
    batch_size=32
)

# =========================
# Build CNN Model
# =========================

model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(128, 128, 3)),

    layers.Conv2D(16, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(128, activation="relu"),

    layers.Dense(1, activation="sigmoid")
])

# =========================
# Compile Model
# =========================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Show model architecture
model.summary()

# =========================
# Train Model
# =========================

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=5
)

# =========================
# Evaluate Model
# =========================

test_loss, test_accuracy = model.evaluate(test_dataset)

print(f"\nTest Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# =========================
# Save Model
# =========================

os.makedirs("models", exist_ok=True)

model.save("models/cat_dog_classifier.keras")

print("\n✅ Model saved successfully!")