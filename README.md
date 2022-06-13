# MACHINE LEARNING PREDICTION TO CHECK WHETHER CUSTOMER WILL BUY A PRODUCT OR NOT

## INTRODUCTION

* The focus of this project is to build a machine learning model that can predict whether a customer will purchase a product not.

* The data used for the project was provided by [analyticsvidhya](http://datahack.analyticsvidhya.com/contest/job-a-thon-june-2022/?utm_source=datahack&utm_medium=navbar) which was the data used for their June Job-a-thon

* The data of particular interest because of the value it can provide in helping business make informed decision and to properly categorize their customer base

## METADATA
* The raw data consist of ```39161 rows(observations)``` and ```18 columns(features)```. The feature name are self explanatory and don't require any further note and can be found in [data exploration]().
* The data is class imbalance 
* contain not a number value across two features

## WORKFLOW
> An easy guide in working through this notebook includes
>> 1. [Data exploration](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/data%20exploration.ipynb)
>> 2. [Feature engineering](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/feature%20engineering.ipynb)
>> 3. [Logistic Reg (baseline model)](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/logistic%20reg.ipynb)
>> 5. [RandomForest Model](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/RandomForest%20Model.ipynb)
>> 6. [Xgradient Boost](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/xgradient-boost.ipynb)
>> 7. [Light Gradient Boost](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/light-Gradient-Boost.ipynb)
>> 8. [Stack Model (Final Model)](https://github.com/akinyosoyeisaac/Customer_Purchase_Prediction/blob/main/Stacking.ipynb)

## PERFORMANCE
* The average performance of the model was measure using using the classification report which include precision, recall, f1-score and accuracy
* The performance of all the model is included below
```Logistic Regression Performance```
<img src="img\logistic regression performance.JPG" width="350">

```Random Forest Performance```
<img src="img\random forest performance.JPG" width="350">

```Xgradient Boost Performance```
<img src="img\light gradient boost performance.png" width="350">

```Light Gradient Boost Performance```
<img src="img\light gradient boost performance.JPG" width="350">

```Stacking Performance```
<img src="img\stacking performance.JPG" width="350">


## DEPLOYMENT
* The final model which is the stack of random forest, xgradient boost, light gradient boost will be deployed on heruko


### TOOLS
[![Pandas](http://pandas.pydata.org/doc/)]
[![Numpy](http://numpy.org/doc/stable/)]
[![Sklearn](http://scikit-learn.org/stable/modules/classes.html)]
[![Imblearn](http://imbalanced-learn.org/stable/user_guide.html)]
[![Imblearn](http://matplotlib.org/stable/api/index.html)]
