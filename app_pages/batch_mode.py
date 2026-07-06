import streamlit as st
import pandas as pd

from utils.model_loader import load_model, load_feature_names
from utils.preprocessing import encode_and_align
from utils.shap_utils import get_shap_explanation
from utils.recommendations import generate_recommendations


def show_batch_mode():
    model = load_model()
    feature_names = load_feature_names()

    st.markdown(
        '<div class="main-title">Full Feature Prediction Mode</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        Upload the processed final dataset. The application will encode,
        align features, and generate dropout predictions for all students.
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload final_dataset.csv",
        type=["csv"]
    )

    if uploaded_file is None:
        st.markdown("""
        <div class="card">
            Upload final_dataset.csv to generate predictions for multiple students.
        </div>
        """, unsafe_allow_html=True)
        return

    data = pd.read_csv(uploaded_file)

    st.markdown('<div class="section-title">Uploaded Data Preview</div>', unsafe_allow_html=True)
    st.dataframe(data.head(), use_container_width=True)

    input_data = data.copy()

    if "dropout" in input_data.columns:
        input_data = input_data.drop(columns=["dropout"])

    input_encoded = encode_and_align(input_data, feature_names)

    predictions = model.predict(input_encoded)
    probabilities = model.predict_proba(input_encoded)[:, 1]

    results = data.copy()
    results["dropout_prediction"] = predictions
    results["dropout_probability"] = probabilities
    results["prediction_label"] = results["dropout_prediction"].map(
        {
            0: "Continue",
            1: "At Risk of Dropout"
        }
    )

    st.markdown('<div class="section-title">Prediction Results</div>', unsafe_allow_html=True)

    st.dataframe(
        results[["prediction_label", "dropout_probability"]].head(20),
        use_container_width=True
    )

    csv_data = results.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Prediction Results",
        data=csv_data,
        file_name="student_dropout_predictions.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown('<div class="section-title">Single Student Explanation</div>', unsafe_allow_html=True)

    student_options = list(results.index)

    selected_index = st.selectbox(
        "Select student row for explanation",
        student_options,
        format_func=lambda x: f"Student Row {x}"
    )

    selected_prediction = results.loc[selected_index, "prediction_label"]
    selected_probability = results.loc[selected_index, "dropout_probability"]

    st.markdown(f"""
    <div class="card">
        <h4>Selected Student Summary</h4>
        <p><b>Prediction:</b> {selected_prediction}</p>
        <p><b>Dropout Probability:</b> {selected_probability:.2%}</p>
    </div>
    """, unsafe_allow_html=True)

    selected_encoded = input_encoded.iloc[[selected_index]]

    student_shap_df = get_shap_explanation(model, selected_encoded)
    top_shap = student_shap_df.head(5).copy()

    st.markdown('<div class="section-title">SHAP Explanation for Selected Student</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>
            These features had the strongest influence on this selected student's prediction.
            Positive SHAP values increase dropout risk, while negative SHAP values reduce dropout risk.
        </p>
    </div>
    """, unsafe_allow_html=True)

    for _, row in top_shap.iterrows():
        shap_value = row["SHAP Value"]
        feature_name = row["Display Feature"]

        if shap_value > 0:
            impact_text = "This factor increases the predicted dropout risk."
            sign = "+"
        else:
            impact_text = "This factor reduces the predicted dropout risk."
            sign = ""

        st.markdown(f"""
        <div class="card">
            <h4>{feature_name}</h4>
            <p><b>SHAP Contribution:</b> {sign}{shap_value:.4f}</p>
            <p>{impact_text}</p>
        </div>
        """, unsafe_allow_html=True)

    recommendations = generate_recommendations(top_shap)

    st.markdown('<div class="section-title">Personalized Recommendations</div>', unsafe_allow_html=True)

    for recommendation in recommendations:
        st.markdown(f"""
        <div class="card">
            <p>{recommendation}</p>
        </div>
        """, unsafe_allow_html=True)