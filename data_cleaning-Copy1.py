import pandas as pd
import numpy as np


def get_df():
    useful = ['order_delivered_customer_date','order_estimated_delivery_date',
         'payment_type','payment_value','review_id','review_score','customer_city','customer_state','price','freight_value','product_name_lenght','product_description_lenght','product_photos_qty',
         'product_weight_g','product_length_cm','product_height_cm','product_width_cm','product_category_name_english']

    df_all = pd.read_csv('data/products_full.csv')
    df1 = pd.DataFrame(df_all, columns=useful)
    df.drop(columns='Unnamed: 0')
    df1.dropna(inplace=True)
    df1.to_csv('./data/products_new.csv', index=True)

def products_df():
    df = pd.read_csv('./data/products.csv')
    return df
    

def con_df():
    df = pd.read_csv('./data/products.csv')
    cont_features = []

    for colname, coltype in df.dtypes.iteritems():
        if coltype in [np.float64, np.int64]:
            cont_features.append(colname)

    cont = pd.DataFrame(df, columns=cont_features)
    return cont
    

def cat_df():
    df = pd.read_csv('./data/products.csv')
    cat_features = []

    for colname, coltype in df.dtypes.iteritems():
        if coltype in [np.object]:
            cat_features.append(colname)

    cat = pd.DataFrame(df, columns=cat_features)
    return cat

def clean_columns(df):
    df=df.rename(columns={'review_score':'Review_Score', 'price':'Price_$','freight_value':"Shipping_Cost", 'product_name_lenght':"Product_Name_Length",
           'product_description_lenght':'Product_Description_Length', 'product_photos_qty':'Product_Photos_Qty', 'product_weight_g':'Product_Weight_g',
           'product_length_cm':'Product_Length_cm', 'product_height_cm':'Product_Height_cm', 'product_width_cm':'Product_Width_cm'})
    
    df["Product_Area_cm2"]=df['Product_Length_cm']*df['Product_Width_cm']

    df["Product_Photos_Qty"].astype('int64')
    df["Product_Description_Length"].astype('int64')
    df["Product_Name_Length"].astype('int64')
    df["Review_Score"].astype('int64')

    new_df=df.drop(columns=['Product_Length_cm','Product_Width_cm'])
    
    return new_df
 
    
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score    


def cross_validate(k, X_train, y_train):
    
    mse_results = cross_val_score(linreg, X_train_imputed_scaled, y_train, folds=k, scoring='neg_mean_squared_error')
    r2_results = cross_val_score(linreg, X_train_imputed_scaled, y_train, folds=k, scoring='r2')
    return(print(f"After cross-validating the data for {k}-folds: \nMean Squared Errors: {mse_results}  \nR2: {r2_results}"))
    