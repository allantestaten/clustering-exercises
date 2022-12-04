import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from env import get_db_url



#Define a query for the mall dataset
sql_query = '''
             SELECT *
             FROM customers
             '''

#Read in the dataset
mall_df = pd.read_sql(sql_query, get_db_url('mall_customers'))

#Visualize distribution of target variable
plt.hist(mall_df['spending_score'])

#Descriptive statistics of numerical columns
mall_df.describe().T

# null count
mall_df.isna().sum()

#See the quantiles for age
mall_df['age'].quantile([0.25, 0.75])

#Store the quantiles in variables
age_q1, age_q3 = mall_df['age'].quantile([0.25, 0.75])

#Calculate the IQR
age_iqr = age_q3 - age_q1

age_iqr


#Calculate upper and lower bounds based on a k value of 1.5
age_upper = age_q3 + (age_iqr * 1.5)
age_lower = age_q1 - (age_iqr * 1.5)

age_upper, age_lower


#Check for outliers in the age column
mall_df[mall_df['age'] > age_upper]

#Split my data into three subsets
seed = 42

mall_train, test_val = train_test_split(mall_df, train_size=0.7,
                                   random_state=seed)

mall_test, mall_val = train_test_split(test_val, train_size=0.5,
                                       random_state=seed)

mall_train.shape, mall_val.shape, mall_test.shape


#Check get_dummies works as expected on my training data
pd.get_dummies(mall_train)


#Create the dataframe with dummies for gender and drop redundant column
mall_train = pd.get_dummies(mall_train)

mall_train.drop(columns=['gender_Male'], inplace=True)

mall_train.head()

#Check for missing values
mall_train.info()

#Initialize the scaler and fit/transform a couple columns in my training data
mms = MinMaxScaler()

mall_train[['age', 'annual_income']] = mms.fit_transform(mall_train[['age',
                                                                     'annual_income']])

mall_train.head()