def get_recommendation(risk_level, ghi):
    """
    Generates groundwater conservation recommendations
    based on Risk Level and Groundwater Health Index.
    """

    recommendations = []

    if risk_level == "High":
        recommendations.extend([
            "🚨 Reduce groundwater extraction immediately.",
            "🌧️ Implement large-scale rainwater harvesting.",
            "💧 Promote artificial groundwater recharge.",
            "📊 Monitor groundwater levels every week."
        ])

    elif risk_level == "Moderate":
        recommendations.extend([
            "💧 Encourage efficient water usage.",
            "🌱 Improve groundwater recharge through recharge pits.",
            "📈 Monitor groundwater levels monthly."
        ])

    else:
        recommendations.extend([
            "✅ Maintain current groundwater conservation practices.",
            "🌳 Continue rainwater harvesting initiatives.",
            "📅 Monitor groundwater levels periodically."
        ])

    # Additional advice based on Groundwater Health Index
    if ghi < 40:
        recommendations.append("⚠️ Groundwater Health Index is Critical. Immediate intervention is recommended.")

    elif ghi < 60:
        recommendations.append("🟠 Improve recharge activities to increase groundwater health.")

    elif ghi >= 80:
        recommendations.append("🟢 Groundwater system is healthy. Continue sustainable management.")

    return recommendations