import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#scatter
N = 1000

x = np.random.randn(N)
y = np.random.randn(N)

plt.scatter(x,y,s = 20,marker = 'D',c = 'g')
plt.savefig("scatter.jpg")




