with open('Top-50-genes_all.csv','rb') as fhand:
	for line in fhand:
		line = line.rstrip()
		tumor = line.split(',')[51]
		if not tumor in ['COAD','READ','LGG','GBM','KICH','KIRP','KIRC','STAD','ESCA']:
			print tumor
			with open('write_me.txt','a') as fhand2:
				fhand2.write(line+'\n')