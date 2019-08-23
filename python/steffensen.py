# 1-s2.0-S0096300311002748-main.pdf pag 1

from sympy import sympify
from numpy import isnan, isinf
from python.graficar_error import graficar_error


def steffensen(str_funcion, xk, tol, graph=1):
    """
    Metodo de Steffensen para encontrar el cero de una funcion
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Se verifica el tipo de str_funcion
    if type(str_funcion) != str:
        return "La funcion debe estar en un string"

    # Se verifica el tipo de xk
    if type(xk) != int and type(xk) != float:
        return "xk debe ser un numero"

    # Se verifica el tipo de la tolerancia
    if type(tol) != int and type(tol) != float:
        return "La tolerancia debe ser un numero"

    # Se verifica que el valor de graph sea uno o cero
    if graph != 1 and graph != 0:
        return "graph debe ser cero (desactivado) o uno (activado)"

    try:
        funcion = sympify(str_funcion)  # Se obtiene la funcion del string

        # Se evalua la sintaxis de la funcion evaluandola en xk
        float(funcion.subs({'x': xk}))

    except:
        return "Sintaxis de la funcion es incorrecta"

    itr = 0  # Se inicializa el contador de iteraciones

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []

    while 1:
        fxk = float(funcion.subs({'x': xk}))  # Se evalua la funcion

        if graph == 1:  # Se guardan los valores para la grafica
            lista_fxk += [abs(fxk)]
            lista_iter += [itr]

        if abs(fxk) <= tol:  # Se verifica la condicion de parada
            break

        else:
            # Variable auxiliar para el calculo del denominador
            denominador_aux = float(funcion.subs({'x': (xk + fxk)}))  # Se evalua la funcion

            # Se calcula el denominador entero
            denominador = denominador_aux - fxk

            # Se verifica denominador para evitar division entre cero
            if denominador == 0:
                break

            # Se verifica que el nuevo xk no se indefina
            nuevo_xk = xk - ((fxk ** 2) / denominador)
            if isnan(nuevo_xk) or isinf(nuevo_xk):
                print('Este metodo no es apto para la funcion ingresada')
                break

            xk = nuevo_xk
            itr += 1

    if graph == 1:
        graficar_error(lista_iter, lista_fxk)

    return [xk, itr]

