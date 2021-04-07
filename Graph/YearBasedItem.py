
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")
#database
MainDatabase = pd.read_excel("../Database/AnotherNewFinalManipulated.xlsx")

sumCount = list()
for i in range(2013,2018):
    yearly = MainDatabase.loc[MainDatabase['year'] == i,'item']
    yearly = pd.DataFrame(yearly)
    itemCountsDf =  yearly['item'].value_counts().rename_axis('uniqueItems').reset_index(name='counts')
    sumCount.append(sum(itemCountsDf['counts'].values.tolist()))

print(sumCount)

objects = [x for x in range(2013,2018)]
y_pos = np.arange(len(objects)) #[x for x in range(len(objects))]

plt.bar(y_pos, sumCount,width=0.5, align='center', alpha=0.8)
plt.xticks(y_pos, objects)
plt.ylabel('Sales items')
plt.xlabel('Years')
plt.grid()
plt.savefig('yearly sales rate.png')
plt.show()
