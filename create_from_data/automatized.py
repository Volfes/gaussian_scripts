import pandas as pd

df = pd.read_excel('variables.xlsx')
print(df)
data = []
data = df.iloc[:,1].tolist()  # zmienia w liste .iloc[:,1] całe wiersze pierwsza kolumna
no_space = ''
for i in data:
    i = i.replace('=',' ')
    no_space += i
    no_space += '\n'

