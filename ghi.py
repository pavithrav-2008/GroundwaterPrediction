def calculate_ghi(prediction, rainfall, soil_moisture, recharge, water_consumption):
    """
    Calculates Groundwater Health Index (0–100)
    """

    # Normalize values to 0–100
    groundwater_score = min(max((prediction / 25) * 100, 0), 100)
    rainfall_score = min(max((rainfall / 300) * 100, 0), 100)
    soil_score = min(max(soil_moisture, 0), 100)
    recharge_score = min(max((recharge / 150) * 100, 0), 100)

    # Lower water consumption is better
    consumption_score = 100 - min(max((water_consumption / 500) * 100, 0), 100)

    # Weighted Groundwater Health Index
    ghi = (
        groundwater_score * 0.35 +
        rainfall_score * 0.20 +
        soil_score * 0.20 +
        recharge_score * 0.15 +
        consumption_score * 0.10
    )

    ghi = round(ghi, 2)

    # Health status
    if ghi >= 80:
        status = "Excellent"
        color = "🟢"

    elif ghi >= 60:
        status = "Good"
        color = "🟡"

    elif ghi >= 40:
        status = "Moderate"
        color = "🟠"

    else:
        status = "Critical"
        color = "🔴"

    return ghi, status, color