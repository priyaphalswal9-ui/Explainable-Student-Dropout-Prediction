import streamlit as st


def show_about_model():

    st.markdown(
        '<div class="main-title">About the Model</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        This page provides a detailed overview of the machine learning model,
        dataset, feature engineering process, evaluation metrics, and
        explainability techniques used in this project.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Project Overview</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>Explainable Student Dropout Prediction using XGBoost & SHAP</h4>
        <p>
            This application predicts the likelihood of student dropout in online
            learning environments using a tuned XGBoost classifier.
        </p>
        <p>
            The primary objective is to help educational institutions identify
            students who may require early academic intervention.
        </p>
        <p>
            Instead of only predicting whether a student is at risk, the application
            also explains <b>why</b> the prediction was made using SHAP
            (SHapley Additive Explanations).
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Dataset Information</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <h4>32,548</h4>
            <p>Student Records</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>46</h4>
            <p>Raw Features</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h4>76</h4>
            <p>Encoded Model Features</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <h4>Dropout</h4>
            <p>Target Variable</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>
            The project uses the Open University Learning Analytics Dataset
            after cleaning, feature engineering, and transformation into a
            model-ready format. The final model input contains academic,
            demographic, assessment, and learning engagement features.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Feature Engineering</div>', unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
        <div class="card">
            <h4>Data Preparation</h4>
            Missing Value Handling<br>
            Feature Engineering<br>
            Assessment Statistics<br>
            Learning Engagement Features<br>
            Binary Encoding<br>
            One-Hot Encoding<br>
            Feature Alignment for Deployment
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="card">
            <h4>Engineered Features</h4>
            Average Assessment Score<br>
            Maximum Assessment Score<br>
            Minimum Assessment Score<br>
            Total Assessments<br>
            Average Assessment Weight<br>
            Total Clicks<br>
            Active Learning Days<br>
            Last Activity Day
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Model Selection</div>', unsafe_allow_html=True)

    comparison = {
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "XGBoost"
        ],
        "Role": [
            "Baseline Model",
            "Compared Model",
            "Compared Model",
            "Final Selected Model"
        ]
    }

    st.table(comparison)

    st.markdown("""
    <div class="card">
        <h4>Why XGBoost?</h4>
        <p>
            XGBoost was selected because it achieved the strongest overall
            performance and provided the best balance between precision, recall,
            F1-score, and ROC-AUC.
        </p>
        <p>
            It also integrates effectively with SHAP, which makes it suitable
            for explainable student-level predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Final Model Performance</div>', unsafe_allow_html=True)

    metric1, metric2, metric3, metric4, metric5 = st.columns(5)

    with metric1:
        st.markdown("""
        <div class="card">
            <h4>86.90%</h4>
            <p>Accuracy</p>
        </div>
        """, unsafe_allow_html=True)

    with metric2:
        st.markdown("""
        <div class="card">
            <h4>73.79%</h4>
            <p>Precision</p>
        </div>
        """, unsafe_allow_html=True)

    with metric3:
        st.markdown("""
        <div class="card">
            <h4>89.72%</h4>
            <p>Recall</p>
        </div>
        """, unsafe_allow_html=True)

    with metric4:
        st.markdown("""
        <div class="card">
            <h4>80.98%</h4>
            <p>F1 Score</p>
        </div>
        """, unsafe_allow_html=True)

    with metric5:
        st.markdown("""
        <div class="card">
            <h4>94.58%</h4>
            <p>ROC-AUC</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>Performance Interpretation</h4>
        <p>
            The model achieved strong recall and ROC-AUC. For dropout prediction,
            recall is especially important because missing an at-risk student can
            be more harmful than incorrectly flagging a stable student.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Explainable AI</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>SHAP-Based Explanation</h4>
        <p>
            SHAP is used to explain how individual features influence each
            prediction. Positive SHAP values increase predicted dropout risk,
            while negative SHAP values reduce predicted dropout risk.
        </p>
        <p>
            The application provides both teacher-friendly business explanations
            and technical SHAP-based explanations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Strengths and Limitations</div>', unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
        <div class="card">
            <h4>Strengths</h4>
            Explainable predictions<br>
            Batch prediction support<br>
            Personalized recommendations<br>
            What-if simulation<br>
            SHAP-based interpretation<br>
            Modular software architecture
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="card">
            <h4>Limitations</h4>
            Trained on OULAD dataset<br>
            Depends on input data quality<br>
            Predictions are probabilistic<br>
            Should not replace human academic judgment<br>
            May require retraining for new institutions
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Future Scope</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        Real-time LMS integration<br>
        Instructor dashboard<br>
        Early warning notifications<br>
        Intervention tracking<br>
        Continuous model retraining<br>
        Fairness and bias monitoring
    </div>
    """, unsafe_allow_html=True)