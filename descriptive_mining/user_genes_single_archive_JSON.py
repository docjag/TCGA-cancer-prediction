#Author: Sohel Mahmud
#Date: 22-08-16
#Description: Extracting the genes from a single archive and 
# storing as a JSON format

import os
import json
import tarfile


gene_list =  []
data = {}
user_gene_list = []
gene_dict = {}
tumor_dict = {}

# Resolving the path issues
archive_name = 'gdac.broadinstitute.org_ACC.Mutation_Packager_Oncotated_Calls.Level_3.2016012800.0.0.tar.gz'

# taking the directory name from archive_name excluding the archive extensions (.tar.gz) (7 characters)
directory_name = archive_name[:-7]

# One level above in the directory structure
archive_path = os.path.split(os.getcwd())[0] + '/' + archive_name

#Opening the tar file
tar = tarfile.open(archive_path, 'r:gz')

#Extracting the name of the tumor for the achive name
tumor_name = (archive_name.split('_')[1]).split('.')[0]

for tar_info in tar:
    myfile = tar.extractfile(tar_info)
    #print myfile.name
    if myfile is None: continue
    elif myfile.name == directory_name + '/MANIFEST.txt': continue
    userID = myfile.name.split('/')[1].split('.')[0]
    for line in myfile:
        if line.startswith('#'): continue
        line = line.rstrip()
        columns = line.split('\t')
        if len(columns) >= 2:
            if columns[0] == 'Hugo_Symbol': continue
            
            #print columns[0]
            #gene_list.append(columns[0])
            gene_dict['gene'] = columns[0]
            gene_dict['var_class'] = columns[8]
            gene_dict['var_type'] = columns[9]
            
            gene_list.append(gene_dict)
            gene_dict = {}
            
    data['userID'] = userID
    data['genes'] = gene_list
    user_gene_list.append(data)
    
    gene_list = []
    data = {}       
    
    tar.members = []

tumor_dict[tumor_name] = user_gene_list

#create a JSON file using the data
with open('all_tumors.json', 'w') as outfile:
    json.dump(tumor_dict, outfile,sort_keys = True, indent=4)        # There is another variant: json.dumps() for creating a JSON file
                                                                    # json.dumps(): 