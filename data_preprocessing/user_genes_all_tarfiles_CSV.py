#Author: Sohel Mahmud
#Date: 16-09-16
#Description: Extracting genes from all archive files of 36 tumor_names and storing into a CSV file

import tarfile
import csv
import os
from os import path

silent_mut = {}

# Getting the path of the firebrowse directory one level above
firebrowse = os.path.split(os.getcwd())[0] + '/firebrowse'

# List comprehension for extracting the names of the files in firebrowse directory
archives = [x for x in os.listdir(firebrowse) if path.isfile(firebrowse + os.sep + x)]

archives.sort()                                                                # sorted out according to accending order

for archive in archives:
    tumor_name = archive.split('_')[1].split('.')[0]                         # extracting the name of the tumor_name type
    
    #user_gene_list =  []
    
    dir_name = archive[:-7]                                                  # extracting the name of the archive directory
    
    tar_files = tarfile.open(firebrowse +'/' + archive, 'r:gz')                    # opening the compressed files in firebrowse directory
                                                                            # tarfile.open(myfile) returns a TarFile Object
    for tar_file in tar_files:
        user_gene_list =  []
        myfile = tar_files.extractfile(tar_file)                                  # tar.extractfile(tar_info) return regular file type object
        
        if myfile is None: continue                                         # Excluding the file object NONE
        elif myfile.name == dir_name + '/MANIFEST.txt': continue            # Excluding the MANIFEST.txt file
        
        userID = myfile.name.split('/')[1].split('.')[0]
        user_gene_list.append(userID)
        print tumor_name, userID

        for line in myfile:
            if line.startswith('#'): continue                               # Excluding the lines starting with #
            line = line.rstrip()
            columns = line.split('\t')
            if len(columns) >= 2:
                if columns[0] == 'Hugo_Symbol': continue
                if columns[8] == 'Silent':                                  # Filtering out the silent mutated genes
                    silent_mut['Silent'] = silent_mut.get('Silent', 0) + 1
                    continue
                user_gene_list.append(columns[0])

        tar_files.members = []

    	with open('CSV/' + tumor_name + '.csv', 'a') as outfile:
        	wr = csv.writer(outfile, quoting=csv.QUOTE_NONE)
        	wr.writerow(user_gene_list)