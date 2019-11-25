import pandas as pd
import numpy as np

def get_data():
    data = pd.read_csv('query.csv')
    data1 = pd.read_csv('query(1).csv')
    data2 = pd.read_csv('query(2).csv')
    data3 = pd.read_csv('query(3).csv')
    df = pd.concat([data,data1,data2,data3])
    df.to_csv('earthquakes_raw.csv')
    

