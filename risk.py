def assess_risk(prediction, rainfall, recharge):
    """
    Determines groundwater risk level based on
    predicted groundwater level, rainfall, and recharge.
    """

    # High Risk
    if prediction < 8 or rainfall < 80 or recharge < 40:
        return (
            "High",
            "🔴",
            "Immediate conservation measures are required."
        )

    # Moderate Risk
    elif prediction < 15 or rainfall < 150 or recharge < 80:
        return (
            "Moderate",
            "🟡",
            "Monitor groundwater usage and promote recharge."
        )

    # Low Risk
    else:
        return (
            "Low",
            "🟢",
            "Groundwater conditions are currently healthy."
        )