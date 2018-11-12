# Author: Sohel Mahmud
# Date: 15-08-16
# Description: Extracting all mutated genes (except silently mutated ones)
# from all the tumor type archives. The name of all mutated genes are sorted in
# ascending order


import tarfile
import os
from os import path
import pandas as pd

# Getting the path of the firebrowse directory one level above
firebrowse = os.path.split(os.getcwd())[0] + '/firebrowse'

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir(firebrowse) if path.isfile(firebrowse + os.sep + x)]

files.sort()                                                                # sorting the file names in ascending order

gene_list = []
silent_dict = {}

for myfile in files:
    mutation = myfile.split('_')[1].split('.')[0]                           # extracting the name of the mutation type
    dir_name = myfile[:-7]                                                  # extracting the name of the archive directory
    tar = tarfile.open(firebrowse +'/' + myfile, 'r:gz')                      # opening the compressed files in firebrowse directory
                                                                            # tarfile.open(myfile) returns a TarFile Object
    for tar_info in tar:
        myfile = tar.extractfile(tar_info)                                  # tar.extractfile(tar_info) return regular file type object
        print myfile.name
        if myfile is None: continue                                         # Excluding the file object NONE
        if myfile.name == dir_name + '/MANIFEST.txt': continue              # Excluding the MANIFEST.txt file
        for line in myfile:
            if line.startswith('#'): continue                               # Excluding the lines starting with #
            line = line.rstrip()
            columns = line.split('\t')
            if len(columns) >= 2:
                if columns[0] == 'Hugo_Symbol': continue
                
                if columns[8] == 'Silent':                                  # Filtering out the silent mutated genes
                    silent_dict['Silent'] = silent_dict.get('Silent',0) + 1
                    continue
                
                gene_list.append(columns[0])
                
                # Writing the mutated genes in files naming with the tumors
                with open('gene_list/filtered/' + mutation + '.txt', 'a') as fhand:
                    fhand.write(columns[0] + '\n')
                    fhand.close()

        tar.members = []                                                    # Clearing the list of tar members

gene_list.sort()


for gene in gene_list:
    with open('gene_list/filtered/All_filtered.txt', 'a') as fhand:
        fhand.write(gene + '\n')
    fhand.close()
