#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r5_llmasjudge_fluency/001EF856699CBB1791EF2DEB00F66DD259491C332E0A8A4DC3ADF80531EBFF8B.py
