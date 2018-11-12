'''
@Author: Sohel Mahmud
@Date: 22-09-16
@Description: The format of JSON file is: 
              {'ACC':
              	[
              		{'userID':,
              		 'genes':[
              		 	{'gene':,
              		 	 'var_class':,
              		 	 'var_type':''
              		 	},
              		 	 ,{},...
              		 ]
              		},
              		{},...
              	]
              }
'''

import json
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
		
		gene_count = {}	
		mut_dict = {}																    # dictionary for counting the genes
		
		for user_body in tumor_json.values():											# tumor_json.values is a list of values. Here the number of value is one.
			for element in user_body:													# user_body is a list containing dictionaries of users and gene information.
																						# For example, user_body[89]['userID'] = TCGA-OR-A5JP-01.
				for gene_info in element['genes']:								 		# element is a dictionary which is a list member of user_body list
					gene_name = gene_info['gene']										# Parsing the names of the genes from the dictionary
					mutation = gene_info['var_class']
					gene_count[gene_name] = gene_count.get(gene_name, 0) + 1			# word count pattern using dict.get()
					mut_dict[mutation] = mut_dict.get(mutation, 0) + 1
	return gene_count, mut_dict


def top_N(entity_type, entity_dict, top_n):
	
	gene_counter = len(entity_dict.keys()) 												# Total Number of Mutated Genes
	mut_counter = sum(entity_dict.values())												# Total Number of Mutations
	
	lst = [(value, key) for key, value in entity_dict.items()]							# appending the items in (value, key) order
	lst.sort(reverse = True)															# Reverse the list 
	
	pool_size = gene_counter if entity_type == 'gene' else mut_counter
	print 'Pool Size: ', pool_size
	print entity_dict.values()

	for val, key in lst[:top_n]:
		percentage = float(val) * 100 / pool_size
		print '\t',key, val, str(percentage) + '%'

#################################################
############ Main body of the program: ##########
#################################################

file_path = 'JSON/ACC.json'
top_n = int(raw_input('Enter the number of frequent genes: '))

tumor = tumor_name(file_path)
gene_dict, mut_dict = gene_parser(file_path)
gene_total = len(gene_dict.keys())

print '###############################'
print 'Tumor Name: %s' %(tumor)

#print 'Total number of Genes: %d' %(gene_total)

print 'Top %d mutated genes:' %(top_n)
top_N('gene',gene_dict, top_n)

print 'Top %d mutations:' %(top_n)
top_N('mut',mut_dict, top_n)

'''
json_files = get_file_list()
for file_path in json_files:
	file_path = 'JSON/' + file_path

	tumor = tumor_name(file_path)
	print '###############################'
	print 'Tumor Name:	 %s' %(tumor)

	gene_dict, mut_dict = gene_parser(file_path)

	gene_total = len(gene_dict.keys())
	print 'Total number of Genes: %d' %(gene_total)

	print 'Top %d mutated genes:' %(top_n)

	top_genes(gene_dict, top_n)
'''

'''
#Standard Deviation

import math

s = [2,4,4,4,5,5,7,9]

def average(s): return sum(s) * 1.0 / len(s)
 
avg = average(s)
variance = map(lambda x: (x - avg)**2, s)
average(variance)
standard_deviation = math.sqrt(average(variance))
'''