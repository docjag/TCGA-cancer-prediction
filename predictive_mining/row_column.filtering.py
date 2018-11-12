# @Author: Sohel Mahmud
# @Date: 03-11-16
# @Describe: Filter out the rows and columns with zero-sums

import pandas as pd
from os.path import expanduser

def filter_rows(csv_file, file_out):
	df = pd.read_csv(csv_file)

	#Determining the number of Rows
	print len(df['#patientID'])

	#Add all the columns and store in a new column name 'total_ones'
	#df['total_ones'] = df.sum(axis=1)

	#print df.loc[df.sum(axis=1) > 0]

	df2 = df.loc[df.sum(axis=1) > 0]
	print len(df2)

	#Writing in a CSV file
	df2.to_csv(file_out, sep=',', header=True, index=False)

def filter_cols(csv_file):
	pass


#################################################
############ Main body of the program: ##########
#################################################

#Getting the File path
home = expanduser("~") + '/Guided_Research/Data/'

# genes_no = raw_input('Enter the number of genes: ')
# file_prefix = 'top-' + genes_no + '-'
# csv_file = home + file_prefix +'genes_unique.csv'
# file_out = file_prefix + 'genes_filtered.csv'

csv_file = home + 'Top-50-genes_all.csv'
file_out = 'top-50-genes-all-filtered.csv'

filter_rows(csv_file,file_out)