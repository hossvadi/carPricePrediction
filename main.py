from re import X
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn import metrics

#Read the dataFrame, Data collection and Processing
car_dataset = pd.read_csv('car-dataset.csv')

#see the dimention of the dataset
car_dataset.shape

#See datatype ofall attributes
car_dataset.info()

# Find ther number of null values 
car_dataset.isnull().sum()

# The distribution of each category
print(car_dataset.Fuel_Type.value_counts())
print(car_dataset.Seller_Type.value_counts())
print(car_dataset.Transmission.value_counts())

# Encoding Fuel_Type Column or convert to the digit values
car_dataset.replace({'Fuel_Type':{'Petrol':0, 'Diesel':1, 'CNG':2}}, inplace=True)

# Encoding Seller_Type Column or convert to the digit values
car_dataset.replace({'Seller_Type':{'Dealer':0, 'Individual':1}}, inplace=True)

# Encoding Transmission Column or convert to the digit values
car_dataset.replace({'Transmission':{'Manual':0, 'Automatic':1}}, inplace=True)

#Split data into training and testing data (drop a column = 1, drop a column = 0)
X = car_dataset.drop(['Car_Name', 'Selling_Price'], axis=1)
Y = car_dataset['Selling_Price']

#Split training and testing, test size = 10 percent for testing data
# random state = 2 > split data in the same way that we splited, 3 > new kind
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=2)

#Training the model through LinearRegression




















