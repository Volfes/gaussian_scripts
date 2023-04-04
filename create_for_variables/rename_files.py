import os

directory = "E:\Python_projects\script_cln\create_for_variables\\tmp"
os.chdir(directory)
dir_list = os.listdir(directory)
for item in dir_list:
    if '.sh' in item:
        print("'"+item+"'"+",")
