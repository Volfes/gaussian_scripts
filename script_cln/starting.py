import os
import pandas as pd
import create_bat
import create_sh

df = pd.read_excel('variables.xlsx')
data = []
data = df.iloc[:,1].tolist()  # zmienia w liste .iloc[:,1] całe wiersze pierwsza kolumna
no_space = ''
for i in data:
    i = i.replace('=',' ')
    no_space += i
    no_space += '\n'
blank = []
functionals = ['lc-wpbe', 'm062x', 'pbepbe']
a = 0
c=2  # wartość nazwy FTFSI zaczynając od 2
for i in range(14):

    data = []
    data = df.iloc[:,c].tolist()  # zmienia w liste .iloc[:,1] całe wiersze pierwsza kolumna
    no_space = ''
    for i in data:
        i = i.replace('=',' ')
        no_space += i
        no_space += '\n'

    for x in range(3):
        name = f"FTFSI{str(c)}{functionals[x]}"
        print(name)
        chosen_functional = functionals[x]
        create_bat.create()
        create_sh.create()
        # os.system(f'sbatch {name}.sh')
    c += 1
