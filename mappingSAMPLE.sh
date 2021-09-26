#!/bin/bash
#SBATCH --job-name=fastqtosam # Job name
#SBATCH --nodes=1                   # Run all processes on a single node
#SBATCH --mem=128G
#SBATCH --partition=hpc              # Time limit hrs:min:sec
#SBATCH --output=multiprocess_%j.log # Standard output and error log

start=$(date +%s)
./runBWAMEM2.sh /vol01/clean_data/Reference/ST5024G_5.fasta /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-529_1.fq.gz /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-529_2.fq.gz
./runBWAMEM2.sh /vol01/clean_data/Reference/ST5024G_5.fasta /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-530_1.fq.gz /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-530_2.fq.gz
./runBWAMEM2.sh /vol01/clean_data/Reference/ST5024G_5.fasta /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-531_1.fq.gz /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-531_2.fq.gz
./runBWAMEM2.sh /vol01/clean_data/Reference/ST5024G_5.fasta /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-532_1.fq.gz /vol01/clean_data/Ca_2_1/V300030679_L2_B5GPEPuisRAAADAAA-532_2.fq.gz
end=$(date +%s)
diff=$(echo "$end - $start" | bc)
echo "The running time is $diff seconds "
