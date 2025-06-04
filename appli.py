import pandas as pd
import numpy as np
from fastapi import FastAPI
import pickle







app = FastAPI()


@app.post('/get_resutls')
def pass_para(a:float,b:float,c:float,d:float):
    with open (r'C:\Users\Dell\coding\pythonPrac\logistic_reg.pkl','rb') as f:
        model_r = pickle.load(f)
    results = model_r.predict([[a,b,c,d]])
    return f'The model result is {results[0]}'