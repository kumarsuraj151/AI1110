import matplotlib.pyplot as plt


x=[118,120,122,127,128,129,130,132,
136,137,138,139,140,141,142,143,142.5,
145,145.5,146,146.5,147,147.5,148,148.5,
149,149.5,150,150.5,
154,155,156,157,158,
163,164,165,166,
172,173]
bins=[117.5,126.5,135.5,144.5,153.5,162.5,171.5,180.5]
plt.hist(x,bins=bins, histtype='bar',edgecolor='black')
plt.xlabel('length in (mm)')
plt.ylabel('Number of leaves')

plt.show()