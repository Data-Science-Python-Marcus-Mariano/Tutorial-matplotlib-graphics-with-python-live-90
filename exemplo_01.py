"""
Tutorial explained how to create graphics with matplotlib in python.

Tutorial-matplotlib-graphics-with-python-live-90

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-matplotlib-graphics-with-python-live-90

License: GNU GENERAL PUBLIC LICENSE Version 3
"""

'''
# modificação 1

import matplotlib.pyplot as plt
from matplotlib import style


# Embalezador de Gráficos
style.use('ggplot')

X = range(10)
Y = [val ** 2 for val in X]

plt.plot(X, Y)
plt.show()
'''

'''
# modificação 2

import matplotlib.pyplot as plt
from matplotlib import style


# Embalezador de Gráficos
style.use('ggplot')

X = range(10)
Y = [val ** 2 for val in X]

plt.plot(X, Y, label='Batatinhas')
plt.plot(Y, X, label='Mouses')
plt.legend()

# plt.plot(X, Y)
plt.show()
'''

# modificação 2

import matplotlib.pyplot as plt
from matplotlib import style


# Embalezador de Gráficos
style.use('ggplot')

X = range(10)
Y = [val ** 2 for val in X]
Z = [val ** 3 for val in X]

plt.plot(X, Y, label='Batatinhas')
plt.plot(Y, X, label='Mouses')
plt.plot(X, Z, label='Cubos')
plt.legend()

# plt.plot(X, Y)
plt.show()
