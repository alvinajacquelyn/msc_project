#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=100G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s0_llmasjudge_relevance/00217C8F76AAA8E5453BFC1269CB080A9A2F7F3D32480FC0C4A1EB99C22AFBAC.py
