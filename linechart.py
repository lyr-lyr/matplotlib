import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.text(0,40,'function:y = x*x')
plt.savefig('linechart.jpg')