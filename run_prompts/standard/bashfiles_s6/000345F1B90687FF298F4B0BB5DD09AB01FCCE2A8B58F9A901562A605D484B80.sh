#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s6/000345F1B90687FF298F4B0BB5DD09AB01FCCE2A8B58F9A901562A605D484B80.py
