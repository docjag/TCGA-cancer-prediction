'''
@Author: Sohel Mahmud
@Date: 07-10-16
@Description: Determining top-N genes for each individual tumory types
'''

import json

def gene_parser(file_path):
	with open(file_path,'r') as input_file:
		tumor_json = json.load(input_file)												# Loading the json file
		gene_count = {}																	# dictionary for counting the genes
		mut_dict = {}
		gene_mut = {}
		for user_body in tumor_json.values():											# tumor_json.values is a list of values. Here the number of value is one.
			for element in user_body:													# user_body is a list containing dictionaries of users and gene information.
																						# For example, user_body[89]['userID'] = TCGA-OR-A5JP-01.
				for gene_info in element['genes']:								 		# element is a dictionary which is a list member of user_body list
					gene_name = gene_info['gene']										# Parsing the names of the genes from the dictionary
					gene_count[gene_name] = gene_count.get(gene_name, 0) + 1			# word count pattern using dict.get()
					mutation = gene_info['var_class']									# parsing the mutation type
					mut_dict[mutation] = mut_dict.get(mutation, 0) + 1
	return gene_count, mut_dict


def top_genes(gene_dict, total_mutations, top_n):

	lst = [(value, key) for key, value in gene_dict.items()]							# appending the items in (value, key) order
	lst.sort(reverse = True)															# Reverse the list 
    
	for val, key in lst[:top_n]:
		mut_rate = float(val) / total_mutations
		print '\t',key, val, mut_rate

#################################################
############ Main body of the program: ##########
#################################################

top_n = 5

file_path = 'dummy.json'

tumor = 'ACC'
print '###############################'
print 'Tumor Name: %s' %(tumor)

gene_dict,mutation_dict = gene_parser(file_path)

gene_total = len(gene_dict.keys())
print 'Total number of Genes: %d' %(gene_total)

total_mutations = sum(mutation_dict.values())
print 'Total number of mutations: %d' %(total_mutations)

print 'Top %d mutated genes:' %(top_n)

top_genes(gene_dict, total_mutations, top_n)