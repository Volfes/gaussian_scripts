import os

directory = "E:\studia\Zaawansowane modelowanie molekularne\mgr\\tmp"
dir_list = os.listdir(directory)
name_list = []
for item in dir_list:
    if '.log' in item:
        name_list.append(item)
name_list.sort()
print(name_list)
