# import quandl
# import pandas as pd
# quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'
# df = quandl.get("WIKI/AAPL") #choose stock with linear pattern
# df.head()


import quandl
import pandas as pd

quandl.ApiConfig.api_key = 'LsYwP9quyK2ezGbiNKGq'

df = quandl.get("WIKI/AAPL") #choose stock with linear pattern
df = df[['Adj. CLose']]
df.head()