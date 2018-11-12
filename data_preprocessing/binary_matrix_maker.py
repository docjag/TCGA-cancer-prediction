'''
@Author: Sohel Mahmud
@Date: 19-09-16
@Description: Creating the binary matrix of 22255 genes vs 9037 patients for 36 tumor types
X-Axis resembles the gene pool and Y-Axis is for the patients
'''

import json
import csv
import os
from os import path

# Read the CSV gene mutation record file
def read_gene_headers(file_path):
    with open(file_path,'r') as fhand:
        heading = fhand.readline()                                  # Reading the first line from the file
        heading.rstrip()                                            # Removing the EOL character '\n'
        heading =  heading.split(',')                               # Spliting the fields with ',' delimiter
        heading.pop(0)                                              # Removing the first field UserID
        heading.pop(len(heading) - 1)                               # Removing the last field Mutation_type
        return heading												# Returns a list of all(22255) mutatated genes


#Gettng the list of file names from a directory
def list_files(dir_path):
	# List comprehension for extracting the names of the files in firebrowse directory
	files = [x for x in os.listdir(dir_path) if path.isfile(dir_path + os.sep + x)]
	files.sort()
	return files 													# Returns a list of file names

# Creating Binary matrix
def binary_matrix_maker(src_dir, dest_dir, gene_pool):
	result = []
	with open(src_dir,'rb') as input_file:					
		tumor_json = json.load(input_file)								# ACC.json contains 90 dictionaries for 90 users
		tumor_name = tumor_json.keys()[0]								# Getting tumor name
		print tumor_name
		for x in tumor_json[tumor_name]:	  							# Getting each dictionary x from the list
			userID = x['userID']		  								# Each userID
			gene_list = x['genes']

			result.append(userID)
			
			# Binary matrix maker
			for gene in gene_pool:
				if gene in gene_list:
					result.append(1)
				else: result.append(0)

			result.append(tumor_name)
			with open(dest_dir, 'a') as fhand:
				wr = csv.writer(fhand, quoting=csv.QUOTE_NONE)
				wr.writerow(result)
			result = []


########################################################################
##################### Main body of the programm ########################
########################################################################

#Getting the all genes from all types of tumors
gene_pool = read_gene_headers('sohel.csv')

print 'Size of Gene pool: ', len(gene_pool)

files = list_files('JSON_Sorted')

for file in files:
	# binary_matrix_maker(src_dir, dest_dir, gene_pool)
	binary_matrix_maker('JSON_Sorted/' + file, 'sohel.csv', gene_pool)