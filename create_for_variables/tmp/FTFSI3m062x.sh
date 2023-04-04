#!/bin/bash -l
# Nazwa zlecenia
#SBATCH -J FTFSI3m062x
# uzywamy 1 wezel
#SBATCH -N 1
# Maksymalna liczba zadan w zleceniu (domyslnie liczba rdzeni)
#SBATCH -n 4
#SBATCH --ntasks-per-core=1
# Maksymalna ilosc zuzytej pamieci na wezel (w MB)
#SBATCH --mem 6500
# Specyfikacja partycji
#SBATCH -p student
# przejscie do katalogu z ktorego wywolany zostal sbatch
#cd $SLURM_SUBMIT_DIR


# przejscie do katalogu z ktorego wywolany zostal sbatch
cd $SLURM_SUBMIT_DIR


# absolutely essential
export g09root="/opt/g09"
source /opt/g09/g09/bsd/g09.profile

# running g09 program with test.bat
g09 FTFSI3m062x.bat
        