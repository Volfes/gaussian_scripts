import os


data = os.listdir('tmp')

for i in data:
    info = []
    with open(('''tmp/'''+i), 'r') as file:
        for line in file:
            # new_line = line.strip(" \n")
            info.append(line)
        
        freq = []
        for a in info:
            if "Frequencies" in a:
                freq.append(a.split())
                # a.strip(" ")
                # print(a)
                
print(freq)
        # info = f.readline()
        # print(info)
# import pandas as pd

# with open("tmp", "r") as file:
#     test = []
#     for line in file:
#         new_line = line.strip(" \n")
#         test.append(new_line)
#     num_pos = test.index('Final structure in terms of initial Z-matrix:')
#     values = []
#     for i in range(30):
#         values.append(test[num_pos+i+14])
#     for a in values:
#         print(a)
#     # text = file.readlines()
#     # print(text)