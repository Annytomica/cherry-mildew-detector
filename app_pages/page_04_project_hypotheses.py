import streamlit as st

def page_project_hypotheses_body():
    st.title('Project Hypotheses')
    st.subheader('Primary Hypothesis')
    st.write('''
    **Mildew infected leaves will have clear signs of white mildew that 
    can differentiate them from a healthy leaf.**
    
    An image montage shows that typically a mildew infected leaf has patches 
    of white powdery deposits (mildew) which may also be accompanied by black 
    or brown patches of leaf damage/death.
    
    A trained CNN model was able to distinguish between healthy and mildew 
    infected leaves with 99% accuracy.
    
    However, Average Image, Variability Image and Difference between Averages studies 
    did not reveal any clear pattern to differentiate one from another.
    
    ''')
    st.write(' ')
    st.subheader('Secondary Hypotheses')
    st.write('''
    *These hypotheses are technical in nature and intended to improve outcome of
    Primary Hypothesis*
    ''')
    
    st.write('''
    **Mildew infection is not as easily distinguished from healthy leaves on 
    low resolution images**
    
    Training models on different image resolutions did not significantly impact 
    prediction accuracy. It did impact model file size. For dashboard performance
    reasons the smaller model, trained on lower resolution images, was chosen.
    ''')
    st.write('''
    **Dataset is small and model performance and accuracy of prediction will 
    be negatively impacted**
    
    This was addressed through augmentation of training dataset to increase sample 
    size. Evaluation of model performance indicates that this may not have been 
    sufficient with a risk of lower accuracy with new data. Collecting additional 
    image data is recommended.
    ''')
    st.write('''
    **Visual differentiation of healthy and infected leaves can be improved by 
    aligning leaf images in the same orientation**
    
    Rotating images prior to Average Image, Variability Image and Difference between 
    Averages studies improved the ability to differentiate healthy from mildew 
    infected leaves. It was not required for image montage or training of mildew 
    detection model.
    ''')