#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=1500G
#$ -l mem=192G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s4/00076CF9D074F00DEA55AF490B9EE8766F8E98382F070AFF6A02D15954DC6C9D.py
