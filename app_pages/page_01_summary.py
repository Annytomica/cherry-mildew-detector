import streamlit as st

def page_summary_body():
    st.image('assets/static/mildew_hero_tall.png')
    st.title('Project Summary')
    st.subheader('General Information')
    st.write('''
    Powdery mildew is an infection found in cherry trees that is caused by the 
    fungus *Podosphaera clandestina*. It presents as white powdery patches on new 
    or young leaves, with growth typically starting on the underside of the leaf. 
    The infection will not kill the leaf but can cause distortion and discolouration. 
    This infection can be transferred to the cherry fruit as they mature, causing 
    damage and losses to the cherry crop. Detection of powdery mildew infection 
    involves visual inspection of individual leaves on each cherry tree.
    ''')
    st.subheader('Project Dataset')
    st.write('''
    The dataset provided by the client contains 4208 .jpg images of healthy and 
    powdery-mildew infected cherry leaves taken from their cherry farms.


    For additional information on the project and dataset, please visit and **read** the 
    [Project README file](https://github.com/Annytomica/cherry-mildew-detector).
    ''')
    st.subheader('Business Requirements')
    st.write('''
    The project has 2 business requirements:

    1. The client is interested in conducting a study to visually differentiate 
        a healthy cherry leaf from one with powdery mildew.

    2. The client is interested in predicting if a cherry leaf is healthy or 
        infected with powdery mildew.
    ''')