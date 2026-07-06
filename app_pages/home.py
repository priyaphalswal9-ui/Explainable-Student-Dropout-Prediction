import streamlit as st
def show_home():
    st.markdown(
        '<div class="main-title">Explainable Student Dropout Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Early identification of at-risk students using XGBoost and Explainable AI.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h2>Project Overview</h2>
        <p>
        This application predicts whether a student is at risk of dropping out from an online learning course.
        It uses machine learning to support early intervention and SHAP explainability to make predictions more transparent.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Dataset</div>
            <div class="metric-value">OULAD</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Final Features</div>
            <div class="metric-value">76</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Final Model</div>
            <div class="metric-value">XGBoost</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Explainability</div>
            <div class="metric-value">SHAP</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Project Workflow</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p><b>1. Data Understanding:</b> OULAD tables were explored to understand student demographics, assessments, registration, and VLE engagement.</p>
        <p><b>2. Feature Engineering:</b> Assessment scores, activity clicks, active days, and registration behavior were transformed into meaningful ML features.</p>
        <p><b>3. Model Training:</b> Multiple models were compared, and tuned XGBoost was selected due to strong recall for dropout detection.</p>
        <p><b>4. Explainability:</b> SHAP was used to explain which features influenced each prediction.</p>
        <p><b>5. Intervention Support:</b> Predictions are converted into risk levels and personalized recommendations for teachers or advisors.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Why This Project Matters</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        Student dropout is a serious challenge in online learning environments.
        Early identification of at-risk students can help teachers, mentors, and academic advisors take timely action.
        This project focuses not only on prediction accuracy, but also on explaining the reasons behind each prediction.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Application Modes</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("""
        <div class="card">
            <h3>Demo Prediction Mode</h3>
            <p>
            Allows manual prediction using selected meaningful features.
            This mode is useful for demonstration and understanding the model behavior.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="card">
            <h3>Full Feature Prediction Mode</h3>
            <p>
            Allows batch prediction using a processed CSV file with the full feature structure.
            This mode is more suitable for institutional-style prediction.
            </p>
        </div>
        """, unsafe_allow_html=True)
