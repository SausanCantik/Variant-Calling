#!/bin/bash
#SBATCH --job-name=fastqtosam # Job name
#SBATCH --nodes=1                   # Run all processes on a single node
#SBATCH --mem=128G
#SBATCH --partition=hpc              # Time limit hrs:min:sec
#SBATCH --output=multiprocess_%j.log # Standard output and error log
start=$(date +%s)
./runMERGEINDEX.sh /vol01/clean_data/Ca_2_1/bam.out /vol01/Alignment/Ca_2_1/Ca_2_1.bam /vol01/Alignment/Ca_2_1/Ca_2_1.bai
end=$(date +%s)
diff=$(echo "$end - $start" | bc)
echo "The running time is $diff seconds "
