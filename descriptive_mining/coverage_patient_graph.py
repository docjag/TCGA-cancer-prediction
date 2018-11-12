'''
@Author: Sohel Mahmud
@Date: 25-09-16
@Description: Generating the graph of coverage patient vs most mutated genes
'''


import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []


# Opening a CSV file for loading the patient numbers and the mostly mutated gene names
with open('dummy.csv','rb') as csvfile:
	plots = csv.reader(csvfile)

	for row in plots:
		x.append(row[1])
		y.append(row[0])

ind = []
genes = []

for i, j in enumerate(x):
	ind.append(i)
	genes.append(j)

print ind
print genes

plt.xticks(ind, genes)


'''
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('dummy.csv', delimiter = ',', unpack=True)
my_xticks = ['John','Arnold','Mavis','Matt']
plt.xticks(x, my_xticks)

'''

plt.plot(ind, y, label='Patient Coverage')
plt.hist()
plt.xlabel('Most Mutated Genes')
plt.ylabel('Coverage Patients')
plt.title('Coverage Patient vs Most mutated Genes')
plt.legend()
plt.show()
