#!/bin/bash
#SBATCH --job-name=fastqtosam # Job name
#SBATCH --nodes=1                   # Run all processes on a single node
#SBATCH --mem=128G
#SBATCH --partition=hpc              # Time limit hrs:min:sec
#SBATCH --output=multiprocess_%j.log # Standard output and error log

start=$(date +%s)
for r1 in /vol01/clean_data/Ca_2_1/*_1.fq.gz;do
  r2=$(echo $r1 | sed 's/_1.fq.gz/_2.fq.gz/g')
  genome="/vol01/clean_data/Reference/ST5024G_5.fasta"
  echo "./runBWAMEM2.sh $genome $r1 $r2";
done > bwamem2.cmds
end=$(date +%s)
diff=$(echo "$end - $start" | bc)
echo "The running time is diff=$diff seconds "
