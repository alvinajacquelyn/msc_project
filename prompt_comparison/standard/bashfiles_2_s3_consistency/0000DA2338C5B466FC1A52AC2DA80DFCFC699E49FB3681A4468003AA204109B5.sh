#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=150G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s3_llmasjudge_consistency/0000DA2338C5B466FC1A52AC2DA80DFCFC699E49FB3681A4468003AA204109B5.py
