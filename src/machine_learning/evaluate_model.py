import streamlit as st
from src.data_management.data_management import load_pkl_file

# The following code is from CI malaria walkthrough project with minimal changes
def load_test_evaluation(version):
    return load_pkl_file(f'outputs/{version}/evaluation_{version}.pkl')
