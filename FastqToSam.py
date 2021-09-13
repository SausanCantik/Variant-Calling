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
        #print(R1)
        #print('\n')
        
         #_loop for every sample folder
        for i in len(range(R1)):
            fastqtosam = 'picard fastqtosam \
            F1= R1[i] \
            F2= R2[i] \
            O= {}.bam \
            SM= sample001 \
            RG= rg001'.format(R1[i])
            
            os.system(fastqTosam)