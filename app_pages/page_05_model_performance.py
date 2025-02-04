import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_model import load_test_evaluation

def page_model_performance_metrics():
    st.title('ML Model Performance Metrics')
    st.subheader('General Information')
    st.write('''
    The ML model is a Convolutional Neural Network (CNN) designed for binary image 
    classification. It uses Softmax activation for class probability predictions. 
    The model is compiled using the Adam optimizer and categorical cross-entropy as 
    the loss function. It has a prediction accuracy of 99.88%.
    
    The performance metrics are:
    - measurement of label frequencies in train, validation and test sets to assess
    whether the labels are balanced or unbalanced.
    - Plots of training accuracy and losses to assess whether model training went as 
    expected and model peformance improved across epochs.
    - performance on the test dataset to assess prediction accuracy and whether model
    is under- or over-fitted to the dataset. This includes:
        - test evaluation
        - confusion matrix
        - classification report
    ''')
    st.write("---")

    # The following code is based on CI malaria walkthrough project with addition
    # of confusion matrix and classification report
    version = 'v5'

    one = st.toggle("Show Label Frequencies", key="label_toggle")
    if one:
        st.subheader('Train, Validation and Test Set: Label Frequencies')

        labels_distribution = plt.imread("outputs/v1/labels_distribution.png")
        st.image(labels_distribution)
        st.write('''
        **Summary:**
        Labels are balanced. The number of images in each set is small and the training 
        data required augmentation to address this.
        ''')
        st.write("---")

    two = st.toggle("Show Training History", key="history_toggle")
    if two:
        st.subheader('Model Training History')
        col1, col2 = st.columns(2)
        with col1: 
            model_acc = plt.imread(f"outputs/{version}/model_training_acc_{version}.png")
            st.image(model_acc, caption='Model Training Accuracy')
        with col2:
            model_loss = plt.imread(f"outputs/{version}/model_training_losses_{version}.png")
            st.image(model_loss, caption='Model Training Losses')
        st.write('''
        **Summary:**
        Plots show training went as expected and model peformance improved across epochs.
        ''')
        st.write("---")

    three = st.toggle("Show Performance on Test Set", key="performance_toggle")
    if three:
        st.subheader('Model Performance on Test Set')
        st.write('**Test Evaluation**')
        st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
    
        st.write(" ")
    
        # confusion matrix and classification report
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Confusion Matrix**')
            cm = plt.imread(f"outputs/{version}/test_confusion_matrix_{version}.png")
            st.image(cm) 
        with col2:
            st.write(' ')
    
        st.write(" ")

        # code to display classification report developed with assistance from ChatGPT
        class_report_path = f"outputs/{version}/classification_report_{version}.txt"
        with open(class_report_path, "r") as file:
            class_report = file.read()
        # Display the file contents with preserved formatting
        st.write('**Classification Report**')
        st.code(class_report, language="text")
        st.write('''
        **Summary:**
        Evaluation shows model fulfilled successs metric with an accuracy of 99.88%. However,
        the 'perfect scores' of the confusion matrix and classification report indicate the 
        potential for the model to have over-fitted to the small dataset and model may have 
        reduced accuracy on new data.
        ''')
        
        st.write("---")
    
    four = st.toggle("Show Conclusions", key="metrics_toggle")
    if four: 
        st.subheader('Conclusions')
        st.write('''
        The trained model fulfilled business requirement 2 and the success metric of greater
        than 97% prediction accuracy. However, the study also identified that the small
        dataset used for model development increased the potential for over-fitting. 
        Our recommendation is for more data to be collected to ensure the model maintains
        its high accuracy of prediction on new data.
        ''')