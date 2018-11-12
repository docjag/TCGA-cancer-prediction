#Author: Sohel Mahmud
#Date: 22-08-16
#Description: Extracting genes from all archive files of 32 tumor_names and storing into a JSON file
#             The format of the JSON file is {userID: [gene_list],...}


import json
import tarfile
import os
from os import path

silent_mut = {}

# Getting the path of the firebrowse directory one level above
firebrowse = os.path.split(os.getcwd())[0] + '/firebrowse'

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir(firebrowse) if path.isfile(firebrowse + os.sep + x)]

files.sort()                                                                # sorted out according to accending order

for myfile in files:
    tumor_name = myfile.split('_')[1].split('.')[0]                         # extracting the name of the tumor_name type
    print tumor_name

    tumor_type = {}
    user_gene_list =  []

    dir_name = myfile[:-7]                                                  # extracting the name of the archive directory
    tar = tarfile.open(firebrowse +'/' + myfile, 'r:gz')                    # opening the compressed files in firebrowse directory
                                                                            # tarfile.open(myfile) returns a TarFile Object
    for tar_info in tar:
    	
    	gene_list = []
        data = {}
        
        myfile = tar.extractfile(tar_info)                                  # tar.extractfile(tar_info) return regular file type object
        if myfile is None: continue                                         # Excluding the file object NONE
        elif myfile.name == dir_name + '/MANIFEST.txt': continue            # Excluding the MANIFEST.txt file

        userID = myfile.name.split('/')[1].split('.')[0]
        
        for line in myfile:
            if line.startswith('#'): continue                               # Excluding the lines starting with #
            line = line.rstrip()
            columns = line.split('\t')
            if len(columns) >= 2:

            	gene_dict = {}

                if columns[0] == 'Hugo_Symbol': continue
                if columns[8] == 'Silent':                                  # Filtering out the silent mutated genes
                    #silent_mut['Silent'] = silent_mut.get('Silent', 0) + 1
                    continue

                gene_dict['gene'] = columns[0]
            	gene_dict['var_class'] = columns[8]
            	gene_dict['var_type'] = columns[9]
            
            	gene_list.append(gene_dict)
        
        gene_list.sort()
        
        data['userID'] = userID
        data['genes'] = gene_list

        user_gene_list.append(data)
        # alternative way: user_gene_list.append(data.copy())

        tar.members = []

    tumor_type[tumor_name] = user_gene_list

    with open('JSON/' + tumor_name + '.json', 'wb') as outfile:
    	json.dump(tumor_type, outfile,sort_keys = True, indent = 4)


'''
with open('all_user_genes.json', 'w') as outfile:                           # Create a JSON file using the data
    json.dump(tumor_type, outfile,sort_keys = True)                         # There is another variant: json.dumps() for creating a JSON file
'''