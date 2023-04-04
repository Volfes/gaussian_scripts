import os

directory = "E:\studia\Zaawansowane modelowanie molekularne\mgr\\aug"
os.chdir(directory)
dir_list = os.listdir(directory)
for item in dir_list:
    if '.log' in item:
        # print(item[:-4]+"aug"+item[-4:])
        os.rename(item, item[:-4]+"aug"+item[-4:])
