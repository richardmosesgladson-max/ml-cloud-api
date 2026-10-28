
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from model import predict_price

app = FastAPI(
    title="ML Prediction API",
    description="A house price prediction service",
    version="1.0.0"
)


class HouseInput(BaseModel):
    size: float = Field(gt=0, description="House size; must be positive")


@app.get("/")
def home():
    return {"message": "ML Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: HouseInput):
    try:
        price = predict_price(data.size)

        return {
            "size": data.size,
            "predicted_price_lakhs": float(price)
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Check the model and server logs."
        ) from exc
