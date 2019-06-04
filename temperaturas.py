
"""
Temperaturas

"""

# modificação 1

from csv import reader
from matplotlib import pyplot as plt
from matplotlib import  style


style.use('ggplot')

with open('data/temperaturas.csv') as file:
    parsed = reader(file)

    # print(next(parsed))
    # print(next(parsed))

    # Pegar todos os valores de 1999
    data_1999 = list(filter(lambda v: v[0] == '1999.0', parsed))

    # print(next(data_1999))

    # pegar todos os valores de máxima temperaturas e converter em float
    # se existirem (if v[3])
    max_temp = [float(v[3]) for v in data_1999 if v[3]]
    max_min = [float(v[4]) for v in data_1999 if v[4]]
    max_med = [float(v[5]) for v in data_1999 if v[5]]

    plt.plot(max_temp, label='MAX')
    plt.plot(max_min, label='MIN')
    plt.plot(max_med, label='MED')

    plt.title('Temperaturas de 1999 - Piracicaba SP')

    plt.xlabel('Dias do ano')
    plt.ylabel('Temperaturas')

    plt.grid(True)

    plt.legend()

    plt.show()
