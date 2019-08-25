# Importación del paquete simbólico de Python
from sympy import *
# Importación de la función para graficar
from solne.graficar_error import graficar_error
# Importación de la función común para verificar errores
from solne.verificar_errores import verificar_errores
# Importación de numpy para verificar que la función no se indefina
from numpy import isnan, isinf


def sne_ud_5(f, xk, tol, graph=1):
    """
    Metodo de Ostrowski de cuarto orden
    Obtenido de Construction of fourth-order optimal families of iterative methods and their dynamics
    (Bahl et all, 2015) ecuación (3.2)
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Verifica errores con los parámetros
    error = verificar_errores(f, xk, tol, graph)

    if error:
        return error

    # Contador de iteraciones
    iter = 0

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []

    funcion = sympify(f)  # Se obtiene la funcion del string
    df = diff(funcion, 'x').doit()  # Se deriva la funcion

    # Se evalua la sintaxis de la funcion evaluandola en xk
    float(funcion.subs({'x': xk}))
    float(df.subs({'x': xk}))

    while true:
        fxk = float(funcion.subs({'x': xk}))  # Se evalua la funcion

        if graph == 1:  # Se guardan los valores para la grafica
            lista_fxk += [abs(fxk)]
            lista_iter += [iter]

        if abs(fxk) <= tol:  # Se verifica la condicion de parada
            break

        # Se calcula el valor de xk en la derivada de f
        df_xk = float(df.subs({'x': xk}))

        if df_xk == 0:  # Se verifica para evitar division entre cero
            break

        # Calculo de Yk
        yk = float(xk - (fxk / df_xk))
        fyk = float(funcion.subs({'x': yk}))

        # Calculo del nuevo xk
        nuevo_xk = xk - (fxk / df_xk) * ((fxk - fyk)/(fxk - 2*fyk))
        if isnan(nuevo_xk) or isinf(nuevo_xk):
            print('Este metodo no es apto para la funcion ingresada')
            break

        xk = nuevo_xk
        iter += 1

    if graph == 1:
        graficar_error(lista_iter, lista_fxk)

    return [xk, iter]


def sne_ud_6(f, xk, tol, graph=1):
    """
    Metodo de Traub
    Obtenido de A new family of iterative methods widening areas of convergence
    (Budzko et all, 2014) ecuación (3)
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Verifica errores con los parámetros
    error = verificar_errores(f, xk, tol, graph)

    if error:
        return error

    # Contador de iteraciones
    iter = 0

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []

    funcion = sympify(f)  # Se obtiene la funcion del string
    df = diff(funcion, 'x').doit()  # Se deriva la funcion

    # Se evalua la sintaxis de la funcion evaluandola en xk
    float(funcion.subs({'x': xk}))
    float(df.subs({'x': xk}))

    while true:
        fxk = float(funcion.subs({'x': xk}))  # Se evalua la funcion

        if graph == 1:  # Se guardan los valores para la grafica
            lista_fxk += [abs(fxk)]
            lista_iter += [iter]

        if abs(fxk) <= tol:  # Se verifica la condicion de parada
            break

        # Se calcula el valor de xk en la derivada de f
        df_xk = float(df.subs({'x': xk}))

        if df_xk == 0:  # Se verifica para evitar division entre cero
            break

        # Calculo de Yk
        yk = float(xk - (fxk / df_xk))
        fyk = float(funcion.subs({'x': yk}))

        # Calculo del nuevo xk
        nuevo_xk = xk - ((fxk + fyk)/df_xk)
        if isnan(nuevo_xk) or isinf(nuevo_xk):
            print('Este metodo no es apto para la funcion ingresada')
            break

        xk = nuevo_xk
        iter += 1

    if graph == 1:
        graficar_error(lista_iter, lista_fxk)

    return [xk, iter]
