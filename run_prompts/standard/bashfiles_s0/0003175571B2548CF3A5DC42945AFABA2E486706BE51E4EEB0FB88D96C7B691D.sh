#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_2_s0/0003175571B2548CF3A5DC42945AFABA2E486706BE51E4EEB0FB88D96C7B691D.py
