'''
@Author: Sohel Mahmud
@Date: 22-09-16
@Description: 
'''

import json
import os
#import matplotlib.pyplot as plt
from os import path

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
				#print element['userID']													# For example, element['userID'] = TCGA-OR-A5JP-01.
				for gene_info in element['genes']:								 		# element is a dictionary which is a list member of user_body list
					gene_name = gene_info['gene']										# Parsing the names of the genes from the dictionary
					mutation = gene_info['var_class']
					gene_count[gene_name] = gene_count.get(gene_name, 0) + 1			# word count pattern using dict.get()
					mut_dict[mutation] = mut_dict.get(mutation, 0) + 1
	return gene_count, mut_dict


def user_gene_parser(file_path, gene_list):
	with open(file_path,'r') as input_file:
		tumor_json = json.load(input_file)
		
		gene_user_dict = {}														    
		
		for user_body in tumor_json.values():											
			for element in user_body:													
				print element['userID']
				


#################################################
############ Main body of the program: ##########
#################################################

file_path = 'JSON/ACC.json'

tumor = tumor_name(file_path)

gene_dict, mut_dict = gene_parser(file_path)

gene_total = len(gene_dict.keys())

print 'Tumor Name: %s' %(tumor)
print 'Total number of Genes: %d' %(gene_total)

gene_list = gene_dict.keys()

#user_gene_parser(file_path, gene_list)

'''
mystr = ""
for key, val in gene_dict.items():
	print key, val
	mystr += key + ',' + str(val) + "\n"
	with open('hoga.csv','wb') as hoga:
		hoga.write(mystr)
'''