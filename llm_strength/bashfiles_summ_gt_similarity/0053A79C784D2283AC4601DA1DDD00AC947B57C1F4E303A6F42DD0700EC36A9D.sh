#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python summ_gt_similarity/0053A79C784D2283AC4601DA1DDD00AC947B57C1F4E303A6F42DD0700EC36A9D.py
