
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

##################### item vs sell scatter plot #####################
warnings.filterwarnings("ignore")
#database
MainDatabase = pd.read_excel("../Database/AnotherNewFinalManipulated.xlsx")
MainDatabase.plot(kind='scatter', x = 'item', y =  'sales')
plt.savefig('itemVSales scatter plot.png')
plt.show()

###################### year vs item ###########################
MainDatabase.plot(kind='scatter', x = 'store', y =  'sales')
plt.savefig('storeVSsales scatter plot.png')
plt.show()

