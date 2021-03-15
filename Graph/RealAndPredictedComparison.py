import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
import warnings
import matplotlib.pyplot as plt


warnings.filterwarnings("ignore")
#database
MainDatabase = pd.read_excel("../Database/AnotherNewFinalManipulated.xlsx")
# base on database we will set iloc
x = MainDatabase.iloc[: , 1:6].values  #independent variables
print(x)
y = MainDatabase.iloc[ : , -1].values #dependent variables
print(y)

ValidationDataset = pd.read_excel("../Database/ValidationDataset.xlsx")
Vx = ValidationDataset.iloc[: , 1:6].values
Vy = ValidationDataset.iloc[ : , -1].values

thirtypercent=0.30  # training size 70%
fourtypercent=0.40   # training size 60%
fiftypercent=0.50    # training size 50%
sixtypercent=0.60    # training size 40%
seventypercent=0.70   # training size 30%



print("\n########## Gradient Boosting ###########")
print("30% data usage rate")
X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=.30, random_state=42)
clf_gb = GradientBoostingRegressor(n_estimators=200)
clf_gb.fit(X_train,y_train)
y_pred = clf_gb.predict(Vx)
print('Mean Absolute Error:', metrics.mean_absolute_error(Vy, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Vy, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Vy, y_pred)))
print('r2_sore:',r2_score(Vy,y_pred))


axes = plt.axes()
XandYlen = [x for x in range(0,len(y_pred))]
plt.plot(XandYlen, ValidationDataset['sales'].values.tolist(), linewidth=3)
plt.plot(XandYlen, y_pred,  linewidth=2)
plt.yticks([1,20,40,60,80,100,120,140,160])
plt.grid()
plt.legend(['Real value', 'Predicted value'])
plt.xlabel('Numbers')
plt.ylabel('Prediction')
plt.savefig("real vs prediction.png")
plt.show()