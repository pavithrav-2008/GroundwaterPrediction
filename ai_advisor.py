def generate_ai_advice(
    prediction,
    risk_level,
    ghi,
    scarcity_level,
    rainfall,
    temperature,
    humidity,
    soil_moisture,
    water_consumption,
    recharge,
    scenario
):
    """
    AI-Powered Groundwater Action Advisor V2.

    Converts groundwater prediction and environmental indicators
    into a prioritized, personalized action plan.
    """

    actions = []
    priorities = []

    risk = str(risk_level).lower()
    scarcity = str(scarcity_level).lower()
    scenario_lower = str(scenario).lower()

    # ==========================================================
    # 1. GROUNDWATER RISK
    # ==========================================================

    if risk in ["high", "critical", "severe"]:
        priorities.append("HIGH")

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Household / Community",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Reduce unnecessary groundwater consumption",
            "reason": "The predicted groundwater condition indicates increased groundwater stress."
        })

    elif risk in ["moderate", "medium"]:
        priorities.append("MEDIUM")

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Household",
            "timeline": "Short-term",
            "impact": "Medium",
            "action": "Monitor groundwater usage carefully",
            "reason": "The groundwater condition requires monitoring to prevent further deterioration."
        })

    else:
        priorities.append("LOW")

        actions.append({
            "priority": "🟢 LOW",
            "who": "Household / Community",
            "timeline": "Long-term",
            "impact": "Medium",
            "action": "Continue sustainable groundwater practices",
            "reason": "The current groundwater condition is relatively stable."
        })

    # ==========================================================
    # 2. RAINFALL AND RECHARGE
    # ==========================================================

    if rainfall < 100 or recharge < 30:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Community / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Increase groundwater recharge",
            "reason": "Low rainfall or recharge can reduce natural groundwater replenishment."
        })

    elif rainfall < 200 or recharge < 60:

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Household / Community",
            "timeline": "Short-term",
            "impact": "High",
            "action": "Improve rainwater harvesting and recharge",
            "reason": "Moderate recharge conditions provide an opportunity to improve groundwater replenishment."
        })

    else:

        actions.append({
            "priority": "🟢 LOW",
            "who": "Community",
            "timeline": "Long-term",
            "impact": "Medium",
            "action": "Maintain existing recharge practices",
            "reason": "Current rainfall and recharge conditions are relatively favorable."
        })

    # ==========================================================
    # 3. WATER CONSUMPTION
    # ==========================================================

    if water_consumption > 700:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Household / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Reduce excessive water consumption",
            "reason": "High daily water consumption can increase pressure on groundwater resources."
        })

    elif water_consumption > 500:

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Household",
            "timeline": "Short-term",
            "impact": "Medium",
            "action": "Adopt water conservation practices",
            "reason": "Moderate-to-high water consumption may contribute to groundwater stress."
        })

    # ==========================================================
    # 4. TEMPERATURE
    # ==========================================================

    if temperature > 35:

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Household / Community",
            "timeline": "Short-term",
            "impact": "Medium",
            "action": "Increase water conservation during hot periods",
            "reason": "Higher temperatures can increase water demand and evaporative losses."
        })

    # ==========================================================
    # 5. SOIL MOISTURE
    # ==========================================================

    if soil_moisture < 20:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Community / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Improve soil moisture retention",
            "reason": "Low soil moisture may indicate dry conditions and reduced water availability."
        })

    elif soil_moisture < 40:

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Community",
            "timeline": "Short-term",
            "impact": "Medium",
            "action": "Improve soil moisture conservation",
            "reason": "Moderate soil moisture suggests that additional conservation measures could be beneficial."
        })

    # ==========================================================
    # 6. GROUNDWATER HEALTH INDEX
    # ==========================================================

    if ghi < 40:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Community / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Implement immediate groundwater conservation measures",
            "reason": "The Groundwater Health Index indicates significant groundwater stress."
        })

    elif ghi < 70:

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Community",
            "timeline": "Short-term",
            "impact": "Medium",
            "action": "Improve groundwater sustainability measures",
            "reason": "The Groundwater Health Index indicates that improvement is needed."
        })

    # ==========================================================
    # 7. WATER SCARCITY
    # ==========================================================

    if scarcity in ["high", "critical", "severe"]:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Community / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Prepare a local water conservation plan",
            "reason": "The scarcity analysis indicates increased pressure on available groundwater resources."
        })

    elif scarcity in ["moderate", "medium"]:

        actions.append({
            "priority": "🟡 MEDIUM",
            "who": "Community",
            "timeline": "Short-term",
            "impact": "Medium",
            "action": "Prepare preventive water management measures",
            "reason": "Moderate scarcity indicates that proactive management can help prevent future shortages."
        })

    # ==========================================================
    # 8. SCENARIO-SPECIFIC ADVICE
    # ==========================================================

    if "drought" in scenario_lower:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Community / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Activate drought conservation practices",
            "reason": "The selected drought scenario represents increased pressure on groundwater availability."
        })

    elif "heavy rainfall" in scenario_lower:

        actions.append({
            "priority": "🟢 LOW",
            "who": "Household / Community",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Capture excess rainfall for groundwater recharge",
            "reason": "Heavy rainfall provides an opportunity to improve groundwater recharge and rainwater storage."
        })

    elif "high water consumption" in scenario_lower:

        actions.append({
            "priority": "🔴 HIGH",
            "who": "Household / Institution",
            "timeline": "Immediate",
            "impact": "High",
            "action": "Reduce non-essential water usage",
            "reason": "The selected scenario represents increased demand on groundwater resources."
        })

    elif "improved recharge" in scenario_lower:

        actions.append({
            "priority": "🟢 LOW",
            "who": "Community",
            "timeline": "Long-term",
            "impact": "High",
            "action": "Maintain improved groundwater recharge practices",
            "reason": "Improved recharge can support groundwater recovery when maintained over time."
        })

    # ==========================================================
    # 9. AI ASSESSMENT
    # ==========================================================

    high_count = sum(
        1 for action in actions
        if "🔴 HIGH" in action["priority"]
    )

    medium_count = sum(
        1 for action in actions
        if "🟡 MEDIUM" in action["priority"]
    )

    if high_count >= 3:

        assessment = (
            f"The AI assessment indicates significant groundwater stress. "
            f"The predicted groundwater level is {prediction} m with a "
            f"Groundwater Health Index of {ghi}. Multiple environmental "
            f"and water-demand indicators suggest that immediate conservation "
            f"and recharge measures should be prioritized."
        )

        overall = "🔴 Immediate action recommended"

    elif high_count >= 1 or medium_count >= 2:

        assessment = (
            f"The AI assessment indicates that groundwater conditions require "
            f"preventive management. The predicted groundwater level is "
            f"{prediction} m and the Groundwater Health Index is {ghi}. "
            f"Monitoring consumption and improving recharge can help prevent "
            f"further groundwater stress."
        )

        overall = "🟡 Preventive action recommended"

    else:

        assessment = (
            f"The AI assessment indicates relatively stable groundwater "
            f"conditions. The predicted groundwater level is {prediction} m "
            f"and the Groundwater Health Index is {ghi}. Continuing "
            f"responsible water consumption and recharge practices is recommended."
        )

        overall = "🟢 Sustainable management recommended"

    # ==========================================================
    # 10. EXPECTED IMPACT
    # ==========================================================

    if high_count >= 3:

        expected_impact = (
            "Reducing groundwater demand and improving recharge can help "
            "lower pressure on groundwater resources and improve long-term "
            "water security."
        )

    elif high_count >= 1 or medium_count >= 2:

        expected_impact = (
            "Preventive conservation and recharge measures can help stabilize "
            "groundwater conditions and reduce the risk of future water scarcity."
        )

    else:

        expected_impact = (
            "Maintaining sustainable water-use and recharge practices can help "
            "preserve groundwater availability over time."
        )

    # ==========================================================
    # 11. RETURN ACTION PLAN
    # ==========================================================

    return {
        "overall_status": overall,
        "assessment": assessment,
        "actions": actions,
        "expected_impact": expected_impact,
        "scenario": scenario
    }