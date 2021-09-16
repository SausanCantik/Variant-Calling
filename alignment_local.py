'''
This code is used to automate mapping bam files to a reference genome using bwa
it is assume you already have:
1. a list_sample.txt file containing sample.txt list
2. a folder named list_reads containing sample.txt files
3. sample.txt files containing string list: reads_1.fq.gz \n reads_2.fq.gz
4. a folder named clean_data containing sample_folder in which your reads rested

Sausan Nafisah | September 2021
'''
import os
import pandas as pd

def parsing_sample (file): #file should be .txt
    read1 = []
    read2 = []
    readID = []
    i = 0
    for line in open(file):
        reads = line.split('\n')[0]
        
        if i % 2 == 1:
            read2.append(reads)
        else :
            read1.append(reads)
            split1 = reads.split('.')
            split2 = split1[0].split ('_')
            get_read = split2[0]+split2[1]+split2[2]
            readID.append(get_read)
        
        i = i+1        
        
    return read1, read2, readID
    
    list_sample = '/mnt/d/F19FTSAPHT0619_PEPuisR/list_sample.txt'
for sample in open(list_sample):
    sample = sample.split('\n')[0]
    sample_file = '/mnt/d/F19FTSAPHT0619_PEPuisR/list_reads/{}'.format(sample)
    print ('Working with folder clean_data/{}'.format(sample))
    
    #_get .gz list on each sample folder
    read1, read2, readID = parsing_sample(sample_file)
    #print('readID \n', readID)
    #print('read1 \n', read1)
    #print('\n')
    
    #_create output folder
    output_folder = '/mnt/d/F19FTSAPHT0619_PEPuisR/Alignment/{}'.format(sample)
    create_output_folder = 'mkdir {}'.format(output_folder)
    os.system(create_output_folder)
    
    #_align reads
    for i in range(len(read1)):
        reference = '/mnt/d/F19FTSAPHT0619_PEPuisR/clean_data/Reference/ST5024G_5.fasta'
        r1 = '/mnt/d/F19FTSAPHT0619_PEPuisR/clean_data/{}/{}'.format(sample, read1)
        r2 = '/mnt/d/F19FTSAPHT0619_PEPuisR/clean_data/{}/{}'.format(sample, read2)
        output = '{}-aln-pe.sam'.format(readID)
        
        align = 'bwa mem {} {} {} > {}'.format(reference, r1, r2, output)
        os.system(align)
        
        #__move output to output folder
        move_file = 'mv {} {}'.format(output, output_folder)
        os.system(move_file)