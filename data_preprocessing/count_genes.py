import json
import os
from os import path

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir('JSON_Sorted') if path.isfile('JSON_Sorted' + os.sep + x)]

files.sort()
print files
print 'Number of files: %d' %(len(files))
for myfile in files:
	with open('JSON_Sorted/'+ myfile,'r') as input_file:
		acc_json = json.load(input_file)
		
		gene_count = 0
		user_count = 0
		tumor = myfile.split('.')[0]
		
		for x in acc_json.values():
			for element in x:
				gene_count += len(element['genes'])
				user_count += 1
		print "Tumor: %s, Patients: %d, Genes: %d" %(tumor, user_count, gene_count)


