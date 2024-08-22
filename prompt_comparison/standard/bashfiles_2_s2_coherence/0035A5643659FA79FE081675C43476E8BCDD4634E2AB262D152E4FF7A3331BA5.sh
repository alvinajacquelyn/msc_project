#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=100G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s2_llmasjudge_coherence/0035A5643659FA79FE081675C43476E8BCDD4634E2AB262D152E4FF7A3331BA5.py
