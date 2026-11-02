from pydantic import BaseModel, Field


class HeartDiseaseInput(BaseModel):

    age: int = Field(..., gt=0, description="Age of the patient")

    sex: int = Field(..., ge=0, le=1, description="Sex (1 = Male, 0 = Female)")

    cp: int = Field(..., ge=0, le=3, description="Chest pain type")

    trestbps: int = Field(..., gt=0, description="Resting blood pressure")

    chol: int = Field(..., gt=0, description="Serum cholesterol")

    fbs: int = Field(..., ge=0, le=1, description="Fasting blood sugar")

    restecg: int = Field(..., ge=0, le=2, description="Resting ECG results")

    thalach: int = Field(..., gt=0, description="Maximum heart rate")

    exang: int = Field(..., ge=0, le=1, description="Exercise induced angina")

    oldpeak: float = Field(..., ge=0, description="ST depression")

    slope: int = Field(..., ge=0, le=2, description="Slope of peak exercise ST segment")

    ca: int = Field(..., ge=0, description="Number of major vessels")

    thal: int = Field(..., ge=0, description="Thalassemia")


class HeartDiseaseResponse(BaseModel):

    prediction: int
    result: str
    probability: float