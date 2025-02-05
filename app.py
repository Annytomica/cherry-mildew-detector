import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_01_summary import page_summary_body
from app_pages.page_02_leaf_visualisation import page_leaf_visualisation_body
from app_pages.page_03_mildew_prediction import page_mildew_prediction_body
from app_pages.page_04_project_hypotheses import page_project_hypotheses_body
from app_pages.page_05_model_performance import page_model_performance_metrics

app = MultiPage(app_name="Cherry Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Cherry Leaf Visualisation", page_leaf_visualisation_body)
app.add_page("Mildew Detection", page_mildew_prediction_body)
app.add_page("Project Hypotheses", page_project_hypotheses_body)
app.add_page("Model Performance Metrics", page_model_performance_metrics)

# load style.css for custom styling - code from ricardo.pascoal
with open( "src/css/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.logo('assets/static/mildew_logo.png', size="large", icon_image='assets/static/mildew_logo_icon.png')

app.run()  # Run the app