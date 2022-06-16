import pandas as pd
import numpy as np
# Wrangling function for our test data which is an extract of the wrangling for the train data
def wrangling_test(df):
    df = df
    df = df.set_index("id")
    # Summing all the user activity
    user_activity_col = [x for x in df.columns if x.startswith("user")]
    df["sum_user_activities"] = np.sum([df[x] for x in user_activity_col], 0)
    
    # Making the date columns usable for our model
    df["created_at"] = pd.to_datetime(df["created_at"], format="%Y-%m-%d")
    df["signup_date"] = pd.to_datetime(df["signup_date"], format="%Y-%m-%d")
    day = df["created_at"] - df["signup_date"]
    day = day.replace({np.nan:day.max()})
    day = day.astype('str').str.split(" ", expand=True)[0]
    day["day"] = np.abs(day.astype('int'))
    
    # Summing the campaign vars in the data
    camp_col = [x for x in df.columns if x.startswith("camp")]
    df["sum_camp"] = np.sum([df[x] for x in camp_col], 0)
    
    # imputting missing value
    df["products_purchased"] = df["products_purchased"].fillna(0)
    
    # Removing unwanted columns
    df.drop(columns = camp_col + ["created_at", "signup_date"] + user_activity_col, inplace=True)
    return df