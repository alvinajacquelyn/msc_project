#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s6_llmasjudge_coherence/000FEED1F11E6C2BD606A1E0D1DFE7C110A98A275145FD5BBFE302C76078E826.py
