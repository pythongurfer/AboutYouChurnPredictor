# scripts/train.py
import pandas as pd
import mlflow
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

# --- Define a consistent tracking URI ---
TRACKING_URI = os.path.abspath("mlruns")
mlflow.set_tracking_uri(f"file://{TRACKING_URI}")

mlflow.set_experiment("churn_prediction")

print(f"MLflow tracking to: {mlflow.get_tracking_uri()}")

with mlflow.start_run() as run:
    # --- 1. Load Data ---
    df = pd.read_csv("data/customer_data.csv")

    # --- 2. Preprocessing ---
    df_processed = df.drop("customer_id", axis=1)
    
    # IMPORTANT FIX: Ensure one-hot encoding creates integers (0/1) instead of booleans (True/False)
    df_processed = pd.get_dummies(df_processed, columns=['gender'], drop_first=True, dtype=int)

    # --- 3. Feature and Target Split ---
    X = df_processed.drop("churn", axis=1)
    y = df_processed["churn"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- 4. Model Training ---
    n_estimators = 150
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("random_state", 42)
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)

    # --- 5. Evaluation & Logging ---
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    mlflow.log_metric("accuracy", accuracy)

    # --- 6. Log Model with Signature ---
    input_example = X_train.head(5)
    signature = infer_signature(input_example, preds)
    mlflow.sklearn.log_model(
        sk_model=model, 
        artifact_path="churn_model", 
        signature=signature,
        input_example=input_example,
        registered_model_name="ChurnRF"
    )
    
    print(f"Run ID: {run.info.run_id}")
    print(f"Accuracy: {accuracy:.4f}")
    print("Model logged successfully with an INTEGER-based signature!")