import json
import os
from os import path


def tumor_name(file_path):
	tumor = file_path.split('/')[1].split('.')[0]
	return tumor

def gene_counter(file_path):
	with open(file_path,'r') as input_file:
		acc_json = json.load(input_file)
		gene_count = {}
		for x in acc_json.values():
			for element in x:
				for gene in element['genes']:
					gene_count[gene] = gene_count.get(gene, 0) + 1
	return gene_count


def top_genes(gene_dict,top_n):
	lst = []
	for key, value in gene_dict.items():
	    lst.append((value,key))

	lst.sort(reverse = True)
	for val, key in lst[:top_n]:
	    print key, val


#################################################
############ Main body of the program:###########
#################################################

file_path = 'JSON_Sorted/ACC.json'

#top_n = 50
top_n = raw_input('Enter the number of top genes: ')
top_n = int(top_n)

tumor = tumor_name(file_path)

gene_dict = gene_counter(file_path)

print 'Tumor Name: %s' %(tumor)
print 'Total number of Genes: %d' %(len(gene_dict.keys()))

print 'Top %d mutated genes:' %(top_n)
print '#####################'

top_genes(gene_dict, top_n)