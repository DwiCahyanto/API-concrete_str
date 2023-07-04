from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
from joblib import load
import pandas as pd
import pickle

app = FastAPI()

@app.get("/")
async def root():
    response = {
        "status": 200,
        "messages": "Your Iris API is up!"
    }
    return response

class ConcreteItem(BaseModel):
    Cement: float
    Fly_Ash: float
    Water: float
    Superplasticizer: float
    Coarse_Aggregate: float
    Fine_Aggregate: float
    Age: int


with open('../models/model-yaml-format1.pkl','rb') as f:
    model = pickle.load(f)

@app.post("/conc_predict")
async def scoring_endpoint(item:ConcreteItem):
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    cp = model.predict(df)[0]
    response = {
        "status": 200,
        "prediction": int(cp)
    }
    return response


