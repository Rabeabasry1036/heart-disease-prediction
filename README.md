# Heart Disease Prediction API

A Machine Learning-based REST API that predicts the presence of heart disease using patient health information. The project uses a Random Forest Classifier, FastAPI, and Docker.

## Project Overview

This project uses a supervised machine learning model to predict whether a person may have heart disease based on 13 input features.

The trained model is integrated with FastAPI to provide prediction results through REST API endpoints. Docker is used to containerize the application for consistent deployment.

## Technologies Used

* Python 3.11
* Pandas
* NumPy
* Scikit-learn
* Joblib
* FastAPI
* Pydantic
* Uvicorn
* Docker
* Docker Compose
* Render (Deployment)

## Dataset

**Dataset:** Heart Disease Dataset
**Source:** Kaggle
**Link:** https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

The dataset contains 13 input features and one target variable.

### Input Features

| Feature  | Description                       |
| -------- | --------------------------------- |
| age      | Age of the patient                |
| sex      | Sex (1 = Male, 0 = Female)        |
| cp       | Chest pain type                   |
| trestbps | Resting blood pressure            |
| chol     | Serum cholesterol                 |
| fbs      | Fasting blood sugar               |
| restecg  | Resting ECG results               |
| thalach  | Maximum heart rate                |
| exang    | Exercise-induced angina           |
| oldpeak  | ST depression                     |
| slope    | Slope of peak exercise ST segment |
| ca       | Number of major vessels           |
| thal     | Thalassemia                       |

**Target Variable:**

* 0 = No Heart Disease
* 1 = Heart Disease

## Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Number of estimators:** 100
* **Train-test split:** 80:20
* **Random state:** 42
* Stratified splitting was used to maintain class distribution.
* Duplicate records were removed before training.

### Model Performance

**Test Accuracy: 75.41%**

The model is intended for educational and research purposes only. It is not a substitute for professional medical diagnosis.

## Project Structure

```text
heart-disease-prediction/
│
├── backend/
│   ├── __init__.py
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── model.py
│   │   └── schemas.py
│   │
│   ├── data/
│   │   └── heart.csv
│   │
│   ├── model/
│   │   └── heart_model.joblib
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── train_model.py
│
├── frontend/
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

## API Endpoints

The application provides the following endpoints:

| Method | Endpoint   | Description                  |
| ------ | ---------- | ---------------------------- |
| GET    | `/`        | Welcome message              |
| GET    | `/health`  | Checks API and model status  |
| GET    | `/info`    | Provides project information |
| POST   | `/predict` | Predicts heart disease       |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rabeabasry1036/heart-disease-prediction.git
```

### 2. Navigate to the project directory

```bash
cd heart-disease-prediction
```

### 3. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -3.11 -m venv .venv

.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r backend/requirements.txt
```

### 5. Run the FastAPI application

```powershell
cd backend

python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

**Swagger API Documentation:**

```text
http://127.0.0.1:8000/docs
```

## Run with Docker

Make sure Docker Desktop is installed and running.

### 1. Build and start the container

From the main project directory, run:

```bash
docker compose up --build
```

### 2. Access the API

**API:**

```text
http://localhost:8000
```

**Swagger Documentation:**

```text
http://localhost:8000/docs
```

**Health Check:**

```text
http://localhost:8000/health
```

### 3. Stop the container

Press `Ctrl + C`, then run:

```bash
docker compose down
```

## Sample Prediction Input

Send the following JSON data to the POST `/predict` endpoint:

```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
```

### Sample Response

```json
{
  "prediction": 1,
  "result": "Heart Disease Detected",
  "probability": 0.69
}
```

The probability represents the model's estimated probability for class 1. It is not a clinical risk estimate.

## Deployment

The application is designed for deployment using Render with Docker.

**Live API:** https://heart-disease-prediction-cxcm.onrender.com

**GitHub Repository:**
https://github.com/Rabeabasry1036/heart-disease-prediction

## Author

**Rabea Basry**

Information & Communication Engineering
Daffodil International University

## Disclaimer

This project is developed for educational and research purposes. The predictions are generated by a machine learning model and must not be used as a replacement for professional medical advice, diagnosis, or treatment.
