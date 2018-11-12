#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#

import csv
import os
from os import path

def get_tumor_files(dir_name):
    # Getting the path of the firebrowse directory one level above
    firebrowse = os.path.split(os.getcwd())[0] + '/firebrowse'

    # List comprehension for extracting the names of the files in firebrowse directory
    files = [x for x in os.listdir(firebrowse) if path.isfile(firebrowse + os.sep + x)]

    files.sort() 
    return files

def gene_freq(file_name):

    genes_dict = {}
    tumor_name = file_name.split('.')[0]

    with open(file_name,'rb') as fhand:
        for line in fhand:
            line = line.rstrip()
            print line
            genes_dict[line] =  genes_dict.get(line,0) + 1

    file_out = 'gene_list/' + tumor_name + '_gene_freq.csv'

    with open(file_out,'wb') as fwrite:
            gene_csv = csv.writer(fwrite, quoting=csv.QUOTE_NONE)
            gene_csv.writerow(['Gene','Freq'])

    for gene, freq in genes_dict.items():
        with open('ACC_gene_freq.csv','a') as fwrite:
            gene_csv = csv.writer(fwrite, quoting=csv.QUOTE_NONE)
            gene_csv.writerow([gene,freq])

#################################################
############ Main body of the program: ##########
#################################################

tumor_files = get_tumor_files('firebrowse')

for file in tumor_files:
    gene_freq(file)