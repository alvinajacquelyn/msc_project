#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r3_llmasjudge_consistency/0003175571B2548CF3A5DC42945AFABA2E486706BE51E4EEB0FB88D96C7B691D.py
