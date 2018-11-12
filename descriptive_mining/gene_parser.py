'''
@Author: Sohel Mahmud
@Date: 24-09-16
@Description: Parsing all genes from all tumors and determine the top-50 genes
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
	tumor = file_path.split('/')[1].split('.')[0]
	return tumor

def gene_parser():
	
	json_files = get_file_list()
	gene_dict = {}	
	mut_dict = {}
	patient_count = 0
	
	for file_path in json_files:
		file_path = 'JSON/' + file_path
		with open(file_path,'r') as input_file:
			tumor_json = json.load(input_file)												
			for user_body in tumor_json.values():											
				for element in user_body:													
					#print element['userID']
					patient_count += 1
					for gene_info in element['genes']:								 		
						gene_name = gene_info['gene']
						mutation = gene_info['var_class']
						gene_dict[gene_name] = gene_dict.get(gene_name, 0) + 1
						mut_dict[mutation] = mut_dict.get(mutation, 0) + 1
		print file_path
		print len(mut_dict.keys())
		print '>>>>>>>>>>>>>>>>>'
		for key, val in mut_dict.items():
			if val != 0:
				print key, val
	return patient_count, gene_dict, mut_dict

def top_N(entity_dict,top_n):

	lst = [(value, key) for key, value in entity_dict.items()]							# appending the items in (value, key) order
	lst.sort(reverse = True)															# Sort the list in reverse order

	top_genes = ['#patientID']

	# with open('Top-50-genes.csv','wb') as fhand:
	# 		csv_write = csv.writer(fhand, quoting=csv.QUOTE_NONE)
	# 		csv_write.writerow(['Genes','Frequencies'])

	for val, key in lst[:top_n]:														# print top N items in reverse order
		print '\t',key, val
		top_genes.append(key)
		
		# with open('Top-50-genes.csv','a') as fhand:
		# 	csv_write = csv.writer(fhand, quoting=csv.QUOTE_NONE)
		# 	csv_write.writerow([key,val])

	top_genes.append('Tumor_type')

	# with open('Top-50-genes_all.csv','a') as fhand:
	# 	csv_write = csv.writer(fhand, quoting=csv.QUOTE_NONE)
	# 	csv_write.writerow(top_genes)

def bottom_N(entity_dict, bottom_n):

	lst = [(value, key) for key, value in entity_dict.items()]							# appending the items in (value, key) order
	lst.sort()																			# sort the list 
    
	for val, key in lst[:bottom_n]:														# print bottom N items in reverse order
		print '\t', key, val



#################################################
############ Main body of the program:###########
#################################################

n_items = int(raw_input('Enter the number of top mutated genes: '))

patients, genes, mutation = gene_parser()

'''
print 'Coverage Patients: ',patients

print 'Gene Pool: ',len(genes.values())
print 'Top %d genes' %(n_items)
top_N(genes, n_items)

print 'Bottom %d genes' %(n_items)
bottom_N(genes,n_items)

print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

print 'Types of Mutations: ', len(mutation.values())
print 'Total occurances of ', sum(mutation.values())

# Print all types of mutations
print 'Name of Mutations:'
for key in mutation.keys(): print '\t',key

print 'Frequencies of mutations: '
top_N(mutation, 22)

print '>>>>>>>>>>>>>>>>>>>>>'

#print 'Bottom 10 mutations: '
#bottom_N(mutation, 10)

# Minimum and maximum occuring mutations
for key, val in mutation.items():
	if min(mutation.values()) == val:
		print 'lowest occuring mutation: ', key
		print 'occurs: ', val

	if max(mutation.values()) == val:
		print 'highest occuring mutation: ', key
		print 'occurs: ', val
'''