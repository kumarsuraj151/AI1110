import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

read_table=pd.read_excel("C:\\Users\\SURAJ\\Desktop\\ai-probability\\assi3\\Table\\table2.xlsx")
l_val=read_table["L_length"]
r_val=read_table["R_length"]
freq=read_table["Number of leaves"]



# adjusting frequency
x=[]

for i in range(len(freq)):
    for j in range(freq[i]):
        x.append((l_val[i]+r_val[i])/2)
        
bins=[117.5,126.5,135.5,144.5,153.5,162.5,171.5,180.5]
plt.hist(x,bins=bins, histtype='bar',edgecolor='black')
plt.xticks(bins)
plt.xlabel('length in (mm)')
plt.ylabel('Number of leaves')

plt.show()