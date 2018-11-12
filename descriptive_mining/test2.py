'''
@Author: Sohel Mahmud
@Date: 22-09-16
@Description: Summary of all types tumors parsing data from the json files.
'''

import json
import csv
import os
from os import path

def path_finder():
	# Getting the path of the firebrowse directory one level above
	#json_dir = os.path.split(os.getcwd())[0] + '/JSON'
	
	# List comprehension for extracting the names of the files in firebrowse directory
	files = [x for x in os.listdir('JSON') if path.isfile('JSON' + os.sep + x)]
	files.sort()

	return files

def tumor_name(file_path):
	tumor = file_path.split('/')[1].split('.')[0]
	return tumor

def gene_parser(file_path):
	with open(file_path,'r') as input_file:
		tumor_json = json.load(input_file)												
		gene_count = {}	
		mut_count = {}
		userIDs = 0
		for user_body in tumor_json.values():											
			for element in user_body:													
				#print element['userID']
				userIDs += 1
				for gene_info in element['genes']:								 		
					gene_name = gene_info['gene']
					mutation = gene_info['var_class']
					gene_count[gene_name] = gene_count.get(gene_name, 0) + 1
					mut_count[mutation] = mut_count.get(mutation, 0) + 1
	return userIDs, gene_count, mut_count


#################################################
############ Main body of the program:###########
#################################################

#file_path = 'JSON/ACC.json'
json_files = path_finder()

if not os.path.exists(os.getcwd() + os.sep +'tumor_summary.csv'):
	print 'File does not exist!!'
	# Creating the header of the CSV file
	with open('tumor_summary.csv','a') as outfile:
		wr = csv.writer(outfile, quoting=csv.QUOTE_NONE)
		wr.writerow(['Cancer Type','Sample Size','Genes','Mutations'])