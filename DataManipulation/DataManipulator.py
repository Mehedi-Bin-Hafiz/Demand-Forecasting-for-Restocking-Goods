import  pandas as pd
import re
from datetime import datetime
# df = pd.read_excel('../Database/RawData.xlsx').sample(frac=1).iloc[:300000]
# df.to_excel('../Database/CutData.xlsx')

# ############# Datetime Devider ###############
# df = pd.read_excel('../Database/CutData.xlsx')
# date = df['date'].values
# yearL = list()
# monthL = list()
# dayL = list()
# for i in date:
#     i = pd.to_datetime(i) ##VVI
#     yearL.append(i.year)
#     monthL.append(i.month)
#     dayL.append(i.day)
# df.insert(1,'year',yearL)
# df.insert(2, 'month',monthL)
# df.insert(3, 'day',dayL)
# df.to_excel('../Database/Manipulated.xlsx',index = False)


###################### select first 15000 data ######################
df = pd.read_excel('../Database/Manipulated.xlsx').sample(frac=1).iloc[:15101]
df.to_excel('../Database/AnotherNewFinalManipulated.xlsx')
















############ Old data program ##########

# date = df['InvoiceDate'].values
# Quantity = len(df['Quantity'].unique())
# print(Quantity)
#
# yearc = open('../Database/year.csv', 'a')
# monthc = open('../Database/mont.csv', 'a')
# dayc = open('../Database/day.csv', 'a')
#
# for i in date:
#     if isinstance(i, str):
#         sp = re.split('/| ', i)
#         monthMy = sp[0]
#         dayMy = sp[1]
#         yearMy = sp[2]
#         yearc.write(yearMy+'\n')
#         monthc.write(monthMy+'\n')
#         dayc.write(dayMy+'\n')
#     else:
#         yearc.write(str(i.year)+'\n')
#         monthc.write(str(i.month)+'\n')
#         dayc.write(str(i.day)+'\n')



##############MinMaxScaler##############
# import pandas as pd
# from sklearn.preprocessing import StandardScaler,MinMaxScaler
# df = pd.read_excel('../Database/Manipulated.xlsx')
# Quantity = df['Quantity']
# StockCode = df['StockCode']
# MS = MinMaxScaler(feature_range=(0,1))
# MS = MS.fit_transform([Quantity])
# print(MS)
# df.insert(10,'EnQuantity',MS[0])
# print(df.head())
# df.to_excel('../Database/normalized.xlsx')

#
# ####################Data cutter ###################
#
# age1_disease1= df.loc[ (df['Quantity']<5) & (df['Quantity'] > 0)] #() is vvi think
# age1_disease1.to_excel('../Database/Manipulated.xlsx')