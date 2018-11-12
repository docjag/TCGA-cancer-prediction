# @Author: Sohel Mahmud
# @Date: 09-10-16
# @Description: determine the frequencies of top 50 genes in all 36 different tumors

import csv
import os
from os import path

#Returns a list of file names of all types of tumors
def get_tumor_files(dir_name):
	# Getting the path of the firebrowse directory one level above
	files_dir = os.getcwd() + os.sep + dir_name

	#print os.getcwd()

	# List comprehension for extracting the names of the files in firebrowse directory
	files = [x for x in os.listdir(files_dir) if path.isfile(files_dir + os.sep + x)]
	files.sort()
	return files


# Write the column headers for the output file in CSV format
def write_header(tumor_name, tumor_files):
	tumor_lst = ['genes'] + [file.split('.')[0] for file in tumor_files]
	with open('Top50_genes_statistics/Top50_'+ tumor_name +'.csv','a') as fhand:
		writecsv = csv.writer(fhand, quoting=csv.QUOTE_NONE)
		writecsv.writerow(tumor_lst)


def total_mutation(gene_file):
	total_mut = sum(1 for line in open(gene_file,'rb'))
	return total_mut


# Getting the most frequent 50 genes of a particular tumor
# Here the parameter 'file_path' is the file of 50 genes
def get_gene_freq(top50_genes_file, files, tumor):

	#List for storing the genes of 
	gene_lst = []
	
	#The directory name of the 
	dir_name = 'tumors_all_mutations'

	#Reading Top 50 genes from a particular tumor type
	with open(top50_genes_file, 'rb') as fhand:
		fhand.readline()		# skip the headers of the file. Alternative -> next(fhand)
		for line in fhand:
			line = line.rstrip()
			gene_lst.append(line.split(',')[0])

	#Sorting the gene list
	gene_lst.sort()

	# for each gene from the 50 frequent genes, get the list of frequencies for 36 tumors
	for gene in gene_lst:
		lst = []
		for file in files:
			dct = {}
			file = dir_name + '/' + file
			# Getting gene pool 
			with open(file,'rb') as read_me:
				total_mut = total_mutation(file)
				for line in read_me:
					line = line.rstrip()
					if line.startswith(gene):
						dct[line] = dct.get(line, 0) + 1
			if not dct.values():
				val = 0
			else: val = float(dct.values()[0]) * 100 / total_mut
			lst.append(val)

		lst = [gene] + lst

		with open('Top50_genes_statistics/Top50_'+ tumor +'.csv','a') as fhand:
			writecsv = csv.writer(fhand, quoting=csv.QUOTE_NONE)
			writecsv.writerow(lst)



#################################################
############ Main body of the program: ##########
#################################################

#Getting the names of all tumor files
tumor_files = get_tumor_files('tumors_all_mutations')

for file in tumor_files:
	#Extracting the tumor name from the archive file name
	tumor_name = file.split('.')[0]

	#Writing the column header in the output file for a particular tumor
	write_header(tumor_name, tumor_files)

	#Gene file name for a particular tumor
	top50_genes = 'Top50_genes_all_tumors/' + tumor_name + '.csv'

	#Calling the "get_gene_freq" function for getting the frequencies of gene
	#for all types of tumors
	get_gene_freq(top50_genes, tumor_files, tumor_name)

	print tumor_name + " file is printed!!"

#Print notification while the file is written for a particular tumor
print 'File printing finished!!'