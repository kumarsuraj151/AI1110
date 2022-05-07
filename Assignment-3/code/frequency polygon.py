import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

read_table=pd.read_excel("C:\\Users\\SURAJ\\Desktop\\ai-probability\\assi3\\Table\\table2.xlsx")

l_val=read_table["L_length"]
r_val=read_table["R_length"]
freq=read_table["Number of leaves"]

x=[]

for i in range(len(freq)):
    for j in range(freq[i]):
        x.append((l_val[i]+r_val[i])/2)

interval=[117.5,126.5,135.5,144.5,153.5,162.5,171.5,180.5]
a,bins,c=plt.hist(x,bins=interval,histtype='step')
plt.xticks(interval)
l=list(bins)
l.insert(0,0)
l.insert(len(bins)+1,bins[len(bins)-1])
mid=[]
for i in range(len(l)-1):
      ele=(l[i]+l[i+1])/2
      mid.append(ele)
x=list(a)
x.insert(0,0)
x.insert(len(a)+1,0)
plt.plot(mid,x,'go--')
plt.xlabel('length in (mm)')
plt.ylabel('Number of leaves')
plt.show()