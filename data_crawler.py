import investpy
import pandas as pd
df_train = investpy.get_stock_historical_data(stock='VCB', country='VietNam', from_date='01/01/2011', to_date='15/08/2021')
pd.DataFrame(df_train).to_csv("D:\Code\Python\Project3\VCB_train.csv")
df_test = investpy.get_stock_historical_data(stock='VCB', country='VietNam', from_date='16/08/2021', to_date='15/10/2021')
pd.DataFrame(df_test).to_csv("D:\Code\Python\Project3\VCB_test.csv")