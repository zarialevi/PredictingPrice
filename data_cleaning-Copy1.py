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


    