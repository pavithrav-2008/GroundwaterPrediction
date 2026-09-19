def analyze_scarcity(prediction, rainfall, recharge):
    """
    Water Scarcity Analysis Module
    """

    if prediction < 8 or rainfall < 100 or recharge < 40:
        return (
            "High",
            "🔴",
            "High probability of groundwater scarcity."
        )

    elif prediction < 15 or rainfall < 200 or recharge < 80:
        return (
            "Moderate",
            "🟡",
            "Moderate groundwater scarcity expected."
        )

    else:
        return (
            "Low",
            "🟢",
            "Groundwater availability is currently sufficient."
        )