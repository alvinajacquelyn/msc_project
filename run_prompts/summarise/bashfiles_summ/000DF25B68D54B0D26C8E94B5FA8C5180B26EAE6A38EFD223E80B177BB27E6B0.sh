#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_summ/000DF25B68D54B0D26C8E94B5FA8C5180B26EAE6A38EFD223E80B177BB27E6B0.py
