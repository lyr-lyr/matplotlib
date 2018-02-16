import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#bar
N=5

y=[20,10,30,25,15]

index = np.arange(N)

p1 = plt.bar(left=index, height=y,width=0.5,bottom=100,color='r')
plt.savefig('bar.jpg')

