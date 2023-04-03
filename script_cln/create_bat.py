
def create():
    import local_settings
    import os
    from starting import name, chosen_functional, no_space

    file_name = name

    full_wd = "tmp"

    print(file_name)

    bat= open(f'{full_wd}/{file_name}.bat', "w")
    # bat= open(file_name+'.bat', "w")

    bat.write(f'''%chk={file_name}.chk 
%mem=6GB
%nprocshared=4
#n {chosen_functional}/aug-cc-pvdz int=UltraFine opt=Tight EmpiricalDispersion=GD3

ftfsi

-1 1
N  
S   1 B1
S   1 B2 2 A2
O   3 B3 1 A3 2 D3
O   3 B4 1 A4 2 D4
O   2 B5 1 A5 3 D5
O   2 B6 1 A6 3 D6
F   3 B7 1 A7 2 D7
C   2 B8 1 A8 3 D8
F   9 B9 2 A9 1 D9
F   9 B10 2 A10 1 D10
F   9 B11 2 A11 1 D11
Variables:
{no_space}

end

''')
    bat.close()



