import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management.data_management import load_pkl_file

# The following code is from CI malaria walkthrough project with minimal changes
def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plots prediction probabilities for each class.
    Args:
        pred_proba (np.array): Array of predicted probabilities.
        pred_class (str): Predicted class label.
    """
    # Define class labels (ensure these match your training class order)
    class_labels = ["Healthy", "Powdery Mildew"]

    # Create a DataFrame with class probabilities
    prob_per_class = pd.DataFrame([pred_proba], columns=class_labels)

    # Ensure that the index matches the predicted class name
    prob_per_class.index = ["Predicted Probabilities"]

    # Plot the probabilities
    st.subheader("Class Prediction Probabilities")
    st.bar_chart(prob_per_class.T)  # Transpose to match class labels on y-axis

    # Show final prediction
    st.error(f"**Predicted Class:** {pred_class} with {max(pred_proba) * 100:.2f}% confidence")


# resize image dimensions
def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = load_pkl_file(file_path=f"outputs/v1/image_shape_small.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image

# Function modified from notebook code to analyse single image
def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction on uploaded live images
    """
    # Define class labels (adjust according to your dataset)
    class_labels = ["Healthy", "Powdery Mildew"] 

    # Load model
    model = load_model(f'outputs/{version}/mildew_detector_model_{version}.h5')

    # Make prediction
    pred_proba = model.predict(my_image)[0]  # Get softmax output (2 values)

    # Interpret prediction
    pred_class_idx = np.argmax(pred_proba)  # Get index of highest probability
    pred_class = class_labels[pred_class_idx]  # Convert index to label

    st.error(
        f"The predictive analysis indicates the leaf health status is "
        f"**{pred_class}**"
        )
    
    return pred_proba, pred_class



