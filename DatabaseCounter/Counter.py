import pandas as pd
import warnings

warnings.filterwarnings("ignore")
#database
MainDatabase = pd.read_excel("../Database/AnotherNewFinalManipulated.xlsx")

#################### Store Counter ######################

Store = set(MainDatabase['store'])
print('total store',Store)
#################### Store Counter ######################
item = set(MainDatabase['item'])
print('total item',item)
#################### Store Counter ######################
year = set(MainDatabase['year'])
print('total year',year)