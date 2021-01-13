#Part 1 - print dataset
import quandl
import pandas as pd

quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'

df = quandl.get("WIKI/AAPL")
df.head()

#Part 1 - print dataset
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
df.head()
 
# SHOW APPL
df = df['Adj. CLose']
df.head()

df['Adj. Close'].plot(figsize=(15, 6), color='g')
plt.legend(loc='upper left')
plt.show()