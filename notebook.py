
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

# API setup
quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'

# choosing stock with linear pattern and showing data
df = quandl.get("WIKI/AAPL")
df= df[["Adj. Close"]]
df.head()

df["Adj. Close"].plot(figsize = (15, 6), color = "g")
plt.legend(loc = "upper left")
plt.show()


forecast = 30 #days, default 30
df["Prediction"] = df[["Adj. Close"]].shift(-forecast)

X = np.array(df.drop(["Prediction"], 1)) #dropping coloumn
X = preprocessing.scale(X) #standardize data so dataset is good for machine learning.. set mean and std of array to 0 and 1

#x.mean() #should give near 0 value
#x.std() #should give 1

#now set last 30 day y values to value x, split into 2 new arrrays

X_forecast = X[-forecast:] #array of days of forecast, no corresponding y val
X = X[:-forecast] #array of days prior

# y array have same size as x array
y = np.array(df["Prediction"])
y = y[:-forecast] #contains all but last 30 days

# create training variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) # 20% of data to go into splilt

#apply and fit linear regression model
clf = LinearRegression() #estimator instance, classifier
clf.fit(X_train, y_train) #create model to fit data

confidence = clf.score(X_test, y_test) #test model linearlty correlation

forecast_predicted = clf.predict(X_forecast) #predicting y values on the x days forecasted
#print(forecast_predicted)
#plt.plot(X, y) #scatterplot of data, model will find lobf

#create array of dates
dates = pd.date_range(start = "2018-03-28", end="2018-04-26")
#print(dates)

plt.plot(dates, forecast_predicted, color = "y")
df["Adj. Close"].plot(color = "g")
plt.xlim(xmin = datetime.date(2017, 4, 26)) #shift start date position for graph 


