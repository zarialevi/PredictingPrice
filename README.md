# E-Commerce Price Predictions
Greg Simon & Zaria Rankine

## Introduction
We have used E-Commerce data from Olist Store -  Brazils largest department store - to predict sale prices. 

### Dataset
We have data on over 100,000 orders from 2016 - 2018, order details from all Olist Stores partner Marketplaces, anonymized for confidentiality.

### The aim
In this project we wanted to understand the biggest influences on the price of orders made through Olist Store.
Through various models fit to the data, we try to see the impact of each chosen feature.
This consisted of many feature such as product name length (as listed on the website), the city and state of the seller as well as
the city and state the order was being shipped to, review score etc.
From the model we get the effect size of each of these features (coefficients) and draw our conclusions
so we can say what aspects the business should focus on.

### Impact
The different models run can eliminate or select variables which fit the data better and therefore have
the strongest effect on prices.
From this, data can be input into our  model and the most influential variables on the dependent variable
chosen (in this case price) will be computed.
This allows the user to choose where to focus their business model dependant on which variable is storngest.
For example, we found that a longer product title would result in cheaper order price, and so we concluded
that a shorter title would sell more.

### Summary of Repository Files

- data_cleaning.py
This consists of various functions to read in and clean data.

- README.md  
This file!

- FinalNotebook.ipynb  
Our notebook which should run, read in and clean the data using our py files, fit  all the models and
return our R^2 value for each model. Cross-validation is performed to account for random sampling in
the training data set.

- Final_E-Commerce in Brazil__How to Improve your Marketplace.pdf
The accompanying presentation.

- Models.py
Functions which run each model in the FinalNotebook.pyfile.

- README_outlines.md
The goals and aims for this project.
