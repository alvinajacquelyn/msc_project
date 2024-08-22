#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G

source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s4_llmasjudge_consistency/00005BE947A8F108382B59CED7D1E95871A68539C00FF53FD3E1D93C58E2BA6C.py
