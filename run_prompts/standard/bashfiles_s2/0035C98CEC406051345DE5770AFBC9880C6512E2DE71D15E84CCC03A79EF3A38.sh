#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s2/0035C98CEC406051345DE5770AFBC9880C6512E2DE71D15E84CCC03A79EF3A38.py
