#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=100G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s3_llmasjudge_coherence/000AEF92243C36C5F4357E5121E74D1D9FD5579A6D1B3CFFEF2354817DED8541.py
