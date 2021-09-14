import os
import pandas as pd

def parsing_sample (file): #file should be .txt
    R1 = []
    R2 = []
    i = 0
    for line in open(file):
        reads = line.split()[-1]
        if i % 2 == 1:
            R2.append(reads)
        else :
            R1.append(reads)
            folder = reads.split('_')[0]
        i = i+1
        
    return R1,R2

def parsing_fastq (R1):
    output_name = []
    for file in R1:
        output = file.split('.')
        output_name.append(output[0])
    return output_name

if __name__ == "__main__":
    file = '/vol01/folder_list.txt'
    for line in open(file):
        line = line.split('\n')
        print("Working with {} folder".format(line[0]))
    
        #_get .gz list on each sample folder
        folder = '/vol01/clean_data/{}'.format(line[0])
        get_list = 'dir {0} > list_{1}.txt'.format(folder,line[0])
        os.system(get_list)
        R1, R2 = parsing_sample('list_{}.txt'.format(line[0]))
        move_list = 'mv /vol01/list_{}.txt /vol01/list_reads'.format(line[0])
        os.system(move_list)
        #print(R1)
        #print('\n')
        
        #_create output name
        output_name = parsing_fastq(R1)
        
        #_loop for every sample folder
        for i in range(len(R1)) :
            fastqtosam = 'java -jar /vol01/picard/picardcloud.jar FastqToSam \
            F1= /vol01/clean_data/{0}/{1} \
            F2= /vol01/clean_data/{0}/{2} \
            O= /vol01/PEP_bam/{3}.bam \
            SM= sample001 \
            RG= rg001'.format(line[0], R1[i], R2[i],output_name[i])
            
            os.system(fastqtosam)