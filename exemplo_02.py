"""
Exemplo 02

without ggplot
"""

'''
# modificação 1

import matplotlib.pyplot as plt


X = range(10)
Y = [val ** 2 for val in X]
Z = [val ** 3 for val in X]

plt.plot(X, Y, label='Batatinhas')
plt.plot(Y, X, label='Mouses')
plt.plot(X, Z, label='Cubos')
plt.legend()
plt.grid(True, lw=2, ls='--')

plt.show()
'''

'''
# modificação 2

import matplotlib.pyplot as plt


X = range(10)
Y = [val ** 2 for val in X]
Z = [val ** 3 for val in X]
W = [val ** 4 for val in X]

plt.plot(X, Y, label='Quadrados')
plt.plot(X, W, label='4 pontência')
plt.plot(X, Z, label='Cubos')

plt.title('Gráfico Irado da live 90')

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.legend()
plt.grid(True, lw=2, ls='--')

plt.show()
'''

# modificação 3

import matplotlib.pyplot as plt

box = {
    'facecolor': '.75',
    'boxstyle': 'round'
}

X = range(10)
Y = [val ** 2 for val in X]
Z = [val ** 3 for val in X]
W = [val ** 4 for val in X]

plt.plot(X, Y, 'g-^', label='Quadrados')
plt.plot(X, W, 'ro', label='4 pontência')
plt.plot(X, Z, 'kD', label='Cubos')

plt.title('Gráfico Irado da live 90')

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.text(50, max(W), 'Meu melhor texto', bbox=box)

plt.legend()
plt.grid(True, lw=2, ls='--')

plt.show()
