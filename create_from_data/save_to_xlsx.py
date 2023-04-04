import pandas as pd
ix = 0
row_name = ['aug','lc-wpbe', 'm062x', 'pbepbe']
data_name = [
    'FTFSI1aug.log', 'FTFSI1lc-wpbe.log', 'FTFSI1m062x.log', 'FTFSI1pbepbe.log', 'FTFSI2aug.log', 'FTFSI2lc-wpbe.log', 'FTFSI2m062x.log', 'FTFSI2pbepbe.log', 'FTFSI3aug.log', 'FTFSI3lc-wpbe.log', 'FTFSI3m062x.log', 'FTFSI3pbepbe.log', 'FTFSI4aug.log', 'FTFSI4lc-wpbe.log', 'FTFSI4m062x.log', 
'FTFSI4pbepbe.log', 'FTFSI5aug.log', 'FTFSI5lc-wpbe.log', 'FTFSI5m062x.log', 'FTFSI5pbepbe.log', 'FTFSI6aug.log', 'FTFSI6lc-wpbe.log', 'FTFSI6m062x.log', 'FTFSI6pbepbe.log', 'FTFSI7aug.log', 'FTFSI7lc-wpbe.log', 'FTFSI7m062x.log', 'FTFSI7pbepbe.log', 'FTFSI8aug.log', 'FTFSI8lc-wpbe.log', 'FTFSI8m062x.log', 'FTFSI8pbepbe.log', 'FTFSI9aug.log', 'FTFSI9lc-wpbe.log', 'FTFSI9m062x.log', 'FTFSI9pbepbe.log',
'FTFSI10aug.log', 'FTFSI10lc-wpbe.log', 'FTFSI10m062x.log', 'FTFSI10pbepbe.log', 'FTFSI11aug.log', 'FTFSI11lc-wpbe.log', 'FTFSI11m062x.log', 'FTFSI11pbepbe.log', 'FTFSI12aug.log', 'FTFSI12lc-wpbe.log', 'FTFSI12m062x.log', 'FTFSI12pbepbe.log', 'FTFSI13aug.log', 'FTFSI13lc-wpbe.log', 'FTFSI13m062x.log', 'FTFSI13pbepbe.log', 'FTFSI14aug.log', 'FTFSI14lc-wpbe.log', 'FTFSI14m062x.log', 'FTFSI14pbepbe.log', 'FTFSI15aug.log', 'FTFSI15lc-wpbe.log', 'FTFSI15m062x.log', 'FTFSI15pbepbe.log'
]
big_data = []
for name in data_name:
    value_clm = []
    index_clm = []
    with open(f'''E:\studia\Zaawansowane modelowanie molekularne\mgr\\tmp\{name}''', "r") as file:
        test = []
        for line in file:
            new_line = line.strip(" \n")
            test.append(new_line)
        num_pos = test.index('Final structure in terms of initial Z-matrix:')
        values = []
        for i in range(30):
            values.append(test[num_pos+i+14])
        for a in values:
            position = a.find("=")
            value_clm.append(a[position+1:])
            index_clm.append(a[:position])
        big_data.append(value_clm)
df = pd.DataFrame(big_data,  columns = index_clm, index=data_name)

df.to_excel('variable_values.xlsx')




