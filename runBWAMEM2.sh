#!/bin/bash
genome=$1
read1=$2
read2=$3
out=$(echo $2 | sed 's/_1.fq.gz/.bam/g')
module load bwa-mem2
module load samtools
bwa-mem2 mem $genome $read1 $read2 |samtools view -S -b /dev/stdin | samtools sort /dev/stdin -o ${out}
