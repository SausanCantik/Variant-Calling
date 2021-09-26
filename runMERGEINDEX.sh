#!/bin/bash
file=$1
out=$2
index=$3
module load samtools
samtools merge -o $out -b $file |samtools index -c $out > $index
