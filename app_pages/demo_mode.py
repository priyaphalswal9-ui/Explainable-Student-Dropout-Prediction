import streamlit as st

from utils.model_loader import load_model, load_feature_names
from utils.preprocessing import create_input_dataframe, encode_and_align
from utils.prediction import predict_dropout
from utils.risk_utils import get_risk_level, get_confidence_level
from utils.shap_utils import get_shap_explanation
from utils.recommendations import generate_recommendations


def generate_business_explanation(prediction, probability, risk_level, confidence_level):
    probability_percent = probability * 100

    if prediction == 1:
        return f"""
The model predicts that this student may be at risk of dropout.

The estimated dropout probability is {probability_percent:.2f}%.

Risk Level: {risk_level}

Confidence Level: {confidence_level}

From an academic support perspective, this student should be monitored carefully. The prediction suggests that the student may need timely academic guidance, engagement support, or intervention before the risk becomes severe.

This result should not be treated as a final institutional decision. It should be used as an early warning signal to support teachers, mentors, or academic advisors.
"""

    return f"""
The model predicts that this student is currently unlikely to drop out.

The estimated dropout probability is {probability_percent:.2f}%.

Risk Level: {risk_level}

Confidence Level: {confidence_level}

From an academic support perspective, this student appears relatively stable based on the selected input features. However, continued monitoring is still useful if academic performance or learning engagement changes over time.

This result should not be treated as a permanent status. It represents the current risk estimate based on the available student information.
"""


