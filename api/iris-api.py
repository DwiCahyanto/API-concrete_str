from fastapi import FastAPI
from fastapi import Request
import pickle
import uvicorn

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
# 2. Loading label = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
# 3. predict Model = sepal_length, sepal_width, petal_length, petal_width 


def load_model():
    try: 
        pickle_file = open('model/classifier.pkl', 'rb')
        classifier = pickle.load(pickle_file)
        return classifier
    except Exception as e:
        response = {
            'status':204,
            'messages': str(e)
        }
        return response
    
@app.get('/check')
async def check():
    model = load_model()
    if model['status'] == 204:
        messages = 'Model is not ready to use' + model['messages']
    else:
        messages = 'Model is ready to use'
    return messages

@app.post("/predict")
async def predict(data: Request):

    # load request
    data = await data.json()
    
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']

    model = load_model()
    label = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

    try:
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]]) #[[0]] --> [  [0]  ]  
        response = {
            'status': 200,
            'input': [sepal_length, sepal_width, petal_length, petal_width],
            'prediction': label[prediction[0]]
        }
    except Exception as e:
        response = {
            'status': 204,
            'messages': str(e)
        }
    return response
    
if __name__ == "__main__":
    uvicorn.run("iris-api:app", host = "0.0.0.0", port = 8000)