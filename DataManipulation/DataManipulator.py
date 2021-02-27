import  pandas as pd
import re
df = pd.read_excel('../Database/RawData.xlsx')

date = df['InvoiceDate'].values

yearc = open('../Database/year.csv', 'a')
monthc = open('../Database/mont.csv', 'a')
dayc = open('../Database/day.csv', 'a')

for i in date:
    if isinstance(i, str):
        sp = re.split('/| ', i)
        monthMy = sp[0]
        dayMy = sp[1]
        yearMy = sp[2]
        yearc.write(yearMy+'\n')
        monthc.write(monthMy+'\n')
        dayc.write(dayMy+'\n')
    else:
        yearc.write(str(i.year)+'\n')
        monthc.write(str(i.month)+'\n')
        dayc.write(str(i.day)+'\n')