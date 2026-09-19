import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("groundwater_dataset.csv")

X = df.drop("Groundwater_Level", axis=1)
y = df["Groundwater_Level"]

# Same split for all iterations
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Three actual model iterations
models = {
    "Iteration 1 (Baseline)": RandomForestRegressor(
        n_estimators=50,
        random_state=42
    ),

    "Iteration 2": RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42
    ),

    "Final Approach": RandomForestRegressor(
        n_estimators=200,
        max_depth=12,
        random_state=42
    )
}

results = []

for name, model in models.items():

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred) ** 0.5
    r2 = r2_score(y_test, y_pred)

    results.append([
        name,
        mae,
        rmse,
        r2
    ])

    print("\n" + "=" * 40)
    print(name)
    print("=" * 40)
    print(f"MAE      : {mae:.3f}")
    print(f"RMSE     : {rmse:.3f}")
    print(f"R² Score : {r2:.4f}")

# Save the FINAL model so your app continues using it
final_model = models["Final Approach"]
joblib.dump(final_model, "model.pkl")

print("\n" + "=" * 40)
print("Final model saved successfully!")
print("=" * 40)