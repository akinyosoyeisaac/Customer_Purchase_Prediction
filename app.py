"""
This script containers code that can help end users interact with the model such that they can easily run a prediction with their own raw data.

In building the app, fastapi was used and uvicorn was used for the server side
"""

#importing necessary libraries
import pickle as pk
import pandas as pd
from fastapi import FastAPI, Form
from feature_engineering import wrangling_test

# initializing the app
app = FastAPI()

# loading the model into the script
with open(r"final_model.pk", "rb") as file:
    model = pk.load(file)


# Building the path to our home page
@app.get("/")
async def home():
    """
    The home page just returns a string given the user an introduction as to the function of the app
    """
    return {"predict": "Customer Purchase Prediction"}


# Building the path to the prediction page
@app.post("/predict")
async def prediction(id: int = Form(1), created_at: str = Form(regex=r"[0-9]{4,}-[0-9]{1,2}-[0-9]{1,2}", description="YYYY-MM-DD"), campaign_var_1: int = Form(..., ge=0), campaign_var_2: int = Form(..., ge=0), products_purchased: int = Form(..., ge=0), signup_date: str = Form(regex=r"[0-9]{4,}-[0-9]{1,2}-[0-9]{1,2}", description="YYYY-MM-DD"), user_activity_var_1: int = Form(0, ge=0, le=1), user_activity_var_2: int = Form(0, ge=0, le=1), user_activity_var_3: int = Form(0, ge=0, le=1), user_activity_var_4: int = Form(0, ge=0, le=1), user_activity_var_5: int = Form(0, ge=0, le=1), user_activity_var_6: int = Form(0, ge=0, le=1), user_activity_var_7: int = Form(0, ge=0, le=1), user_activity_var_8: int = Form(0, ge=0, le=1), user_activity_var_9: int = Form(0, ge=0, le=1), user_activity_var_10: int = Form(0, ge=0, le=1), user_activity_var_11: int = Form(0, ge=0, le=1), user_activity_var_12: int = Form(0, ge=0, le=1)):

    """
    Using the advantage of Form provided by the fastapi module to collected the data need for the prediction.
    Also the data to be collected has been rap around different data validation like the data type expected from the user of the app. The format in which the date are expected to be provided and other related condition.
    In the workflow all inputs are collated as a dictionary using the variable name features. This is immediately followed by converting the features into a form that is acceptable by our model which the pandas dataframe using the variable data, the data is passed to our wraggling funtion which can be found in the feature engineering script.
    The predicted value is store as predicted value and the final output is store as prediction
    """

    # features to be used to create dataframe object
    features = dict([("id", id), ("created_at", created_at), ("campaign_var_1", campaign_var_1), ("campaign_var_2", campaign_var_2), ("products_purchased", products_purchased), ("signup_date", signup_date), ("user_activity_var_1", user_activity_var_1), ("user_activity_var_2", user_activity_var_2), ("user_activity_var_3", user_activity_var_3), ("user_activity_var_4", user_activity_var_4), ("user_activity_var_5", user_activity_var_5), ("user_activity_var_6", user_activity_var_6), ("user_activity_var_7", user_activity_var_7), ("user_activity_var_8", user_activity_var_8), ("user_activity_var_9", user_activity_var_9), ("user_activity_var_10", user_activity_var_10), ("user_activity_var_11", user_activity_var_11), ("user_activity_var_12", user_activity_var_12)])

    # Dataframe object of the raw data
    data = pd.DataFrame(data = [features.values()], columns=features.keys())
    
    # preprocessed dataframe object
    data = wrangling_test(data)
    
    # Generating prediction from our model
    predicted_value = model.predict(data)[0]
    
    # Generating our prediction in a human readable format
    if predicted_value == 0:
        prediction = "Item not bought"
    else:
        prediction = "Item not bought"
    return {"prediction": prediction}