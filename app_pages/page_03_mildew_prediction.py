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
    st.title('Cherry Mildew Detector')
    st.subheader('General Information')
    st.write('''
    The client is interested in predicting if a cherry leaf is healthy or 
    infected with powdery mildew. The success metric is a prediction 
    accuracy of greater than 97%. These requirements were met, with a 
    classifier model developed with evaluated prediction accuracy of more 
    than 99%. Details on the model evaluation can be found on the 'Model 
    Performance Metrics' page.
    ''')
    st.write("---")
    st.subheader('How to Use:')
    st.write('''
    Images of a cherry leaf, in .JPG/.jpeg format, can be uploaded for 
    evaluation of mildew presence or absence using the file uploader. 
    Once uploaded the images are automatically evaluated and the predicted
    health status of the leaf displayed. An evaluation report, in .csv 
    format, can be downloaded.
    
    **Key Points:**
    - single or multiple images can be uploaded at once
    - additional images uploaded will be added to the same evaluation report
    - to reset the evaluation report refresh the page
    ''')
    st.write(
        f"You can download a set of healthy and powdery mildew infected leaf images "
        f"for live prediction [here](https://www.kaggle.com/codeinstitute/cherry-leaves)."
        )

    #Load Image
    images_buffer = st.file_uploader('Upload cherry leaf images. You may select more than one.',
                                        type='JPG',accept_multiple_files=True)

    #define image shape
    image_shape = (50,50,3)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            
            pil_image = (Image.open(image))

            version = 'v5'
            img_array = np.array(pil_image)
            resized_img = resize_input_image(img=pil_image, version=version)                       
            
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            col1, col2 = st.columns(2)
            with col1: 
                st.image(pil_image)
            with col2:
                st.write("**Uploaded image profile:**")
                st.write(f"Image Name: {image.name}")        
                st.write(f"Image Size: {pil_image.size[1]}px width x {pil_image.size[0]}px height")        
                st.write(f"Image mode: {pil_image.mode}")
            
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