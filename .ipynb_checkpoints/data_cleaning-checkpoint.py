import pandas as pd
import numpy as np


def data_clean(df):
    df = pd.read_csv('data/products_full.csv', low_memory=False)
    df.drop(columns=['order_id','customer_id','review_id','seller_id','product_id','order_item_id',
                     'customer_unique_id'], inplace=True)
    df.drop(columns=['Unnamed: 0','review_comment_title','review_creation_date',
                     'payment_value','review_answer_timestamp','review_comment_message',
                     'product_category_name','product_category_name_english',
                     'order_approved_at'], inplace=True)
    df.drop(columns=['order_purchase_timestamp','order_delivered_customer_date',
                     'order_estimated_delivery_date','order_delivered_carrier_date','shipping_limit_date'], inplace=True)
    df = df.dropna()

    df['payment_type'] = df['payment_type'].astype('category')
    df['customer_city'] = df['customer_city'].astype('category')
    df['customer_state'] = df['customer_state'].astype('category')
    df['order_status'] = df['order_status'].astype('category')
    df['seller_city'] = df['seller_city'].astype('category')
    df['seller_state'] = df['seller_state'].astype('category')
       
    df['payment_type'] = df['payment_type'].cat.codes
    df['customer_city'] = df['customer_city'].cat.codes
    df['customer_state'] = df['customer_state'].cat.codes
    df['order_status'] = df['order_status'].cat.codes
    df['seller_city'] = df['seller_city'].cat.codes
    df['seller_state'] = df['seller_state'].cat.codes
    
    df.to_csv('./data/products_final.csv')
    
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
 
