'''
@Author: Sohel Mahmud
@Date: 18-09-16
@Description:
'''

import json
import csv
import os
from os import path

# Read the CSV gene mutation record file
def read_gene_headers():
    with open('gene_mutation_record.csv','r') as fhand:
        heading = fhand.readline()                                  # Reading the first line from the file
        heading.rstrip()                                            # Removing the EOL character '\n'
        heading =  heading.split(',')                               # Spliting the fields with ',' delimiter
        heading.pop(0)                                              # Removing the first field UserID
        heading.pop(len(heading) - 1)                               # Removing the last field Mutation_type
        return heading												# Returns a list of all(22,255) mutatated genes


gene_pool = read_gene_headers()
print len(gene_pool)

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir('JSON') if path.isfile('JSON' + os.sep + x)]
files.sort()

result = []	
for myfile in files:								
	with open('JSON/'+ myfile,'r') as input_file:					
		tumor_json = json.load(input_file)				# ACC.json contains 90 dictionaries for 90 users
		tumor_name = tumor_json.keys()[0]				# Getting tumor name
		
		for x in tumor_json[tumor_name]:	  			# Getting each dictionary x from the list
			userID = x['userID']		  				# Each userID
			gene_list = x['genes']

			result.append(userID)
			
			# Binary matrix maker
			for gene in gene_pool:
				if gene in gene_list:
					result.append(1)
				else: result.append(0)

			result.append(tumor_name)
			with open('sohel.csv', 'a') as fhand:
				wr = csv.writer(fhand, quoting=csv.QUOTE_NONE)
				wr.writerow(result)
			result = []