from fastapi import FastAPI
import uvicorn
from prediction import *

#Запуск нашего API

app = FastAPI()

@app.get("/ping") #тестовое подключение

def ping():

    return {"message": "pong!"}

@app.get("/predict/{sentence}") #model inference via predict method

def predict_torch(sentence: str):

    pred = predict(sentence)

    return {sentence: str(pred[0][1])}
