#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#


import csv

def csv_template_maker(file_to_read, file_to_write):
	genes = ['userID']

	for line in open(file_to_read,'r'):
	    line = line.rstrip()
	    genes.append(line)

	genes.append('Mutation_type')

	with open(file_to_write, 'a') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
	    wr.writerow(genes)

csv_template_maker('All_Genes_filtered.txt','docjag-gene_mutation_record.csv')