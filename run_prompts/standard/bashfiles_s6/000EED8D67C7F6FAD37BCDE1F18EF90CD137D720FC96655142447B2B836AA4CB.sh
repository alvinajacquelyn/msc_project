#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G

#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s6/000EED8D67C7F6FAD37BCDE1F18EF90CD137D720FC96655142447B2B836AA4CB.py
