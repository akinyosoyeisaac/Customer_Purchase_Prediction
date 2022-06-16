import pickle as pk
import numpy as np
import pandas as pd
from fastapi import FastAPI, Form
from feature_engineering import wrangling_test

app = FastAPI()

with open(r"final_model.pk", "rb") as file:
    model = pk.load(file)



@app.get("/")
async def home():
    return {"predict": "Customer Purchase Prediction"}

@app.post("/predict")
async def prediction(id: int = Form(1), created_at: str = Form(regex=r"[0-9]{4,}-[0-9]{1,2}-[0-9]{1,2}", description="YYYY-MM-DD"), campaign_var_1: int = Form(..., ge=0), campaign_var_2: int = Form(..., ge=0), products_purchased: int = Form(..., ge=0), signup_date: str = Form(regex=r"[0-9]{4,}-[0-9]{1,2}-[0-9]{1,2}", description="YYYY-MM-DD"), user_activity_var_1: int = Form(0, ge=0, le=1), user_activity_var_2: int = Form(0, ge=0, le=1), user_activity_var_3: int = Form(0, ge=0, le=1), user_activity_var_4: int = Form(0, ge=0, le=1), user_activity_var_5: int = Form(0, ge=0, le=1), user_activity_var_6: int = Form(0, ge=0, le=1), user_activity_var_7: int = Form(0, ge=0, le=1), user_activity_var_8: int = Form(0, ge=0, le=1), user_activity_var_9: int = Form(0, ge=0, le=1), user_activity_var_10: int = Form(0, ge=0, le=1), user_activity_var_11: int = Form(0, ge=0, le=1), user_activity_var_12: int = Form(0, ge=0, le=1)):

    features = dict([("id", id), ("created_at", created_at), ("campaign_var_1", campaign_var_1), ("campaign_var_2", campaign_var_2), ("products_purchased", products_purchased), ("signup_date", signup_date), ("user_activity_var_1", user_activity_var_1), ("user_activity_var_2", user_activity_var_2), ("user_activity_var_3", user_activity_var_3), ("user_activity_var_4", user_activity_var_4), ("user_activity_var_5", user_activity_var_5), ("user_activity_var_6", user_activity_var_6), ("user_activity_var_7", user_activity_var_7), ("user_activity_var_8", user_activity_var_8), ("user_activity_var_9", user_activity_var_9), ("user_activity_var_10", user_activity_var_10), ("user_activity_var_11", user_activity_var_11), ("user_activity_var_12", user_activity_var_12)])

    data = pd.DataFrame(data = [features.values()], columns=features.keys())
    
    data = wrangling_test(data)
    
    predicted_value = model.predict(data)[0]
    
    if predicted_value == 0:
        prediction = "Item not bought"
    else:
        prediction = "Item not bought"
    return {"prediction": prediction}