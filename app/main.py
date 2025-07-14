# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow
import os

# --- Define the EXACT SAME tracking URI as in the training script ---
TRACKING_URI = os.path.abspath("mlruns")
mlflow.set_tracking_uri(f"file://{TRACKING_URI}")

# --- 1. Define the input data schema for the API request ---
class CustomerFeatures(BaseModel):
    tenure_months: int
    gender: str
    sessions_last_30d: int
    avg_session_duration_min: float
    items_in_wishlist: int
    items_in_cart: int
    days_since_last_purchase: int
    total_purchases: int
    total_spend_eur: float
    returns_last_90d: int
    used_promo_code: int
    app_user: int
    newsletter_subscriber: int

# --- 2. Load the production model using the alias syntax ---
# This line will now work because the tracking URI is set correctly.
logged_model_uri = "models:/ChurnRF@production"
loaded_model = mlflow.pyfunc.load_model(logged_model_uri)

# Get the expected feature names and order from the model's signature.
model_features = loaded_model.metadata.get_input_schema().input_names()

app = FastAPI(title="Churn Prediction API")

@app.post("/predict")
def predict_churn(features: CustomerFeatures):
    """
    Receives customer data, preprocesses it to match the training format,
    and returns a churn prediction.
    """
    # --- 3. Preprocess the input to match the model's training data ---
    input_df = pd.DataFrame([features.dict()])
    input_df['gender_Male'] = (input_df['gender'] == 'Male').astype(int)
    input_df['gender_Non-binary'] = (input_df['gender'] == 'Non-binary').astype(int)
    input_df = input_df.drop('gender', axis=1)
    final_df = input_df.reindex(columns=model_features, fill_value=0)

    # --- 4. Make the prediction ---
    prediction = loaded_model.predict(final_df)

    return {"churn_prediction": int(prediction[0])}

