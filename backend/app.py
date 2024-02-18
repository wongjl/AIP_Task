#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: wjinglun
"""

from fastapi import FastAPI
from model.model import Model
from pydantic import BaseModel
#import pytesseract


# pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Define a question answer item for FastAPI to do checks on the inputs
class QAItem(BaseModel):
    image_url: str
    question: str

# Initailise FastAPI
app = FastAPI()

# Initalise transformer pipeline model
model = Model()

@app.post('/predict')
async def predict(payload: QAItem):
    payload = payload.dict()
    return model.predict_answer(payload['image_url'], payload['question'])
