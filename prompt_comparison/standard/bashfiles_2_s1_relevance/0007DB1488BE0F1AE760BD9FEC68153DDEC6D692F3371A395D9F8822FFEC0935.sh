#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=100G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s1_llmasjudge_relevance/0007DB1488BE0F1AE760BD9FEC68153DDEC6D692F3371A395D9F8822FFEC0935.py
