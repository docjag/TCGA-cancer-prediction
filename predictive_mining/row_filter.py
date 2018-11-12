__author__ = "Sohel Mahmud"
__date__ = "24-10-16"
__description__ = "Filter out the rows having very low number of 1's"

import pandas as pd
from os.path import expanduser

def filter_rows(csv_file):
	df = pd.read_csv(csv_file)
	print len(df['#patientID'])

	#Add all the columns and store in a new column name 'total_ones'
	#df['total_ones'] = df.sum(axis=1)

	# df2 = df.loc[df.sum(axis=1) > 0]
	# print len(df2)

	#df2.to_csv('test50_unique.csv', sep=',', header=True, index=False)


#################################################
############ Main body of the program: ##########
#################################################

#Getting the File path
home = expanduser("~") + '/Guided_Research/Data/'
csv_file = home + 'top-20-genes_unique.csv'

filter_rows(csv_file)