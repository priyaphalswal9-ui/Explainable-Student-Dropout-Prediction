def generate_recommendations(top_shap):

    recommendations = []

    for _, row in top_shap.iterrows():

        feature = row["Display Feature"]
        shap_value = row["SHAP Value"]

        if shap_value <= 0:
            continue

        if feature == "Average Assessment Score":
            recommendations.append(
                "Provide additional academic support and monitor assessment performance regularly."
            )

        elif feature == "Previous Attempts":
            recommendations.append(
                "Review the student's previous learning history and arrange personalized mentoring."
            )

        elif feature == "Total VLE Clicks":
            recommendations.append(
                "Encourage more frequent interaction with the learning platform and digital resources."
            )

        elif feature == "Active Learning Days":
            recommendations.append(
                "Increase weekly learning participation through regular engagement activities."
            )

        elif feature == "Last Learning Activity Day":
            recommendations.append(
                "Reconnect with the student as recent learning activity appears to be low."
            )

        elif feature == "Forum Clicks":
            recommendations.append(
                "Encourage participation in discussion forums and collaborative learning."
            )

        elif feature == "Homepage Clicks":
            recommendations.append(
                "Guide the student to access course resources more consistently."
            )

        elif feature == "Content Clicks":
            recommendations.append(
                "Recommend spending more time exploring course learning materials."
            )

    if len(recommendations) == 0:
        recommendations.append(
            "No major intervention is currently suggested. Continue regular academic monitoring."
        )

    return list(dict.fromkeys(recommendations))