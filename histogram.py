# DWM
from matplotlib import pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)
a = np.array([22,22,22,36,36,36,52,52,52,78,78,78])
ax.hist(a, bins = [0,25,50,75,100] ,color="green",edgecolor='black')
ax.set_title("Histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()
