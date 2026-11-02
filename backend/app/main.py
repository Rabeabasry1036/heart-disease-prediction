from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request

from app.model import load_model, predict_heart_disease
from app.schemas import HeartDiseaseInput, HeartDiseaseResponse


# Load the trained model when the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.model = load_model()

    print("Heart Disease Prediction Model Loaded Successfully!")

    yield

    print("Application shutting down...")


# Create FastAPI application
app = FastAPI(
    title="Heart Disease Prediction API",
    description="An API for predicting heart disease using Machine Learning.",
    version="1.0.0",
    lifespan=lifespan
)


# Home endpoint
@app.get("/")
def home():

    return {
        "message": "Welcome to Heart Disease Prediction API",
        "documentation": "/docs"
    }


# Health check endpoint
@app.get("/health")
def health_check(request: Request):

    model_loaded = hasattr(request.app.state, "model")

    return {
        "status": "healthy" if model_loaded else "unhealthy",
        "model_loaded": model_loaded
    }


# API information endpoint
@app.get("/info")
def get_info():

    return {
        "project": "Heart Disease Prediction",
        "model": "Random Forest Classifier",
        "version": "1.0.0",
        "features": [
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
    }


# Heart disease prediction endpoint
@app.post("/predict", response_model=HeartDiseaseResponse)
def predict(
    input_data: HeartDiseaseInput,
    request: Request
):

    try:

        # Get the loaded model
        model = request.app.state.model

        # Convert input data into dictionary
        input_dict = input_data.model_dump()

        # Make prediction
        prediction, probability = predict_heart_disease(
            model,
            input_dict
        )

        # Prepare prediction result
        result = (
            "Heart Disease Detected"
            if prediction == 1
            else "No Heart Disease Detected"
        )

        return HeartDiseaseResponse(
            heart_disease=bool(prediction == 1),
            prediction=prediction,
            result=result,
            probability=round(probability, 4)
        )
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )