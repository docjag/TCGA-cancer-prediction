#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#



import csv

hugo_symbol = tuple()

with open('sample.maf') as f:
    for _ in xrange(3):
        next(f)
    
# the following codes won't work!! as we have already dump the column info into hugo_symbol
#    hugo_symbol = zip(*[line.split() for line in f])[0]
#    variant_class = zip(*[line.split() for line in f])[8]

# Dumping the column data into the variable col_dump
# from the dump, we have assigned the particular column values to the hugo_symbol and variant_class
# Here, hugo_dump and variant_class are tuples

    col_dump = zip(*[line.split() for line in f])
    hugo_symbol, variant_class = col_dump[0], col_dump[8]



zipped_hugo = zip(hugo_symbol, variant_class)

for hugo in zipped_hugo:
    print hugo

# Created two empty lists
hugo_list, variant_list = list(), list()

for hugo in hugo_symbol :
    if hugo == 'Hugo_Symbol': continue
    hugo_list.append(hugo)  
    print hugo

print '>>>>>>>>>>>'

'''
for var in variant_class :
    #variant_list.append(var)    
    print var
'''

with open('writeme.txt', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(hugo_list)
