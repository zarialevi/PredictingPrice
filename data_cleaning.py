import pandas as pd
import numpy as np

def get_df():
    useful = ['order_id','customer_id','order_purchase_timestamp','order_delivered_customer_date','order_estimated_delivery_date',
     'payment_type','payment_value','review_id','review_score','review_creation_date','customer_city','customer_state',
     'product_id','seller_id','price','freight_value','product_name_lenght','product_description_lenght','product_photos_qty',
     'product_weight_g','product_length_cm','product_height_cm','product_width_cm','product_category_name_english']
   
    df = pd.read_csv('data/products_full.csv')
    df1 = pd.DataFrame(df, columns=useful)
    df1.dropna(inplace=True)
    df1.to_csv('./data/products.csv', index=True)

def products_df():
    prod_df = pd.read_csv('./data/products.csv')
    retun prod_df
