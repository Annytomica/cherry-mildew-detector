import streamlit as st
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

from src.data_visualisation.visualisation import (
                                                display_thumbnail_montage,
                                                generate_thumbnail_montage,
                                                )

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
        Business requirement 1 is fulfilled. The image montage showed there were clear 
        visual differences between healthy and mildew infected leaves. However, these 
        differences were not born out by the average, variability and difference 
        measures. Our conclusion is that while leaf health status can be visually 
        distinguished, these measures were negatively impacted by cherry leaves having 
        a very distinct, non-circular shape and leaf orientation not being uniform in 
        the images. A future goal would be to investigate if outcomes could be improved 
        if leaves were rotated to uniform orientation prior to analysis.
        ''')
