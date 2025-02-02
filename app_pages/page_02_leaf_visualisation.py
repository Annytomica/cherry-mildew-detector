import streamlit as st

def page_leaf_visualisation_body():
    st.title('Cherry Leaf Data Visualisation')
    st.subheader('General Information')
    st.write('summaryleaf visualisation page')

    one = st.toggle("Show Image Montage", key="montage_toggle")
    if one:
        st.write("Image Montage activated!")
        st.image('outputs/v1/thumbnail_montage.png')

    two = st.toggle("Show Average and Variability Plots", key="healthy_toggle")
    if two:
        st.write("Average & Variability Plots activated!")
        st.image('outputs/v1/mean_var_montage_healthy_v1.png')

    three = st.toggle("Show Powdery Mildew Differences", key="mildew_toggle")
    if three:
        st.write("Powdery Mildew Differences activated!")
        st.image('outputs/v1/mean_var_montage_powdery_mildew_v1.png')

    four = st.toggle("Show Label Differences", key="difference_toggle")
    if four:
        st.write("Label Differences activated!")
        st.image('outputs/v1/diff_btwn_labels.png')