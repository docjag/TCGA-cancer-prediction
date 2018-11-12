import pandas as pd
import matplotlib.pyplot as plt

#pd.read_csv('try_pandas.csv', quoting=2).hist(bins=50)
df = pd.read_csv('gene-mutations.csv', quoting=2)

ax = df.plot.bar(legend=None)
#ax.set_xticks(df.index)
#ax.set_xticklabels(df.Genes, rotation=90)

plt.xlabel("Genes")
plt.ylabel("Mutation variants")
plt.title('Mutated Genes vs variant class')
plt.show()

'''
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('D1.csv', quoting=2)
data.hist(bins=50)
plt.xlim([0,115000])
plt.title("Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
'''