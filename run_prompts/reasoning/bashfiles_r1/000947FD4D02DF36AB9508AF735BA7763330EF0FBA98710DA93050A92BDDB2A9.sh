#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r1/000947FD4D02DF36AB9508AF735BA7763330EF0FBA98710DA93050A92BDDB2A9.py
