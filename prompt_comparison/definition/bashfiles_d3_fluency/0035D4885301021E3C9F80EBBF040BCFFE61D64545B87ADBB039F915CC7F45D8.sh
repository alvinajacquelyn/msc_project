#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G



source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_d3_llmasjudge_fluency/0035D4885301021E3C9F80EBBF040BCFFE61D64545B87ADBB039F915CC7F45D8.py
