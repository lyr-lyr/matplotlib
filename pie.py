import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
explode = (0, 0.05, 0, 0)
plt.axes(aspect=1)
explode = (0,0,0,0.8)

plt.pie(fracs, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)

plt.savefig('pie.jpg')

