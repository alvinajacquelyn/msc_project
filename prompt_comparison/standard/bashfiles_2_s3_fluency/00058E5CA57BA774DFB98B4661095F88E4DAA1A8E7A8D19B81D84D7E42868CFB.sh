#!/bin/bash -l
#$ -l gpu=1

#$ -l tmpfs=100G
#$ -l mem=40G


source /etc/profile.d/modules.sh

module load python/3.8.6
source msc/bin/activate

cd Scratch/

python python_s3_llmasjudge_fluency/00058E5CA57BA774DFB98B4661095F88E4DAA1A8E7A8D19B81D84D7E42868CFB.py
