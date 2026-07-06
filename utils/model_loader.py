import os
import pickle
import streamlit as st


MODEL_PATH = os.path.join("models", "student_dropout_xgboost.pkl")
FEATURE_PATH = os.path.join("models", "feature_names.pkl")


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    return model


@st.cache_data
def load_feature_names():
    with open(FEATURE_PATH, "rb") as file:
        feature_names = pickle.load(file)
    return feature_names