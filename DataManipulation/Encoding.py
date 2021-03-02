import  pandas as pd
import re
Dataframe = pd.read_excel('../Database/Manipulated.xlsx').iloc[:200000]

uniqueCheck = len(Dataframe['StockCode'].unique())
print(uniqueCheck)

""" we will use label encoder"""

from sklearn.preprocessing import LabelEncoder

#Country
le = LabelEncoder()
label = le.fit(Dataframe['Country'].astype(str))
label = label.transform(Dataframe['Country'].astype(str))
Dataframe.insert(4,'EnCountry',label)

#stock Code
le = LabelEncoder()
label = le.fit(Dataframe['StockCode'].astype(str))
label = label.transform(Dataframe['StockCode'].astype(str))
Dataframe.insert(5,'EnStockCode',label)
print(Dataframe.head())
Dataframe.to_excel('../Database/FinalManipulated.xlsx')



