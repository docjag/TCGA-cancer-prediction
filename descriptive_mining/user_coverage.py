'''
@Author: Sohel Mahmud
@Date: 05-10-16
@Description: determine the frequency of patients for each mutated gene

'''

import collections
import pandas as pd

csv_file = 'Top-50-genes.csv'

# Getting the Data frame
df = pd.read_csv(csv_file)

gene_dict = {}

# Determine the patients for each type of mutated genes
for gene_name in df.columns.values:
	if gene_name in ['#patientID', 'Tumor_type']:
		continue
	
	patients = df['#patientID'][df[gene_name] == 1]
	
	patients_list = list(patients)
	patients_no = len(patients)
	
	#print patients_list
	#print patients_no

	gene_dict[gene_name.upper()] = patients_no

# for key, val in gene_dict.items():
# 	print key, val

# print sum(gene_dict.values())

# print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.'
gene_dict = collections.OrderedDict(sorted(gene_dict.items()))


df2 = pd.Series(gene_dict)

print df2

df2.to_csv('user_coverage.csv', sep=',')
