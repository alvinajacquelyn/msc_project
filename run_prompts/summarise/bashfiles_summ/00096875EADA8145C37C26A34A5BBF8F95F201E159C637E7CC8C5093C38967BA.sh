#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_summ/00096875EADA8145C37C26A34A5BBF8F95F201E159C637E7CC8C5093C38967BA.py
