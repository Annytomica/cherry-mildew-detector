import streamlit as st
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

# Define paths for montage functions
default_montage_path = "outputs/v1/thumbnail_montage.png"
montage_dir = "inputs/datasets/montage"

# Initialize session state for montage if not set
if "current_montage" not in st.session_state:
    st.session_state["current_montage"] = default_montage_path

# main body content - four toggles for displaying plots
def page_leaf_visualisation_body():
    st.title('Cherry Leaf Data Visualisation')
    st.subheader('General Information')
    st.write('''
    The client is interested in conducting a study to visually differentiate a healthy 
    cherry leaf from one with powdery mildew.
    To fulfill this requirement the study contains:
    - An image montage showing a random selection of leaf images from both healthy and 
    powdery mildew infected categories. The montage can be regenerated to include a new 
    selection of images using the "generate new montage" button.
    - Plots of average image and image variability within each category
    - A plot of the differences between the average images from each category
    ''')

    one = st.toggle("Show Image Montage", key="montage_toggle")
    if one:
        st.subheader("Image Montage")
        display_thumbnail_montage()
        st.write('''
        The montage shows that there are clear visual differences between the healthy 
        and powdery mildew infected leaves. Healthy leaves are a uniform bright green 
        color. Powdery mildew infected leaves typically have patches of white powdery 
        deposits (mildew) which may also be accompanied by yellow, black or brown 
        patches of leaf damage/death.
        ''')

    two = st.toggle("Show Average and Variability Plots", key="average_toggle")
    if two:
        st.subheader("Average Image and Image Variability")
        st.image('outputs/v1/mean_var_montage_healthy_v1.png', caption='Healthy')
        st.image('outputs/v1/mean_var_montage_powdery_mildew_v1.png', caption='Powdery Mildew Infected')
        st.write('''
        The average and variability plots do not show clear visual patterns that could 
        be used to distinguish healthy from mildew infected leaves. However, there is 
        a small difference in intensity of the green colouration of the average plots, 
        with healthy leaves having a brighter colouration. Variability plots primarily 
        highlight variability in leaf border due to leaves not being in uniform 
        orientation. Mildew infected leaves show lower contrast to the image background.
        ''')

    three = st.toggle("Show Difference Plot", key="difference_toggle")
    if three:
        st.subheader("Average Image Differences")
        st.image('outputs/v1/diff_btwn_labels.png')
        st.write('''
        The average image difference plot does not show clear visual patterns that could 
        be used to distinguish healthy from mildew infected leaves. The most significant 
        area of difference is the image background.
        ''')

    four = st.toggle("Show Conclusions", key="conclusion_toggle")
    if four:
        st.subheader("Conclusions")
        st.write('''
        The image montage showed there were clear visual differences between healthy 
        and mildew infected leaves. However, these differences were not born out by 
        the average, variability and difference measures. Our conclusion is that while 
        leaf health status can be visually distinguished, these measures were negatively 
        impacted by cherry leaves having a very distinct, non-circular shape and leaf 
        orientation not being uniform in the images. A future goal would be to 
        investigate if outcomes could be improved if leaves were rotated to uniform 
        orientation prior to analysis.
        ''')
        


# Function to display the thumbnail montage
def display_thumbnail_montage():
    # Load and check default montage
    if not os.path.exists(default_montage_path):
        st.error("Default montage not found. Please check the file path.")
        return

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