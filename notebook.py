# #Part 1 - print dataset
# import quandl
# import pandas as pd

# quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'

# df = quandl.get("WIKI/AAPL")
# df.head()

# #Part 2 - view adjusted close coloumn for analysis
# import quandl
# import pandas as pd

# quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'

# df = quandl.get("WIKI/AAPL")
# df= df[["Adj. Close"]]

# df.head()

# #Part 3 - show graph of stock price data over time
# # Imports used
# import quandl
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
# from sklearn.linear_model import LinearRegression

# # API setup
# quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'

# # choosing stock with linear pattern and showing data
# df = quandl.get("WIKI/AAPL")
# df= df[["Adj. Close"]]
# df.head()

# df["Adj. Close"].plot(figsize = (15, 6), color = "g")
# plt.legend(loc = "upper left")
# plt.show()

#Part 4 - Predicting future data points,x is features, y is labels...
# Imports used
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


forecast = 30
df["Prediction"] = df[["Adj. Close"]].shift(-forecast)

X = np.array(df.drop(["Prediction"], 1)) #dropping coloumn
X = preprocessing.scale(X) #standardize data so dataset is good for machine learning.. set mean and std of array to 0 and 1

#x.mean() #should give near 0 value
#x.std() #should give 1

#now set last 30 day y values to value x, split into 2 new arrrays

X_forecast = X[-forecast:] #array of days of forecast, no corresponding y val
X = X[:-forecast] #array of days prior

# y array have same size as x array
y = np.array(dif["Prediction"])
y = y[:-forecast] #contains all but last 30 days