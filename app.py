import streamlit as st

from utils.styles import load_css
from app_pages.home import show_home
from app_pages.demo_mode import show_demo_mode
from app_pages.batch_mode import show_batch_mode
from app_pages.about_model import show_about_model

st.set_page_config(
    page_title="Explainable Student Dropout Prediction",
    layout="wide"
)

load_css()

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Demo Prediction Mode",
        "Full Feature Prediction Mode",
        "About Model"
    ]
)

if page == "Home":
    show_home()
elif page == "Demo Prediction Mode":
    show_demo_mode()
elif page == "Full Feature Prediction Mode":
    show_batch_mode()
elif page == "About Model":
    show_about_model()