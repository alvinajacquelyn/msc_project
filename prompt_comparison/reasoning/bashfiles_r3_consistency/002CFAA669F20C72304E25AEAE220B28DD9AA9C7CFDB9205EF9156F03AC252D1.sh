#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r3_llmasjudge_consistency/002CFAA669F20C72304E25AEAE220B28DD9AA9C7CFDB9205EF9156F03AC252D1.py
