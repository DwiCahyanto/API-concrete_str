from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
from joblib import load
import pandas as pd
import pickle
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    response = {
        "status": 200,
        "messages": "Your API is up!"
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


with open('model/model-yaml-format1.pkl','rb') as f:
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
    
if __name__ == "__main__":
    uvicorn.run("con_str-api-staging:app", host = "0.0.0.0", port = 8000)

