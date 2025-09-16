# fastapi_churn_api.py
# API sencilla para exponer un pipeline de sklearn

import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

class CustomerData(BaseModel):
    age: float
    gender: str
    tenure: float
    usage_frequency: float
    support_calls: float
    payment_delay: float
    subscription_type: str
    contract_length: str
    total_spend: float
    last_interaction: float

model_path = 'modelo_churn.joblib'
app = FastAPI(title='Churn prediction API')

model = joblib.load(model_path)

@app.post('/')
def welcome():
    return {"message": "API arriba. Usa POST /predict/ para predicciones."}

@app.post('/predict/')
def model_prediction(payload: CustomerData):
    df = pd.DataFrame.from_dict(payload.model_dump(),orient='index').T
    print(df)
    print(df.columns)

    rename_map = {
        'age': 'Age',
        'gender': 'Gender',
        'tenure': 'Tenure',
        'usage_frequency': 'Usage Frequency',
        'support_calls': 'Support Calls',
        'payment_delay': 'Payment Delay',
        'subscription_type': 'Subscription Type',
        'contract_length': 'Contract Length',
        'total_spend': 'Total Spend',
        'last_interaction': 'Last Interaction'
    }
    df = df.rename(columns=rename_map)

    prediction = int(model.predict(df)[0])

    return {
    "msg":prediction
    }

