import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image


# Laad het model en de labels
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("keras_model.h5")
    return model


@st.cache_resource
def load_labels():
    with open("labels.txt", "r") as f:
        labels = [line.strip() for line in f.readlines()]
    return labels


model = load_model()
labels = load_labels()

st.title("Webcam Image Classifier")

# Webcam input
img_file_buffer = st.camera_input("Neem een foto")

if img_file_buffer is not None:
    # Converteer naar OpenCV formaat
    image = Image.open(img_file_buffer)
    image = np.array(image)
    image = cv2.resize(image, (224, 224))  # Zorg ervoor dat de resolutie klopt met het model
    image = image / 255.0  # Normalisatie
    image = np.expand_dims(image, axis=0)

    # Voorspel klasse
    predictions = model.predict(image)
    class_index = np.argmax(predictions)
    class_label = labels[class_index]
    confidence = predictions[0][class_index]

    st.image(img_file_buffer, caption="Geselecteerde afbeelding", use_column_width=True)
    st.write(f"**Voorspelde klasse:** {class_label} ({confidence:.2f})")
