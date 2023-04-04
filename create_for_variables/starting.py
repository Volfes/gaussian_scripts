import os
import create_bat
import create_sh
import pandas as pd

df = pd.read_excel('variable_values.xlsx')
data_top = df.columns

# print(df)
# data = []
# row_num = df.index[-1] + 1
# h = 0
# for row in range(row_num):
#     one_input_values = df.iloc[h].tolist()  # zmienia w liste .iloc[1] całe wiersze po kolei wierszami
#     h+=1

functionals = ['b3lyp','lc-wpbe', 'm062x', 'pbepbe']
a = 0
c=1  # wartość nazwy FTFSI zaczynając od 1
for i in range(15):

    data = []
    one_input_values = df.iloc[c].tolist()  # zmienia w liste .iloc[1] całe wiersze po kolei wierszami
    no_space = ""
    k = 0
    for word in one_input_values:
        # print(word)
        if k != 0:
            no_space += str(data_top[k]) + (" ") + str(word) + "\n"
        k += 1

    for x in range(4):
        name = f"FTFSI{str(c)}{functionals[x]}"
        print(name)
        chosen_functional = functionals[x]
        create_bat.create()
        create_sh.create()
        # os.system(f'sbatch {name}.sh')
    c += 1
