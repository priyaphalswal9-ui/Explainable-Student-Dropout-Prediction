def get_risk_level(probability):
    if probability < 0.30:
        return "Low Risk", "risk-low"
    elif probability <= 0.70:
        return "Medium Risk", "risk-medium"
    else:
        return "High Risk", "risk-high"


def get_confidence_level(probability):
    distance = abs(probability - 0.50)

    if distance < 0.10:
        return "Moderate"
    elif distance < 0.30:
        return "High"
    else:
        return "Very High"