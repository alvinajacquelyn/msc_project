#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=200G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_r1_llmasjudge_relevance/0013121BFDC7CC7E21401F95144EF56AF783F20477748E488725A1CFF68BB2B7.py
