import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: #F8FAFC;
    }

    .main-title {
    font-size: 36px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 12px;
}

    .subtitle {
        font-size: 18px;
        color: #4B5563;
        margin-bottom: 28px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #111827;
        margin-top: 20px;
        margin-bottom: 14px;
    }

    .card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
    }

    .info-card {
        background-color: #EFF6FF;
        padding: 20px;
        border-radius: 14px;
        border-left: 6px solid #2563EB;
        margin-bottom: 20px;
    }

    .metric-card {
        background-color: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        text-align: center;
    }

    .metric-label {
        font-size: 15px;
        color: #6B7280;
        margin-bottom: 6px;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 800;
        color: #111827;
    }
                
    .block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

    .risk-low {
        border-left: 6px solid #16A34A;
    }

    .risk-medium {
        border-left: 6px solid #F59E0B;
    }

    .risk-high {
        border-left: 6px solid #DC2626;
    }

    .small-text {
        font-size: 14px;
        color: #6B7280;
    }
    </style>
    """, unsafe_allow_html=True)