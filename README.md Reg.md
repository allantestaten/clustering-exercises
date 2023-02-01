# Predicting home prices
 
# Project Description
I am taking the opportunity to demonstrate my skills learned in codeup to impress the Zillow Data Science team in hopes of recieving an opportunity to interview for a position at their company. I will build a model to predict values of single unit properties based on Zillow data from 2017. 
 
# Project Goal
* Identify which features are drivers for predicting the value of a single unit property
* Develop and use machine learning model that accurately predict value of properties in 2017.
* Deliver a report that explains what steps were taken and why there were taken.

 
# Initial Thoughts
 
Home value will depend heavily on the bedrooms, bathrooms and square footage of the home. 


# The Plan
 
* Acquire data from Codeup database using mySQL Workbench
 
* Prepare data
   * Created columns representing anticipated drivers that are easy for machine learning model to process
       * beds
       * baths
       * sqft
       * fips
       * property_value
       * total rooms 

 
* Explore data in search of drivers of propety value
   * Answer the following initial questions
       * What is the median home price?
       * What is the mean home price?
       * Is there a signfiicant difference in property value across the three counties?
       * Is there a correlation between square footage and property value?
       * Is there a correlation between the bedrooms and property value?
       * Is there a correlation between the bathrooms and property value?
      
* Develop a Model to predict an accurate value of the property
   * Use drivers supported by statistical test results to build predictive models
   * Evaluate all models on train 
   * Evaluate top models on validate data 
   * Select the best model based on lowest Root Mean Squared Error
   * Evaluate the best model on test data
 
* Draw conclusions
 
# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Beds| Number of bedrooms in the home|
|Baths| Number of bathrooms in the home|
|sqft| The square footage of the home|
|rooms_count| Represents the total number of rooms in the home|
|fips| The county the property is located in Los Angelese County CA, Ventura CA or Orange County CA|

# Steps to Reproduce
1) Clone this repo
2) Acquire the data from mySQL workbench database 
3) Create env file with username, password and codeup host name 
4) Include the function below in your env file
def get_db_url(db, user = username, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
5) Put the data in the file containing the cloned repo
6) Run notebook