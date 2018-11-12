import tarfile
import os
from os import path

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir('firebrowse') if path.isfile('firebrowse'+os.sep+x)]

files.sort()                                                        # sorted out according to accending order
users_list = []

for myfile in files:    
    print myfile 
    mutation = myfile.split('_')[1].split('.')[0]                   # extracting the name of the mutation type
    tar = tarfile.open('firebrowse/' + myfile)                      # opening the compressed files in firebrowse directory
    filelist = tar.getnames()                                       # extracting the list of the file names of zipped archive
    print filelist
    for users in filelist:
        users = users.split('/')[1].split('.')[0]                   # extracting the user IDs from the file name
        if users == 'MANIFEST': continue                            # Skip the MANIFEST.txt file
        users_list.append(users)
        #with open('userlist/' + mutation +'.txt','a') as fhand:     # storing the userIDs in the files
            #fhand.write(users + '\n')


for user in users_list:
    with open('all_users.txt', 'a') as fhand:
        fhand.write(user + '\n')
    fhand.close()
