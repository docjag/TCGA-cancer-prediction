import csv
import pandas as pd

acc_genes = []
gene_pool = []

with open('ACC.txt','rb') as fhand:
    for lines in fhand:
        lines = lines.strip()
        acc_genes.append(lines)

with open('sohel.csv','rb') as gene_csv:
    read_me = csv.reader(gene_csv)
    gene_pool = read_me.next()

gene_pool.pop(0)
gene_pool.pop(len(gene_pool) - 1)

acc_genes = set(acc_genes)
result = [i for i, item in enumerate(gene_pool) if item in acc_genes]

'''
print result
print len(result)
'''
df= pd.read_csv('sohel.csv')
for i in result: 
    print(df.loc[df[gene_pool[i]] == 1])
    
