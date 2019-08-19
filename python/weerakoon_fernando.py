# M1 - Weerakoon and Fernando (2000), Articulo1.pdf pag 2

from sympy import Derivative, sympify
from python.graficar_error import graficar_error

"""
Metodo de Weerakoon-Fernando para encontrar el cero de una funcion
:param str_funcion: string con la funcion que se debe evaluar
:param xk: valor de x inicial con el cual aplicar el metodo
:param tol: tolerancia al fallo de debe tener el resultado final
:returns: lista con dos elementos, xk calculado y numero iteraciones
"""


def weerakoon_fernando(str_funcion, xk, tol, graph=1):
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
        df = Derivative(funcion, 'x')  # Se deriva la funcion
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
                # Se calcula el xk de la siguiente iteracion
                numerador = 2 * fxk

                # Primera parte del denominador
                denominador1 = float(df.doit().subs({'x': xk}))

                # Segunda parte del denominador
                denominador2 = float(xk - fxk / (df.doit().subs({'x': xk})))

                # Se calcula el denominador entero
                denominador = float(denominador1 + df.doit().subs({'x': denominador2}))

                # Si verifica denominador para evitar division entre cero
                if denominador == 0:
                    break

                xk = xk - (numerador / denominador)
                itr += 1

        if graph == 1:
            graficar_error(lista_iter, lista_fxk)

        return [xk, itr]

    except:
        return "Sintaxis de la funcion es incorrecta"