def show_demo_mode():
    model = load_model()
    feature_names = load_feature_names()

    st.markdown('<div class="main-title">Demo Prediction Mode</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="subtitle">
        Predict student dropout risk using selected meaningful features.
        This mode is intended for demonstration and educational purposes.
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns([2, 3], gap="large")

    with left:
        st.markdown('<div class="section-title">Student Information</div>', unsafe_allow_html=True)

        gender = st.selectbox("Gender", ["Male", "Female"])

        education = st.selectbox(
            "Highest Education",
            [
                "No Formal quals",
                "Lower Than A Level",
                "A Level or Equivalent",
                "HE Qualification",
                "Post Graduate Qualification"
            ]
        )

        age = st.selectbox("Age Band", ["0-35", "35-55", "55<="])
        disability = st.selectbox("Disability", ["No", "Yes"])

        previous_attempts = st.number_input("Previous Attempts", 0, 10, 0)
        studied_credits = st.number_input("Studied Credits", 0, 300, 60)

        st.divider()

        st.markdown('<div class="section-title">Academic Performance</div>', unsafe_allow_html=True)

        average_score = st.slider("Average Score", 0.0, 100.0, 70.0)
        max_score = st.slider("Maximum Score", 0.0, 100.0, 85.0)
        min_score = st.slider("Minimum Score", 0.0, 100.0, 50.0)
        total_assessments = st.number_input("Total Assessments", 0, 20, 5)
        average_weight = st.slider("Average Assessment Weight", 0.0, 100.0, 20.0)

        st.divider()

        st.markdown('<div class="section-title">Learning Engagement</div>', unsafe_allow_html=True)

        total_clicks = st.number_input("Total Clicks", 0, 10000, 500)
        active_days = st.number_input("Active Days", 0, 300, 60)
        last_activity_day = st.number_input("Last Activity Day", -30, 300, 120)
        forum_clicks = st.number_input("Forum Clicks", 0, 5000, 100)
        homepage_clicks = st.number_input("Homepage Clicks", 0, 5000, 100)
        content_clicks = st.number_input("Content Clicks", 0, 5000, 100)

        predict_button = st.button("Generate Prediction", use_container_width=True)

    with right:
        st.markdown('<div class="section-title">Prediction Result</div>', unsafe_allow_html=True)

        if predict_button:
            input_data = {
                "gender": "M" if gender == "Male" else "F",
                "highest_education": education,
                "age_band": age,
                "disability": "Y" if disability == "Yes" else "N",
                "num_of_prev_attempts": previous_attempts,
                "studied_credits": studied_credits,
                "average_score": average_score,
                "max_score": max_score,
                "min_score": min_score,
                "total_assessments": total_assessments,
                "average_weight": average_weight,
                "total_clicks": total_clicks,
                "active_days": active_days,
                "last_activity_day": last_activity_day,
                "forum_clicks": forum_clicks,
                "homepage_clicks": homepage_clicks,
                "content_clicks": content_clicks,
            }

            input_df = create_input_dataframe(input_data)
            input_encoded = encode_and_align(input_df, feature_names)

            prediction, probability = predict_dropout(model, input_encoded)
            risk_level, risk_class = get_risk_level(probability)
            confidence = get_confidence_level(probability)

            prediction_text = (
                "Student is predicted to be at risk of dropout"
                if prediction == 1
                else "Student is predicted to continue"
            )

            st.markdown(f"""
            <div class="card {risk_class}">
                <h3>Prediction Result</h3>
                <p><b>{prediction_text}</b></p>
                <p class="metric-label">Dropout Probability</p>
                <p class="metric-value">{probability:.2%}</p>
                <p><b>Risk Level:</b> {risk_level}</p>
                <p><b>Confidence Level:</b> {confidence}</p>
            </div>
            """, unsafe_allow_html=True)

            business_explanation = generate_business_explanation(
                prediction=prediction,
                probability=probability,
                risk_level=risk_level,
                confidence_level=confidence
            )

            st.markdown('<div class="section-title">Business Explanation</div>', unsafe_allow_html=True)

            st.markdown(f"""
            <div class="card">
                <p style="white-space: pre-line;">{business_explanation}</p>
            </div>
            """, unsafe_allow_html=True)

            shap_df = get_shap_explanation(model, input_encoded)
            top_shap = shap_df.head(5).copy()

            st.markdown('<div class="section-title">SHAP Technical Explanation</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="card">
                <p>
                    This section explains which model features had the strongest influence
                    on this individual prediction. Positive SHAP values push the prediction
                    toward dropout risk, while negative SHAP values reduce the predicted risk.
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

            st.markdown('<div class="section-title">What-If Simulation</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="card">
                <p>
                    Adjust key academic and engagement values to see how the dropout
                    probability may change. This simulation uses the same trained model
                    and should be interpreted as a decision-support tool, not a guarantee.
                </p>
            </div>
            """, unsafe_allow_html=True)

            sim_average_score = st.slider(
                "Simulated Average Score",
                0.0,
                100.0,
                float(average_score)
            )

            sim_total_clicks = st.number_input(
                "Simulated Total Clicks",
                0,
                10000,
                int(total_clicks)
            )

            sim_active_days = st.number_input(
                "Simulated Active Days",
                0,
                300,
                int(active_days)
            )

            simulate_button = st.button(
                "Run What-If Simulation",
                use_container_width=True
            )

            if simulate_button:
                simulated_input_data = input_data.copy()

                simulated_input_data["average_score"] = sim_average_score
                simulated_input_data["total_clicks"] = sim_total_clicks
                simulated_input_data["active_days"] = sim_active_days

                simulated_df = create_input_dataframe(simulated_input_data)
                simulated_encoded = encode_and_align(simulated_df, feature_names)

                simulated_prediction, simulated_probability = predict_dropout(
                    model,
                    simulated_encoded
                )

                simulated_risk_level, simulated_risk_class = get_risk_level(simulated_probability)
                probability_change = simulated_probability - probability

                if probability_change < 0:
                    change_text = f"Dropout probability decreased by {abs(probability_change):.2%}."
                elif probability_change > 0:
                    change_text = f"Dropout probability increased by {probability_change:.2%}."
                else:
                    change_text = "Dropout probability did not change."

                st.markdown(f"""
                <div class="card {simulated_risk_class}">
                    <h4>Simulation Result</h4>
                    <p><b>Original Probability:</b> {probability:.2%}</p>
                    <p><b>Simulated Probability:</b> {simulated_probability:.2%}</p>
                    <p><b>Original Risk Level:</b> {risk_level}</p>
                    <p><b>Simulated Risk Level:</b> {simulated_risk_level}</p>
                    <p><b>{change_text}</b></p>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="card">
                Prediction results will appear here after clicking
                <b>Generate Prediction</b>.
            </div>
            """, unsafe_allow_html=True)