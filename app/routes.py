from fastapi import APIRouter
from pathlib import Path
import pandas as pd
import joblib

from app.utils import preprocessing
from app.schemas import EmployeeTurnover, EmployeeData

# load dataset
DATA_PATH = Path("csv")
df = pd.read_csv(DATA_PATH / "HR_capstone_dataset.csv")

# load model
MODEL_PATH = Path("models")

router = APIRouter(prefix="/turnover", tags=["Turnover Prediction"])
@router.get("")
def read_data():
    return df.to_dict(orient="records")

# get prediction
@router.post("/predict", response_model=EmployeeTurnover)
def predict(payload: EmployeeData):
    predictor = pd.DataFrame(payload.model_dump(), index = [0])
    processed_predictor = preprocessing(predictor)
    rf_opt = joblib.load(MODEL_PATH / "rf_opt.joblib")
    prediction = rf_opt.predict(processed_predictor)

    return {"left": int(prediction[0])}