from fastapi import FastAPI
from fastapi import Request
import pickle
from joblib import load
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    response = {
        "status": 200,
        "messages": "Your Iris API is up!"
    }
    return response

# =====
# 1. Loading Model
# 2. Loading label = ['Concrete_compressive_strength']
# 3. predict Model = Cement, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age

def load_model():
    try:
        pickle_file = open('../models/model-yaml-format.pkl','rb')
        regression = pickle.load(pickle_file)
        return regression 
        
    except Exception as e:
        response = {
            'status':204,
            'messages': str(e)
        }
        return response

@app.get('/check')
async def check():
    model = load_model()
    return load_model()

# @app.post("/con_predict")
# async def predict(Cement: float, Fly_Ash: float, Water: float, Superplasticizer: float, Coarse_Aggregate: float, Fine_Aggregate: float,  Age:int):
#     model = load_model()
#     label = ['Concrete_compressive_strength']
    
#     try:
#         prediction = model.predict([[Cement, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age]]) #[[0]] --> [  [0]  ]  
#         response = {
#             'status': 200,
#             'input': [Cement, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age],
#             'prediction': label[int(prediction)]
#         }
#     except Exception as e:
#         response = {
#             'status': 204,
#             'messages': str(e)
#         }
#     return response

# @app.post("/conc_predict")
# async def predict(Cement: float, Fly_Ash: float, Water: float, Superplasticizer: float, Coarse_Aggregate: float, Fine_Aggregate: float, Age: float):
#     model = load_model()
#     label = ['Concrete_compressive_strength']
    
#     try:
#         prediction = model.predict([[Cement, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age]])[0][0]
#         response = {
#             'status': 200,
#             'input': [Cement, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age],
#             'prediction': label[int(prediction)]
#         }
#     except Exception as e:
#         response = {
#             'status': 204,
#             'messages': str(e)
#         }
#     return response

# from fastapi import Request
# # Defining the prediction endpoint without data validation
# @app.post('/basic_predict')
# async def basic_predict(request: Request):

#  # Getting the JSON from the body of the request
#  input_data = await request.json()
 
#  # Converting JSON to Pandas DataFrame
#  input_df = pd.DataFrame([input_data])
 
#  # Getting the prediction from the Logistic Regression model
#  pred = model.predict(input_df)[0]
 
#  return pred

import pandas as pd

@app.post("/conc_predict")
async def predict(Cement: float, Fly_Ash: float, Water: float, Superplasticizer: float, Coarse_Aggregate: float, Fine_Aggregate: float, Age: float):
    model = load_model()
    label = ['Concrete_compressive_strength']
    
    try:
        input_data = pd.DataFrame({
            'Cement': [Cement],
            'Fly_Ash': [Fly_Ash],
            'Water': [Water],
            'Superplasticizer': [Superplasticizer],
            'Coarse_Aggregate': [Coarse_Aggregate],
            'Fine_Aggregate': [Fine_Aggregate],
            'Age': [Age]
        })
        prediction = model.predict(input_data)[0][0]
        response = {
            'status': 200,
            'input': input_data.to_dict(orient='records'),
            'prediction': label[prediction]
        }
    except Exception as e:
        response = {
            'status': 204,
            'messages': str(e)
        }
    return response

