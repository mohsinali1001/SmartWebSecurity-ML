from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle
from pathlib import Path

app = FastAPI(title="DigitalAxis ML Model Service")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
MODEL_PATH = Path(__file__).parent / "model" / "pipe.pkl"
model = None

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print(f"✅ Model loaded from {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error loading model: {e}")


# Input schema
class IncomingData(BaseModel):
    network_packet_size: float
    protocol_type: str
    login_attempts: int
    session_duration: float
    encryption_used: str
    ip_reputation_score: float
    failed_logins: int
    browser_type: str
    unusual_time_access: int


@app.get("/")
def root():
    return {
        "message": "DigitalAxis ML Model Service",
        "model_loaded": model is not None
    }


@app.post("/predict")
def predict(data: IncomingData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    try:
        # IMPORTANT: Use DataFrame with column names
        input_df = pd.DataFrame([data.dict()])

        prediction = model.predict(input_df)[0]

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_df)[0][1]
        else:
            probability = 0.5

        attack_detected = bool(prediction == 1)

        return {
            "prediction": int(prediction),
            "probability": float(probability),
            "attack_detected": attack_detected,
            "locked_state": attack_detected
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }
