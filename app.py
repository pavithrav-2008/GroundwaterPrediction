from scarcity import analyze_scarcity
from scenario import simulate_scenario
import joblib
import streamlit as st
import pandas as pd
import plotly.express as px

from ghi import calculate_ghi
from risk import assess_risk
from recommendation import get_recommendation
from ai_advisor import generate_ai_advice


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AquaPredict",
    page_icon="💧",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("groundwater_dataset.csv")


df = load_data()


# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------

try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"Unable to load model: {e}")
    st.stop()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("📋 Project Details")

st.sidebar.success("Machine Learning Model")
st.sidebar.info("Random Forest Regressor")
st.sidebar.info(f"Dataset: {len(df)} Records")

st.sidebar.markdown("### Features")

st.sidebar.write("""
✔ Rainfall

✔ Temperature

✔ Humidity

✔ Soil Moisture

✔ Previous Groundwater Level

✔ Water Consumption

✔ Groundwater Recharge
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### Decision Support Modules")

st.sidebar.write("""
✅ Groundwater Prediction

✅ Risk Assessment

✅ Groundwater Health Index

✅ Conservation Recommendation

✅ Water Scarcity Analysis

✅ Scenario Simulator

🧠 AI Action Advisor
""")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title(
    "💧 AquaPredict: Machine Learning-Based Smart "
    "Groundwater Monitoring & Decision Support System"
)

st.write("""
This system predicts groundwater levels using Machine Learning
and further analyzes the prediction through intelligent
decision-support modules.
""")

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.header("🌍 Environmental Parameters")

left, right = st.columns(2)


with left:

    rainfall = st.slider(
        "🌧 Rainfall (mm)",
        0,
        500,
        250
    )

    temperature = st.slider(
        "🌡 Temperature (°C)",
        15,
        45,
        30
    )

    humidity = st.slider(
        "💧 Humidity (%)",
        20,
        100,
        60
    )

    soil = st.slider(
        "🌱 Soil Moisture (%)",
        5,
        80,
        40
    )


with right:

    previous = st.slider(
        "💦 Previous Groundwater Level (m)",
        2.0,
        30.0,
        15.0
    )

    water = st.slider(
        "🚰 Water Consumption (L/day)",
        100,
        1000,
        500
    )

    recharge = st.slider(
        "🔄 Groundwater Recharge (mm)",
        0,
        150,
        75
    )


# --------------------------------------------------
# SCENARIO SIMULATOR
# --------------------------------------------------

st.subheader("🧪 Scenario Simulator")

scenario = st.selectbox(
    "Choose a Scenario",
    [
        "Normal",
        "Heavy Rainfall",
        "Drought",
        "High Water Consumption",
        "Improved Recharge"
    ]
)


# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------

predict = st.button(
    "🔍 Predict Groundwater Level",
    use_container_width=True
)


# ==================================================
# PREDICTION
# ==================================================

if predict:

    # --------------------------------------------------
    # APPLY SELECTED SCENARIO
    # --------------------------------------------------

    rainfall, temperature, humidity, soil, previous, water, recharge = simulate_scenario(
        scenario,
        rainfall,
        temperature,
        humidity,
        soil,
        previous,
        water,
        recharge
    )


    # --------------------------------------------------
    # PREPARE MODEL INPUT
    # --------------------------------------------------

    input_data = pd.DataFrame({
        "Rainfall": [rainfall],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Soil_Moisture": [soil],
        "Previous_Groundwater_Level": [previous],
        "Water_Consumption": [water],
        "Groundwater_Recharge": [recharge]
    })


    # --------------------------------------------------
    # PREDICT GROUNDWATER LEVEL
    # --------------------------------------------------

    prediction = model.predict(input_data)[0]

    prediction = round(float(prediction), 2)


    # --------------------------------------------------
    # GROUNDWATER HEALTH INDEX
    # --------------------------------------------------

    ghi, ghi_status, ghi_icon = calculate_ghi(
        prediction,
        rainfall,
        soil,
        recharge,
        water
    )


    # --------------------------------------------------
    # RISK ASSESSMENT
    # --------------------------------------------------

    risk_level, risk_icon, risk_message = assess_risk(
        prediction,
        rainfall,
        recharge
    )


    # --------------------------------------------------
    # CONSERVATION RECOMMENDATIONS
    # --------------------------------------------------

    recommendations = get_recommendation(
        risk_level,
        ghi
    )


    # --------------------------------------------------
    # WATER SCARCITY ANALYSIS
    # --------------------------------------------------

    scarcity_level, scarcity_icon, scarcity_message = analyze_scarcity(
        prediction,
        rainfall,
        recharge
    )


    # ==================================================
    # 🧠 AI ACTION ADVISOR
    # ==================================================

    ai_advice = generate_ai_advice(
        prediction=prediction,
        risk_level=risk_level,
        ghi=ghi,
        scarcity_level=scarcity_level,
        rainfall=rainfall,
        temperature=temperature,
        humidity=humidity,
        soil_moisture=soil,
        water_consumption=water,
        recharge=recharge,
        scenario=scenario
    )


    # ==================================================
    # PREDICTION RESULTS
    # ==================================================

    st.divider()

    st.header("📊 Prediction Results")

    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "Predicted Groundwater Level",
            f"{prediction} m"
        )


    with c2:

        st.metric(
            "Risk Level",
            f"{risk_icon} {risk_level}"
        )


    with c3:

        st.metric(
            "Groundwater Health Index",
            f"{ghi}/100"
        )


    with c4:

        st.metric(
            "Health Status",
            f"{ghi_icon} {ghi_status}"
        )


    # ==================================================
    # WATER SCARCITY ANALYSIS
    # ==================================================

    st.divider()

    st.header("💧 Water Scarcity Analysis")

    s1, s2 = st.columns(2)


    with s1:

        st.metric(
            "Scarcity Level",
            f"{scarcity_icon} {scarcity_level}"
        )


    with s2:

        st.info(scarcity_message)


    # ==================================================
    # CONSERVATION RECOMMENDATIONS
    # ==================================================

    st.divider()

    st.header("💡 Conservation Recommendations")

    st.info(risk_message)

    for recommendation in recommendations:

        st.write(recommendation)


    # ==================================================
    # 🧠 AI-POWERED GROUNDWATER ACTION ADVISOR
    # ==================================================

    st.divider()

    st.header("🧠 AI-Powered Groundwater Action Advisor")

    st.success(
        ai_advice["overall_status"]
    )


    # --------------------------------------------------
    # AI ASSESSMENT
    # --------------------------------------------------

    st.subheader("🔍 AI Assessment")

    st.info(
        ai_advice["assessment"]
    )


    # --------------------------------------------------
    # PERSONALIZED WATER ACTION PLAN
    # --------------------------------------------------

    st.subheader("🎯 Personalized Water Action Plan")


    for i, action in enumerate(
        ai_advice["actions"],
        1
    ):

        priority = action["priority"]


        # --------------------------------------------------
        # ACTION CARD
        # --------------------------------------------------

        with st.container(border=True):

            st.markdown(
                f"### {priority}  {action['action']}"
            )


            # --------------------------------------------------
            # ACTION DETAILS
            # --------------------------------------------------

            a1, a2, a3 = st.columns(3)


            with a1:

                st.markdown(
                    "👤 **Who should act**"
                )

                st.write(
                    action["who"]
                )


            with a2:

                st.markdown(
                    "⏱️ **When to act**"
                )

                st.write(
                    action["timeline"]
                )


            with a3:

                st.markdown(
                    "📈 **Expected impact**"
                )

                st.write(
                    action["impact"]
                )


            # --------------------------------------------------
            # REASON
            # --------------------------------------------------

            st.markdown(
                "🧠 **Why this action?**"
            )

            st.write(
                action["reason"]
            )


    # ==================================================
    # EXPECTED SOCIAL & ENVIRONMENTAL IMPACT
    # ==================================================

    st.subheader(
        "🌱 Expected Social & Environmental Impact"
    )

    st.success(
        ai_advice["expected_impact"]
    )


    # ==================================================
    # SCENARIO INFORMATION
    # ==================================================

    st.caption(
        f"🧪 AI analysis based on the selected scenario: "
        f"{ai_advice['scenario']}"
    )


    # ==================================================
    # DECISION SUPPORT MODULES
    # ==================================================

    st.divider()

    st.header("🧠 Decision Support Modules")

    d1, d2 = st.columns(2)


    with d1:

        st.info("""
        ### 💧 Water Scarcity Analysis

        **Status:** ✅ Implemented

        This module analyzes groundwater availability
        using the predicted groundwater level,
        rainfall and recharge values.

        Current Status:

        - Prediction Module ✅
        - Water Scarcity Analysis ✅
        """)


    with d2:

        st.info(f"""
### 🧪 Scenario Simulator

**Status:** ✅ Implemented

Current Scenario:

**{scenario}**

The simulator modifies environmental
conditions and predicts the impact
on groundwater availability.
""")


    # ==================================================
    # DECISION SUPPORT SUMMARY
    # ==================================================

    st.divider()

    st.subheader("📋 Decision Support Summary")


    summary = pd.DataFrame({

        "Module": [

            "Groundwater Prediction",

            "Risk Assessment",

            "Groundwater Health Index",

            "Recommendation Engine",

            "Water Scarcity Analysis",

            "Scenario Simulator",

            "AI Action Advisor"
        ],


        "Status": [

            "✅ Implemented",

            "✅ Implemented",

            "✅ Implemented",

            "✅ Implemented",

            "✅ Implemented",

            "✅ Implemented",

            "✅ Implemented"
        ]

    })


    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )


# ==================================================
# DATASET PREVIEW
# ==================================================

st.divider()

st.header("📄 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)


# ==================================================
# DATASET STATISTICS
# ==================================================

st.divider()

st.header("📊 Dataset Statistics")

a, b, c = st.columns(3)


a.metric(
    "Total Records",
    len(df)
)


b.metric(
    "Input Features",
    len(df.columns) - 1
)


c.metric(
    "Target Variable",
    "Groundwater Level"
)


st.subheader("📈 Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)


# ==================================================
# DISTRIBUTION CHART
# ==================================================

st.divider()

st.header("📊 Groundwater Level Distribution")


fig = px.histogram(
    df,
    x="Groundwater_Level",
    nbins=30,
    color_discrete_sequence=["royalblue"],
    title="Distribution of Groundwater Levels"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ==================================================
# RAINFALL VS GROUNDWATER
# ==================================================

st.divider()

st.header("🌧 Rainfall vs Groundwater Level")


scatter = px.scatter(
    df,
    x="Rainfall",
    y="Groundwater_Level",
    color="Groundwater_Level",
    size="Groundwater_Level",
    title="Rainfall vs Groundwater Level"
)


st.plotly_chart(
    scatter,
    use_container_width=True
)


# ==================================================
# CORRELATION HEATMAP
# ==================================================

st.divider()

st.header("🔥 Correlation Heatmap")


corr = df.corr(
    numeric_only=True
)


heatmap = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Blues",
    title="Feature Correlation Matrix"
)


st.plotly_chart(
    heatmap,
    use_container_width=True
)


# ==================================================
# FEATURE ANALYSIS
# ==================================================

st.divider()

st.header("📌 Feature Analysis")


tab1, tab2 = st.tabs(
    ["Dataset", "Correlation"]
)


with tab1:

    st.dataframe(
        df.head(20),
        use_container_width=True
    )


with tab2:

    st.dataframe(
        corr.round(2),
        use_container_width=True
    )


# ==================================================
# MODEL INSIGHTS
# ==================================================

st.divider()

st.header("🧠 Model Insights")


st.success("""
### Key Observations

• Higher rainfall generally improves groundwater recharge.

• Higher soil moisture positively influences groundwater availability.

• Excessive water consumption reduces groundwater levels.

• High temperatures negatively affect groundwater sustainability.

• Groundwater recharge contributes significantly to groundwater recovery.

• Decision-support modules assist users in understanding groundwater health and conservation needs.
""")


# ==================================================
# ABOUT PROJECT
# ==================================================

st.divider()

st.header("ℹ️ About AquaPredict")


st.write("""
**AquaPredict** is a Machine Learning-based groundwater monitoring and decision-support system.

The application predicts groundwater levels using environmental parameters and then analyzes the prediction using intelligent decision-support modules.

### Implemented Modules

- ✅ Groundwater Prediction
- ✅ Risk Assessment
- ✅ Groundwater Health Index (GHI)
- ✅ Conservation Recommendation Engine
- ✅ Water Scarcity Analysis
- ✅ Scenario Simulator
- 🧠 AI-Powered Groundwater Action Advisor

The AI Action Advisor analyzes the predicted groundwater condition,
environmental indicators and water demand to generate a prioritized
water-management action plan.
""")


# ==================================================
# FUTURE WORK
# ==================================================

st.divider()

st.header("🚀 Future Enhancements")


future = pd.DataFrame({

    "Future Module": [

        "Real-Time Weather API",

        "IoT Sensor Integration",

        "GIS-Based Groundwater Mapping",

        "Advanced Water Scarcity Analysis",

        "Mobile Application"
    ],


    "Status": [

        "Planned",

        "Planned",

        "Planned",

        "Research",

        "Future Scope"
    ]

})


st.dataframe(
    future,
    hide_index=True,
    use_container_width=True
)


# ==================================================
# FOOTER
# ==================================================

st.divider()


st.markdown(
    """
<div style="text-align:center">

## 💧 AquaPredict

### Machine Learning-Based Smart Groundwater Monitoring & Decision Support System

**Technology Stack**

Python • Streamlit • Pandas • Plotly • Scikit-Learn

**Implemented Modules**

Groundwater Prediction • Risk Assessment • Groundwater Health Index • Recommendation Engine • Water Scarcity Analysis • Scenario Simulator • AI Action Advisor

---

Developed for Smart Water Resource Management

</div>
""",
    unsafe_allow_html=True
)
