from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI(title="AquaPredict API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("../model.pkl")


@app.get("/")
def home():
    return {"message": "AquaPredict API is running"}


@app.post("/predict")
def predict(data: dict):

    input_data = pd.DataFrame({
        "Rainfall": [data["rainfall"]],
        "Temperature": [data["temperature"]],
        "Humidity": [data["humidity"]],
        "Soil_Moisture": [data["soil_moisture"]],
        "Previous_Groundwater_Level": [
            data["previous_groundwater_level"]
        ],
        "Water_Consumption": [data["water_consumption"]],
        "Groundwater_Recharge": [data["groundwater_recharge"]],
    })

    prediction = model.predict(input_data)[0]

    return {
        "predicted_groundwater_level": round(float(prediction), 2)
    }