#Author: Sohel Mahmud
#Date: 22-08-16
#Description: Extracting the genes from a single archive and 
# storing as a JSON format

import os
import json
import tarfile
import csv

gene_list =  []
data = {}
silent_dict = {}
user_gene_list = []

#archive_name = 'gdac.broadinstitute.org_ACC.Mutation_Packager_Oncotated_Calls.Level_3.2016012800.0.0.tar.gz'
archive_name = 'gdac.broadinstitute.org_BLCA.Mutation_Packager_Oncotated_Calls.Level_3.2016012800.0.0.tar.gz'

# Getting the path of the firebrowse directory one level above
archive_name = os.path.split(os.getcwd())[0] + os.sep + archive_name

# taking the directory name from archive_name excluding the archive extensions (.tar.gz) (7 characters)
dir_name = archive_name[:-7]

tumor_type = {}
tumor_name = archive_name.split('_')[1].split('.')[0]

tar = tarfile.open(archive_name, 'r:gz')

for tar_info in tar:
    myfile = tar.extractfile(tar_info)

    if myfile is None: continue
    
    elif myfile.name == dir_name + '/MANIFEST.txt': continue

    userID = myfile.name.split('/')[1].split('.')[0]

    for line in myfile:
        if line.startswith('#'): continue
        line = line.rstrip()
        columns = line.split('\t')
        if len(columns) >= 2:
            if columns[0] == 'Hugo_Symbol': continue

            if columns[8] == 'Silent': 
                silent_dict['Silent'] = silent_dict.get('Silent',0) + 1
                continue

            gene_list.append(columns[0])
            
    print userID
    data['userID'] = userID
    data['genes'] = gene_list

    user_gene_list.append(data)
    #user_gene_list.append(data.copy())

    gene_list = []
    data = {}

    tar.members = []

tumor_type[tumor_name] = user_gene_list

#create a JSON file using the data
with open('BLCA.json', 'w') as outfile:
    json.dump(tumor_type, outfile, sort_keys = True, indent=4)
                                                        