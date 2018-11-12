# @Author: Sohel Mahmud
# @Date: 24-10-16
# @Describe: Filter out the rows having very low number of 1's

import pandas as pd
import numpy as np
from os.path import expanduser

#Getting the File path
home = expanduser("~") + '/Guided_Research/Data/'
csv_file = home + 'top-20-genes_unique.csv'

df = pd.read_csv(csv_file)
print len(df['#patientID'])

#Add all the columns and store in a new column name 'total_ones'
#df['total_ones'] = df.sum(axis=1)

df['ACC?'] = np.where(df['Tumor_type'] == 'ACC', 'Yes', 'No')


df2 = df.loc[df.sum(axis=1) > 0]
print len(df2)
print len(df2.columns.values)

df2.to_csv('jaglul_pasha.csv', sep=',', header=True, index=False)
