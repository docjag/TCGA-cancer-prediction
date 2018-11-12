#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#This program is written for extracting all the genes from a particular archive file (a particular mutatation type). 


import tarfile
import csv

gene_list =  list()

archive_name = 'gdac.broadinstitute.org_ACC.Mutation_Packager_Oncotated_Calls.Level_3.2016012800.0.0.tar.gz'
dir_name = archive_name[:-7]

tar = tarfile.open(archive_name, 'r:gz')

for tar_info in tar:
    myfile = tar.extractfile(tar_info)                      # returns a file descriptor 
    #print myfile.name                                      # myfile.name is the name of the file
    if myfile is None: continue
    elif myfile.name == dir_name + '/MANIFEST.txt': continue
    userID = myfile.name.split('/')[1].split('.')[0]
    userLine = "UserID: " + userID
    with open('tmp/test2.txt', 'a') as fhand:               # Storing the UserID
        fhand.write( userLine+ '\n')
        fhand.close()
    for line in myfile:
        if line.startswith('#'): continue
        line = line.rstrip()
        columns = line.split('\t')
        if len(columns) >= 2:
            if columns[0] == 'Hugo_Symbol': continue
            #print columns[0]
            gene_list.append(columns[0])
            with open('tmp/test2.txt', 'a') as fhand:       # Storing the genes
                fhand.write(columns[0] + '\n')
                fhand.close()
    tar.members = []
   
'''
# Storing only genes, no user information is available
for gene in gene_list:
    with open('tmp/test_dump_fromList.txt', 'a') as fhand:
        fhand.write(gene + '\n')
    fhand.close()
'''
