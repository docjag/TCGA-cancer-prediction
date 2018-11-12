# @Author: Sohel Mahmud
# @Date: 24-10-16
# @Describe: Filter out the rows having very low number of 1's

'''
# Without using pandas library package

# import csv

# def filter_rows(csv_file, threshold):
# 	with open(csv_file, 'rb') as csvfile:
# 	    spamreader = csv.reader(csvfile)
# 	    with open('test10.csv','a') as fh:
# 			csv_wr = csv.writer(fh, quoting=csv.QUOTE_NONE)
# 			first_line = spamreader.next()
# 			col_num = len(first_line)
# 			csv_wr.writerow(first_line)									#Writing the headers of the file

# 	    rows = [row for row in spamreader if int(row[22]) > threshold]			#Getting the filtered rows of the file

# 	for row in rows:
# 		with open('test10.csv','a') as fh:
# 			csv_wr = csv.writer(fh, quoting=csv.QUOTE_NONE)
# 			csv_wr.writerow(row)


# #################################################
# ############ Main body of the program: ##########
# #################################################

# csv_file = 'test_back.csv'
# filter_rows(csv_file, 10)


'''

# Using pandas library package

import pandas as pd 

csv_file = 'test_back.csv'

df = pd.read_csv(csv_file)
print len(df['#patientID'])

print df.columns.values
df = df.drop('sum', axis=1)
print df.columns.values

rows = df['#patientID'][df['sum'] > 10]
print len(rows)

#Filtering specific columns and add the values
col_list = list(df)
col_list.remove('#patientID')
col_list.remove('Tumor_type')
col_list.remove('sum')

print len(col_list)

df['jag'] = df[col_list].sum(axis=1)
print len(df['jag'])

#Add all the columns and store in a new column name 'jag'
df['total_ones'] = df.sum(axis=1)

#Showing the patient IDs with sum greater than 10
rows = df['#patientID'][df['sum'] > 10]
print len(rows)
