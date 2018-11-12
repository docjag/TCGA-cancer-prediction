'''
@Author: Sohel Mahmud
@Date: 22-09-16
@Description: Summary of all types tumors parsing data from the json files.
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

def gene_parser(file_path):
	with open(file_path,'r') as input_file:
		tumor_json = json.load(input_file)												
		gene_dict = {}	
		mut_dict = {}
		patient_count = 0
		for user_body in tumor_json.values():											
			for element in user_body:													
				#print element['userID']
				patient_count += 1
				for gene_info in element['genes']:								 		
					gene_name = gene_info['gene']
					mutation = gene_info['var_class']
					gene_dict[gene_name] = gene_dict.get(gene_name, 0) + 1
					mut_dict[mutation] = mut_dict.get(mutation, 0) + 1
	return patient_count, gene_dict, mut_dict

def display_list_format(tumor_name, patient_count, gene_dict, mut_dict):
	
	gene_count = len(gene_dict.keys()) 								# Total Number of Mutated Genes
	mut_count = sum(mut_dict.values())							# Total Number of Mutations

	avg_effect_genes = gene_count / patient_count

	mut_per_gene = mut_count / gene_count
	mut_per_patient = mut_count / patient_count

	#print the tumor name
	print 'Tumor Name: %s' %(tumor_name)
	print '--------------------'
	my_str = 'Tumor Name: ' + tumor_name + '\n'
	my_str += '--------------------' + '\n'

	#print the number of patients
	print 'Number of Patients: ', patient_count
	my_str += 'Number of Patients: ' + str(patient_count) + '\n'

	#print the total number of genes
	print 'Total number of mutated Genes: %d' %(gene_count)
	my_str += 'Total number of Genes: ' + str(gene_count) + '\n'

	#print the total number of mutations
	print 'Total number of mutations: ',mut_count
	my_str += 'Total number of mutations: '+ str(mut_count) + '\n'

	#print the average effected genes 
	print 'average effected gene: ',avg_effect_genes
	my_str += 'average effected gene: ' + str(avg_effect_genes) + '\n'

	#print the number of mutations per gene
	print 'Number of mutations per gene: ',mut_per_gene
	my_str += 'Number of mutations per gene: '+ str(mut_per_gene) + '\n'

	#Print the number of mutations per patient
	print 'Number of mutations per patient: ',mut_per_patient
	print '#####################################'
	my_str += 'Number of mutations per patient: '+ str(mut_per_patient) + '\n'
	my_str += '#####################################' + '\n'

	#Write in a file
	write_result(my_str,'tumor_summary.txt')

def write_result(str_to_write, output_file):
	with open(output_file,'a') as fhand:
		fhand.write(str_to_write)


#################################################
############ Main body of the program:###########
#################################################

#file_path = 'JSON/ACC.json'
json_files = get_file_list()


# Checking whether the outfile exists so that
# we don't need to write the CSV header again
if not os.path.exists(os.getcwd() + os.sep +'tumor_summary.csv'):
	print 'File does not exist!!'
	# Creating the header of the CSV file
	with open('tumor_summary.csv','a') as outfile:
		wr = csv.writer(outfile, quoting=csv.QUOTE_NONE)
		wr.writerow(['Cancer Type','Sample Size','Genes','Mutations'])

# Creating the summary for 36 types of tumors in a CSV format
for file_path in json_files:
	file_path = 'JSON/' + file_path

	tumor = tumor_name(file_path)
	patients, gene_dict, mut_dict = gene_parser(file_path)
	
	display_list_format(tumor,patients, gene_dict, mut_dict)   					# For showing the results in list format


'''
# Creating the summary for 36 types of tumors in a CSV format
for file_path in json_files:
	file_path = 'JSON/' + file_path

	tumor = tumor_name(file_path)
	patients, gene_dict, mut_dict = gene_parser(file_path)
	
	genes = len(gene_dict.keys()) 							# Total Number of Mutated Genes
	result = sum(mut_dict.values())							# Total Number of Mutations

	summary_list = [tumor, patients, genes, mutations]		# List of all results

	# Creating CSV file with above outcomes
	with open('tumor_summary.csv','a') as outfile:
		wr = csv.writer(outfile, quoting=csv.QUOTE_NONE)
		wr.writerow(summary_list)
'''
	#display_result(tumor,patients, gene_dict, mut_dict)   	# For showing the results in list format