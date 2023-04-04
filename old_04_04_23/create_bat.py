import local_settings
import os

provide_path = local_settings.path
file_name = input(f'provide name: ')

txt = open("data.txt", 'r')
wd = os.getcwd()
full_wd = f"{wd}/{provide_path}"
print(full_wd)
bat= open(f"{full_wd}/{file_name}.bat","w+")
bat.write(f'''%chk={file_name}.chk 
{txt.read()}

''')
bat.close()



