######### 1
# import quandl
# import pandas as pd
# quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'
# df = quandl.get("WIKI/AAPL") #choose stock with linear pattern
# df.head()

######### 2
# import quandl
# import pandas
# quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'
# df = quandl.get("WIKI/AAPL") #choose stock with linear pattern
# df = df[['Adj. CLose']]
# df.head()

########## 3
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression