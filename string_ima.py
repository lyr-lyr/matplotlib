import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import random

#randomstring
def random_string():
    str_digits = '0123456789'
    str_lowercase= 'abcdefghijklmnopqrstuvwxyz'
    str_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_all = str_digits +  str_lowercase + str_uppercase
    string = random.sample(str_all,5)
    randomstring = ''.join(string)
    return randomstring

plt.figure(figsize=(24,6))
plt.text(0.3,0.4,random_string(),weight = "light",color = 'green',size = 200)
plt.axis('off')
plt.savefig('string.jpg')