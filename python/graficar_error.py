from matplotlib import pyplot as plt

"""
Funcion para realizar la grafica de error, iteraciones vs | f(xk) |
:param eje_x: lista con todos los valores que deben graficarse en el eje x
:param eje_y: lista con todos los valores que deben graficarse en el eje y
"""


def graficar_error(eje_x, eje_y):
    plt.plot(eje_x, eje_y)  # Se asignan los valores a los ejes de coordenadas
    plt.xlabel('Iteracion')  # Se le coloca un nombre al eje x
    plt.ylabel('| f(xk) |')  # Se le coloca un nombre al eje y
    plt.show()  # Se despliega el grafico
