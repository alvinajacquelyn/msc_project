#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s4_llmasjudge_consistency/0004D708768948DB3E79C2300368972EBED64C1FE6C0521A03A868188C122D2A.py
