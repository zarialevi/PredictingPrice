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
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

def cont_model(df, feat_col):
    
    cont_features = []
    for colname, coltype in df.dtypes.iteritems():
        if coltype in [np.float64, np.int64]:
            cont_features.append(colname)
    
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
    
    X_train_cont_scaled = ss.transform(X_train_continuous)

    #Fit the normalized data
    linreg_norm = LinearRegression()
    linreg_norm.fit(X_train_cont_scaled, y_train)

    print('Training r^2:', linreg_norm.score(X_train_cont_scaled, y_train))
    print('Training MSE:', mean_squared_error(y_train, linreg_norm.predict(X_train_cont_scaled)))
    
    return linreg_norm
    

def cat_model(df, feat_col):
    
    cont_features = []
    for colname, coltype in df.dtypes.iteritems():
        if coltype in [np.float64, np.int64]:
            cont_features.append(colname)
            
    cat_features = []
    for x in df.columns:
        if x not in cont_features:
            cat_features.append(x)
    
    features = [col for col in df.columns if col != feat_col]
    X = df.loc[:, features]
    y = df.loc[:, feat_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)
    
   # Create X_cat which contains only the categorical variables
    X_train_cat = X_train.loc[:, cat_features]
    X_test_cat = X_test.loc[:, cat_features]

    # Impute missing values with median using Imputer from sklearn.preprocessing
    impute = Imputer(strategy='most_frequent')
    impute.fit(X_train_cat)

    X_train_categorical = impute.transform(X_train_cat)
    X_test_categorical = impute.transform(X_test_cat)

    # Fit the model and print R2 and MSE for train and test
    linreg = LinearRegression()
    linreg.fit(X_train_categorical, y_train)
    
    # Scale the train data
    ss = StandardScaler()
    ss.fit(X_train_categorical)
    
    X_train_cat_scaled = ss.transform(X_train_categorical)
    
    #Fit the normalized data
    linreg_norm = LinearRegression()
    linreg_norm.fit(X_train_cat_scaled, y_train)

    print('Training r^2:', linreg_norm.score(X_train_cat_scaled, y_train))
    print('Training MSE:', mean_squared_error(y_train, linreg_norm.predict(X_train_cat_scaled)))
    
    return linreg_norm    
    
    
def full_def(reg1,reg2):
    
    x_cat = pd.DataFrame(reg1)
    
    x_con = pd.DataFrame(reg2)
    
    X_train_all = pd.concat([x_cat,x_con], axis=1)
 