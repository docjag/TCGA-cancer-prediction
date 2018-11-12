'''
@Author: Sohel Mahmud
@Date: 22-09-16
@Description: Determining top-N genes for each individual tumory types
'''

import json
import csv
import os
from os import path

def get_file_list():
	# Getting the path of the firebrowse directory one level above
	#json_dir = os.path.split(os.getcwd())[0] + '/JSON'
	
	# List comprehension for extracting the names of the files in firebrowse directory
	files = [x for x in os.listdir('JSON') if path.isfile('JSON' + os.sep + x)]
	files.sort()

	return files

def tumor_name(file_path):
	tumor = file_path.split('/')[1].split('.')[0]										# extract the tumor name from file name
	return tumor


def gene_parser(file_path):
	with open(file_path,'r') as input_file:
		tumor_json = json.load(input_file)												# Loading the json file
		gene_count = {}																	# dictionary for counting the genes
		for user_body in tumor_json.values():											# tumor_json.values is a list of values. Here the number of value is one.
			for element in user_body:													# user_body is a list containing dictionaries of users and gene information.
																						# For example, user_body[89]['userID'] = TCGA-OR-A5JP-01.
				for gene_info in element['genes']:								 		# element is a dictionary which is a list member of user_body list
					gene_name = gene_info['gene']										# Parsing the names of the genes from the dictionary
					gene_count[gene_name] = gene_count.get(gene_name, 0) + 1			# word count pattern using dict.get()
	return gene_count


def top_genes(tumor, gene_dict,top_n):

	lst = [(value, key) for key, value in gene_dict.items()]							# appending the items in (value, key) order
	lst.sort(reverse = True)															# Reverse the list 
    
	for val, key in lst[:top_n]:														# print top_n items in reverse order
	    print '\t',key, val

	    # with open('Top_50/'+tumor + '.csv','a') as fhand:
	    # 	write_freq = csv.writer(fhand,quoting=csv.QUOTE_NONE)
	    # 	write_freq.writerow([key, val])

#################################################
############ Main body of the program: ##########
#################################################

#file_path = 'JSON/ACC.json'
json_files = get_file_list()

top_n = int(raw_input('Enter the number of frequent genes: '))

for file_path in json_files:
	file_path = 'JSON/' + file_path

	tumor = tumor_name(file_path)
	print '###############################'
	print 'Tumor Name: %s' %(tumor)

	gene_dict = gene_parser(file_path)

	gene_total = len(gene_dict.keys())
	print 'Total number of Genes: %d' %(gene_total)

	print 'Top %d mutated genes:' %(top_n)
	
	# with open('Top_50/'+tumor + '.csv','a') as fhand:
	#     write_freq = csv.writer(fhand,quoting=csv.QUOTE_NONE)
	#     write_freq.writerow(['genes', 'freq'])

	top_genes(tumor, gene_dict, top_n)