import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing import image

from src.data_management.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    plot_predictions_probabilities,
                                                    resize_input_image
                                                    )

def page_mildew_prediction_body():
    st.title('Cherry Mildew Predictor')
    st.subheader('General Information')
    st.write('''
    The ML model is a Convolutional Neural Network (CNN) designed for binary image 
    classification. It uses Softmax activation for class probability predictions. 
    The model is compiled using the Adam optimizer and categorical cross-entropy as 
    the loss function. It has an evaluated prediction accuracy of 99.88%.
    ''')
    st.write("---")

    #Load Image
    images_buffer = st.file_uploader('Upload cherry leaf images. You may select more than one.',
                                        type='JPG',accept_multiple_files=True)

    #define image shape
    image_shape = (50,50,3)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            
            pil_image = (Image.open(image))
            #this line of code could be problematic
            #pil_image = image.load_img(image, target_size=image_shape, color_mode='rgb')
            
            #Convert image to array and prepare for prediction
            #my_image = image.img_to_array(pil_image)
            version = 'v5'
            img_array = np.array(pil_image)
            resized_img = resize_input_image(img=pil_image, version=version)
            #my_image = np.expand_dims(my_image, axis=0) / 255.0                       
            
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            col1, col2 = st.columns(2)
            with col1: 
                st.image(pil_image, caption="Uploaded image")
            with col2:
                st.image(resized_img, caption="Processed image")
            st.write(f"Uploaded image profile: Image Size: {pil_image.size[1]}px width x {pil_image.size[0]}px height, Image mode: {pil_image.mode}")      
            
            # Make prediction
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)

            st.write("---")    
            plot_predictions_probabilities(pred_proba, pred_class)
            st.write("---") 
            
            df_report = df_report._append({"Name":image.name, 'Result': pred_class },
                                        ignore_index=True)
        
        if not df_report.empty:
            st.subheader("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)