import pandas as pd
import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Load dataset
data = pd.read_csv("groundwater.csv")

# Page Config
st.set_page_config(
    page_title="Smart Groundwater Monitoring System",
    page_icon="🌊",
    layout="wide"
)

# Title
st.title("🌊 Smart Groundwater Prediction System")

st.caption(
    "AI-powered water resource monitoring and forecasting"
)

# Description
st.info(
    """
    This system predicts groundwater levels using rainfall,
    temperature, and humidity data. It also provides drought
    risk assessment, sustainability scoring, and future forecasts.
    """
)

# Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Rainfall",
    round(data["Rainfall"].mean(), 2)
)

col2.metric(
    "Avg Temp",
    round(data["Temperature"].mean(), 2)
)

col3.metric(
    "Avg Groundwater",
    round(data["Groundwater_Level"].mean(), 2)
)

col4.metric(
    "Water Health Score",
    "82/100"
)

st.divider()

# Charts Section
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📈 Groundwater Trend")
    st.line_chart(
        data["Groundwater_Level"]
    )

with col_right:
    st.subheader("📊 Groundwater Distribution")
    st.bar_chart(
        data["Groundwater_Level"]
    )

st.divider()

# Prediction Section
st.subheader("🔍 Predict Groundwater Level")

col1, col2, col3 = st.columns(3)

with col1:
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        value=100.0
    )

with col2:
    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0
    )

with col3:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

# Predict Button
if st.button("🚀 Predict Groundwater Level"):

    prediction = model.predict(
        [[rainfall, temperature, humidity]]
    )

    level = prediction[0]

    st.success(
        f"💧 Predicted Groundwater Level: {level:.2f} meters"
    )

    # Groundwater Status
    st.subheader("🌍 Groundwater Status")

    if level < 5:

        st.error("🔴 Critical Groundwater Level")

        status = "Critical"

    elif level < 10:

        st.warning("🟠 Low Groundwater Level")

        status = "Low"

    elif level < 15:

        st.warning("🟡 Moderate Groundwater Level")

        status = "Moderate"

    else:

        st.success("🟢 Healthy Groundwater Level")

        status = "Healthy"

    # Drought Risk
    st.subheader("🚨 Drought Risk Assessment")

    if rainfall < 70 and temperature > 35:

        st.error("🔴 High Drought Risk")

    elif rainfall < 100:

        st.warning("🟠 Medium Drought Risk")

    else:

        st.success("🟢 Low Drought Risk")

    # Sustainability Score
    st.subheader("💧 Sustainability Score")

    score = min(
        100,
        int((level / 20) * 50 + (rainfall / 200) * 50)
    )

    st.metric(
        "Overall Sustainability",
        f"{score}/100"
    )

    progress = min(score, 100)

    st.progress(progress)

    # Future Forecast
    st.subheader("🔮 Future Forecast")

    future_prediction = model.predict(
        [[rainfall + 20, temperature, humidity]]
    )[0]

    st.info(
        f"""
        Expected Groundwater Level if rainfall increases by
        20 mm:

        🌧️ Future Prediction: {future_prediction:.2f} meters
        """
    )

    # Recommendations
    st.subheader("💡 Smart Recommendations")

    if status == "Critical":

        st.error("""
        Recommended Actions:

        • Immediate rainwater harvesting
        • Restrict groundwater extraction
        • Recharge wells and water bodies
        • Emergency water conservation plan
        """)

    elif status == "Low":

        st.warning("""
        Recommended Actions:

        • Promote rainwater harvesting
        • Reduce excessive water usage
        • Monitor groundwater monthly
        • Improve irrigation efficiency
        """)

    elif status == "Moderate":

        st.info("""
        Recommended Actions:

        • Continue groundwater monitoring
        • Encourage sustainable water usage
        • Maintain recharge structures
        """)

    else:

        st.success("""
        Recommended Actions:

        • Maintain current conservation efforts
        • Continue periodic monitoring
        • Promote sustainable groundwater management
        """)

    # Summary
    st.subheader("📋 Prediction Summary")

    st.write(f"**Predicted Groundwater Level:** {level:.2f} m")
    st.write(f"**Groundwater Status:** {status}")
    st.write(f"**Sustainability Score:** {score}/100")
    