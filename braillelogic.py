import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

IMAGE_SIZE = (64, 64)
BRAILLE_IMAGE_FOLDER = "C:\\Users\\DELL\\PycharmProjects\\text-braille\\Data"  # Update the folder path


# Preprocessing function to resize and normalize images
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, IMAGE_SIZE)
    img_normalized = img_resized / 255.0
    return img_normalized


# Function to create a CNN model
def create_cnn_model(input_shape, num_classes):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


# Load and preprocess dataset
def load_data():
    train_data = "C:\\Users\\DELL\\PycharmProjects\\text-braille\\Data\\Train"  # Update with correct folder path
    data = []
    labels = []
    CLASSES = []

    for image_file in os.listdir(train_data):
        image_path = os.path.join(train_data, image_file)

        # Skip non-image files just in case
        if not image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        image = preprocess_image(image_path)
        data.append(image)

        # Extract label from filename (e.g., a.jpg → 'a')
        label = image_file[0].upper()
        if label not in CLASSES:
            CLASSES.append(label)
        labels.append(CLASSES.index(label))  # Convert to indices

    data = np.array(data).reshape(-1, 64, 64, 1)  # Add channel dimension
    labels = np.array(labels)
    labels = to_categorical(labels)
    return data, labels, CLASSES


# Function to map text to Braille images
def text_to_braille_images(text):
    braille_images = []
    for char in text:
        if char.isalpha():
            found = False
            for ext in ['.jpg', '.jpeg', '.png']:
                image_path = os.path.join(BRAILLE_IMAGE_FOLDER, f"{char.lower()}{ext}")
                if os.path.exists(image_path):
                    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                    braille_images.append((char.upper(), img))
                    found = True
                    break
            if not found:
                print(f"Braille image for '{char}' not found.")
    return braille_images


# Function to display Braille images side by side
def show_braille_translation(images):
    if not images:
        print("No Braille images to display.")
        return
    plt.figure(figsize=(2 * len(images), 3))
    for i, (char, img) in enumerate(images):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(f"'{char}'")
        plt.axis('off')
    plt.tight_layout()
    plt.show()


# Function to save Braille output as a single image
def save_braille_output_as_image(images, output_path="C:\\Users\\DELL\\PycharmProjects\\text-braille\\Data\\braille_output.jpg"):
    if not images:
        print("No images to save.")
        return
    try:
        # Concatenate Braille images horizontally
        braille_strip = np.hstack([img for _, img in images])
        cv2.imwrite(output_path, braille_strip)
        print(f"Braille output saved to {output_path}")
    except Exception as e:
        print(f"Error saving Braille output: {e}")


# Ask user for text input
def get_user_input():
    user_text = input("Enter text to convert to Braille (letters A-Z only): ")
    braille_output = text_to_braille_images(user_text)
    show_braille_translation(braille_output)
    save_braille_output_as_image(braille_output)


if __name__ == "__main__":
    get_user_input()
