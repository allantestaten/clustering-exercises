import pandas as pd
import numpy as np
from env import get_db_url
from pathlib import Path 

def new_zillow_data():
    '''
    This function reads the zillow data from the Codeup db into a df.
    '''
    # Create SQL query.
    sql_query = ''' SELECT *
        FROM properties_2017 prop
        JOIN (
            SELECT parcelid, MAX(transactiondate) AS max_transactiondate
            FROM predictions_2017
            GROUP BY parcelid
            ) pred USING(parcelid)
        JOIN predictions_2017 ON pred.parcelid = predictions_2017.parcelid
                          AND pred.max_transactiondate = predictions_2017.transactiondate
        LEFT JOIN airconditioningtype air USING(airconditioningtypeid)
        LEFT JOIN architecturalstyletype arch USING(architecturalstyletypeid)
        LEFT JOIN buildingclasstype build USING(buildingclasstypeid)
        LEFT JOIN heatingorsystemtype heat USING(heatingorsystemtypeid)
        LEFT JOIN propertylandusetype land USING(propertylandusetypeid)
        LEFT JOIN storytype story USING(storytypeid)
        LEFT JOIN typeconstructiontype type USING(typeconstructiontypeid)
        WHERE propertylandusedesc = "Single Family Residential"
            AND transactiondate <= '2017-12-31'
            AND prop.longitude IS NOT NULL
            AND prop.latitude IS NOT NULL'''
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('zillow'))

    # Save data to csv 
    filepath = Path('zillow.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index =False)
    
    return df

def get_zillow_data():
    '''
    This function reads in zillow data from local copy as a df
    '''
        
    # Reads local copy of csv 
    df = pd.read_csv('zillow.csv')

    # renaming column names to more readable format
    df = df.rename(columns = {'bedroomcnt':'beds', 'roomcnt':'total_rooms',
                              'bathroomcnt':'baths', 
                              'calculatedfinishedsquarefeet':'sqft',
                              'taxvaluedollarcnt':'property_value', 
                              'yearbuilt':'year_built',})
    
    return df



