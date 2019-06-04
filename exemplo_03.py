
"""
Exemplo 03

"""

'''
# modificação 1

import matplotlib.pyplot as plt


X = [1, 2, 1, 2]
Y = ['Eduardo', 'Lucas', 'Regis', 'Victor']

# plt.plot(X, Y)
plt.bar(Y, X)

plt.show()
'''

'''
# modificação 2

import matplotlib.pyplot as plt


X = [1, 2, 1, 2]
Y = ['Eduardo', 'Lucas', 'Regis', 'Victor']

X.append(5)

Y.append('Alex')

plt.barh(Y, X)

plt.show()
'''

'''
# modificação 3

import matplotlib.pyplot as plt


X = [1, 2, 1, 2, 5]

ls = ['A', 'B', 'C', 'D', 'E']
colors = ['r', 'g', 'b', 'k', 'y']

plt.pie(X, labels=ls, colors=colors)

plt.show()
'''

'''
# modificação 4

import matplotlib.pyplot as plt


X = [1, 10, 99 , -3]


plt.hist(X)

plt.show()
'''
'''
# # modificação 4

import matplotlib.pyplot as plt
from random import  randint


X = [randint(1, 500) for x in range(500)]


plt.hist(X)

plt.show()
'''

# modificação 5

import matplotlib.pyplot as plt
import  numpy as np


X = [np.random.uniform() for x in range(100)]

plt.hist(X)

plt.show()
