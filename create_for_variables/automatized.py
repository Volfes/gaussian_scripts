import pandas as pd

df = pd.read_excel('variable_values.xlsx')
# print(df)
data = []
row_num = df.index[-1] + 1
a = 0
for row in range(row_num):
    one_input_values = df.iloc[a].tolist()  # zmienia w liste .iloc[1] całe wiersze po kolei wierszami
    a+=1
# print(data)
# no_space = ''
# for i in data:
#     i = i.replace('=',' ')
#     no_space += i
#     no_space += '\n'

