import shap
import pandas as pd


FEATURE_DISPLAY_NAMES = {
    "gender_M": "Gender",
    "gender_F": "Gender",
    "highest_education_No Formal quals": "Highest Education",
    "highest_education_Lower Than A Level": "Highest Education",
    "highest_education_A Level or Equivalent": "Highest Education",
    "highest_education_HE Qualification": "Highest Education",
    "highest_education_Post Graduate Qualification": "Highest Education",
    "age_band_0-35": "Age Band",
    "age_band_35-55": "Age Band",
    "age_band_55<=": "Age Band",
    "disability_Y": "Disability",
    "disability_N": "Disability",
    "num_of_prev_attempts": "Previous Attempts",
    "studied_credits": "Studied Credits",
    "average_score": "Average Assessment Score",
    "max_score": "Maximum Assessment Score",
    "min_score": "Minimum Assessment Score",
    "total_assessments": "Total Assessments",
    "average_weight": "Average Assessment Weight",
    "total_clicks": "Total VLE Clicks",
    "active_days": "Active Learning Days",
    "last_activity_day": "Last Learning Activity Day",
    "forum_clicks": "Forum Clicks",
    "homepage_clicks": "Homepage Clicks",
    "content_clicks": "Content Clicks"
}


DEMO_FEATURES = list(FEATURE_DISPLAY_NAMES.keys())


def get_shap_explanation(model, input_encoded):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_encoded)

    shap_df = pd.DataFrame({
        "Feature": input_encoded.columns,
        "SHAP Value": shap_values[0]
    })

    shap_df["Impact"] = shap_df["SHAP Value"].abs()

    shap_df = shap_df[shap_df["Feature"].isin(DEMO_FEATURES)]

    shap_df["Display Feature"] = shap_df["Feature"].map(FEATURE_DISPLAY_NAMES)

    shap_df = shap_df.sort_values(
        by="Impact",
        ascending=False
    )

    return shap_df