import os
import create_bat
import create_sh

create_sh
os.chdir(f'{create_bat.full_wd}')
os.system('sbatch scr.sh')