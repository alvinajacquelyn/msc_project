#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r1_llmasjudge_fluency/000BCFCB3991FE71555AE7D923C6AC59073626AFFFCC9DADDC7B73C0FED8046A.py

