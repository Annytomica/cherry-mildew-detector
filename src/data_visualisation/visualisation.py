import streamlit as st
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# functions in this file from data visualisation notebook, with assistance
# from ChatGPT to refactor for dashboard

# Define paths for montage functions
default_montage_path = "outputs/v1/thumbnail_montage.png"
montage_dir = "inputs/datasets/montage"

# Function to display the thumbnail montage
def display_thumbnail_montage():
    # Load and check default montage
    if not os.path.exists(default_montage_path):
        st.error("Default montage not found. Please check the file path.")
        return
    
    # Initialize session state for montage if not set
    if "current_montage" not in st.session_state:
        st.session_state["current_montage"] = default_montage_path

    # Placeholder for the montage
    montage_placeholder = st.empty()

    # Display the current montage from session state
    montage_placeholder.image(st.session_state["current_montage"], use_container_width=True)

    # Button to generate a new montage
    if st.button("Generate New Montage"):
        if os.path.exists(montage_dir):  # Check if the montage dataset exists
            with montage_placeholder:  # Ensure the spinner replaces the default montage
                with st.spinner("🔄 Montage loading..."):
                    new_montage = generate_thumbnail_montage(data_dir=montage_dir, labels=["healthy", "powdery_mildew"], new_size=(150, 150))

                # Save new montage in session state
                st.session_state["current_montage"] = new_montage

                # Replace with new montage
                montage_placeholder.image(new_montage, use_container_width=True)
        else:
            montage_placeholder.image(default_montage, use_container_width=True)
            st.warning("Montage dataset not found. Default montage shown.")


# Function to generate thumbnail montage - modified from data visualisation notebook
def generate_thumbnail_montage(data_dir, labels, new_size=(150, 150)):
    """
    Generates a thumbnail montage with 2x2 grids for each label side-by-side.
    
    Args:
        data_dir (str): Path to the dataset directory.
        labels (list): List of labels (subfolders) to sample from.
        new_size (tuple): Desired size of each thumbnail image.
    
    Returns:
        PIL.Image: The generated montage image.
    """
    if len(labels) != 2:
        raise ValueError("This function assumes exactly 2 labels for side-by-side layout.")

    # Create a figure for the montage
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    fig.subplots_adjust(wspace=0.3, hspace=0.3)

    for i, label in enumerate(labels):
        label_dir = os.path.join(data_dir, label)
        image_filenames = random.sample(os.listdir(label_dir), 4)  # Select 4 random images per label

        for j, img_file in enumerate(image_filenames):
            row = j // 2
            col = j % 2 + (i * 2)  # Offset by 2 for the second label
            img_path = os.path.join(label_dir, img_file)
            img = image.load_img(img_path, target_size=new_size)
            img_array = image.img_to_array(img) / 255.0  # Normalize

            axes[row, col].imshow(img_array)
            axes[row, col].axis('off')

        # Add a title for each class
        axes[0, i * 2].set_title(f"{label.capitalize()}", fontsize=16, loc='center')
        axes[0, i * 2 + 1].set_title("")

    plt.tight_layout()

    # Convert Matplotlib figure to a PIL image
    buf = io.BytesIO()  # Create an in-memory buffer
    plt.savefig(buf, format="png", bbox_inches="tight", dpi=150)
    plt.close(fig)  # Close the figure to free memory

    buf.seek(0)  # Move cursor to the beginning of the buffer
    montage_image = Image.open(buf)  # Open image as a PIL object

    return montage_image  # Return the PIL image instead of saving