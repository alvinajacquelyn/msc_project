#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r5_llmasjudge_fluency/0035C98CEC406051345DE5770AFBC9880C6512E2DE71D15E84CCC03A79EF3A38.py
