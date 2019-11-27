import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

import data_cleaning as dc
from sklearn import metrics

from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
import scipy.stats as stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_squared_log_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

    

def cont_model(df, feat_col):
      
    cat_features = ['seller_state','payment_type','customer_city','customer_state','order_status']

    cont_features = []
    for x in df.columns:
        if x not in cat_features:
            cont_features.append(x)
    
    features = [col for col in df.columns if col != feat_col]
    X = df.loc[:, features]
    y = df.loc[:, feat_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)

    #Create X test and X train from continuous variables
    X_train_cont = X_train.loc[:, cont_features]
    X_test_cont = X_test.loc[:, cont_features]
    
    # Impute missing values with median using Imputer from sklearn.preprocessing
    impute = Imputer(strategy='median')
    impute.fit(X_train_cont)

    X_train_continuous = impute.transform(X_train_cont)
    X_test_continuous = impute.transform(X_test_cont)

    # Fit the imputed model
    linreg = LinearRegression()
    linreg.fit(X_train_continuous, y_train)
    
    # Scale the train data
    ss = StandardScaler()
    ss.fit(X_train_continuous)
    ss_test = StandardScaler()
    ss_test.fit(X_test_continuous)
    
    X_train_cont_scaled = ss.transform(X_train_continuous)
    X_test_cont_scaled = ss_test.transform(X_test_continuous)

    #Fit the normalized data
    linreg_norm = LinearRegression()
    linreg_norm.fit(X_train_cont_scaled, y_train) 
    linreg_norm_test = LinearRegression()
    linreg_norm_test.fit(X_test_cont_scaled, y_test) 

    print('For our initial model, our values are:')
    print('Training r^2:', linreg_norm.score(X_train_cont_scaled, y_train))
    print('Training MSE:', mean_squared_error(y_train, linreg_norm.predict(X_train_cont_scaled)))
    
    print('And for our testing dataset, our values are:')
    print('Training r^2:', linreg_norm_test.score(X_test_cont_scaled, y_test))
    print('Training MSE:', mean_squared_error(y_test, linreg_norm_test.predict(X_test_cont_scaled)))
    
    return X_train_cont_scaled, y_train, X_test_cont_scaled, y_test, linreg_norm, linreg_norm_test

def RidgeModel(X,Y):
    # Train model setting alpha (lambda) to 0.05
    ridge = Ridge(alpha=0.05, normalize=True)
    #Fit Ridge model to training data
    ridge.fit(X, Y)
    y_predict_ridge = ridge.predict(X)
    # Calculate R^2 and mse
    print('For our improved model, are values are:')
    print('Training r^2:',ridge.score(X, Y))
    print('Training MSE:',mean_squared_error(Y,y_predict_ridge))  
    
def LassoModel(X,Y):
    lasso = Lasso(alpha=0.05, normalize=True)
    lasso.fit(X, Y)
    y_predict_lasso = lasso.predict(X)
    # calculating mse
    print('For our Lasso model, are values are:')
    print('Training MSE:',mean_squared_error(Y,y_predict_lasso))
    print('Training r^2:',lasso.score(X, Y))
    
def ElasticModel(X,Y):
    elastic = ElasticNet(alpha=0.05, l1_ratio=0.5, normalize=False)
    elastic.fit(X,Y)
    y_predict_elastic = elastic.predict(X)
    #calculating mse
    print('For our Elastic model, are values are:')
    print('Training MSE:', mean_squared_error(Y, y_predict_elastic))
    print('Training r^2:', elastic.score(X,Y))
    
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score    


def cross_validate(model, k, X_train, y_train):
    
    mse_result = np.mean(cross_val_score(model, X_train, y_train, cv=k, scoring='neg_mean_squared_error'))
    r2_result = np.mean(cross_val_score(model, X_train, y_train, cv=k, scoring='r2'))
    return(print(f"""After cross-validating the data for {k}-folds: \nThe average Mean Squared Errors: np.mean({mse_result}) 
                 The average R2: {r2_result}\n"""))