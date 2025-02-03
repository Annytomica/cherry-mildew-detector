import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_model import load_test_evaluation

def page_model_performance_metrics():
    st.title('ML Model Performance Metrics')
    st.subheader('General Information')

    # The following code is from CI malaria walkthrough project with minimal changes
    version = 'v5'

    st.subheader('Train, Validation and Test Set: Labels Frequencies')

    labels_distribution = plt.imread("outputs/v1/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.subheader('Model Training History')
    col1, col2 = st.columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc_{version}.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses_{version}.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.subheader('Model Performance on Test Set')
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))