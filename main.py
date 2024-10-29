from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/fraud_model.pkl")

# Initialize FastAPI instance with metadata
app = FastAPI(
    title="Fraud Detection API",
    version="0.1.0",
    description="""
    This API provides endpoints for detecting potential credit card fraud using a machine learning model trained with supervised learning techniques.
    Given a set of transaction features, the model predicts whether a transaction is likely fraudulent and provides the probability of fraud.
    """,
    contact={
        "name": "Nafisa Lawal Idris",
        "url": "https://nafisalawalidris.github.io/13/"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
)

# Define the data schema for transaction input
class Transaction(BaseModel):
    """
    Schema for input data. Each transaction record includes
    28 V-features, the transaction amount, and timestamp.
    """
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# Root Endpoint
@app.get("/", summary="Root Endpoint")
def root():
    """
    Welcome message and API overview.
    """
    return {
        "message": "Welcome to the Credit Card Fraud Detection API",
        "details": "Visit '/docs' for a comprehensive overview of available endpoints and to test the API."
    }

# Root Details
@app.get("/api/v0.1.0/root/", tags=["Root"], summary="Root Details")
def read_root_details():
    """
    Detailed root information, including API overview and key endpoints.
    """
    return {
        "overview": "This API offers endpoints for fraud prediction in credit card transactions.",
        "endpoints": [
            {
                "path": "/",
                "description": "Root endpoint providing welcome message and high-level overview."
            },
            {
                "path": "/api/v0.1.0/predict",
                "description": "Predicts fraud likelihood and provides the probability for a given transaction."
            },
        ]
    }

# Create a router for fraud detection
fraud_detection_router = APIRouter()

@fraud_detection_router.post("/predict", summary="Predict Fraud", tags=["Fraud Detection"])
def predict(transaction: Transaction):
    """
    Predicts whether a transaction is likely fraudulent.
    
    - **transaction**: Transaction data, including 28 V-features, transaction amount, and timestamp.
    - Returns:
        - **fraud_prediction** (bool): True if fraud is predicted, False otherwise.
        - **fraud_probability** (float): Probability of fraud (between 0 and 1).
    """
    # Prepare the input data for model prediction
    data = np.array([[ 
        transaction.Time, transaction.V1, transaction.V2, transaction.V3, transaction.V4,
        transaction.V5, transaction.V6, transaction.V7, transaction.V8, transaction.V9,
        transaction.V10, transaction.V11, transaction.V12, transaction.V13, transaction.V14,
        transaction.V15, transaction.V16, transaction.V17, transaction.V18, transaction.V19,
        transaction.V20, transaction.V21, transaction.V22, transaction.V23, transaction.V24,
        transaction.V25, transaction.V26, transaction.V27, transaction.V28, transaction.Amount
    ]])

    # Make a prediction using the trained model
    prediction = model.predict(data)
    fraud_probability = model.predict_proba(data)[0][1]  # Probability of fraud

    # Return the prediction result
    return {
        "fraud_prediction": bool(prediction[0]),  # True for fraud, False otherwise
        "fraud_probability": fraud_probability
    }

# Include the fraud detection router
app.include_router(fraud_detection_router, prefix="/api/v0.1.0", tags=["Fraud Detection"])

