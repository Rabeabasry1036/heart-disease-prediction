import joblib
import pandas as pd

from pathlib import Path


# Define the trained model path
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "heart_model.joblib"


# Load the trained model
def load_model():

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found at: {MODEL_PATH}"
        )

    model = joblib.load(MODEL_PATH)

    return model


# Make heart disease prediction
def predict_heart_disease(model, input_data):

    # Convert input data into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Ensure correct feature order
    feature_names = [
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ]

    input_df = input_df[feature_names]

    # Predict result
    prediction = int(model.predict(input_df)[0])

    # Get prediction probability
    probabilities = model.predict_proba(input_df)[0]

    probability = float(probabilities[1])

    return prediction, probability