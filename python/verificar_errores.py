# Importación del paquete simbólico de Python
from sympy import *


def verificar_errores(f, xk, tol, graph):
    """
    Función para verificar que los parámetros de las funciones sean los correctos
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: string de error si lo hay, 0 si no lo hay
    """
    # Se verifica el tipo de str_funcion
    if type(f) != str:
        return "La funcion debe estar en un string"

    # Se verifica el tipo de xk
    if type(xk) != int and type(xk) != float:
        return "xk debe ser un numero"

    # Se verifica el tipo de la tolerancia
    if type(tol) != int and type(tol) != float:
        return "La tolerancia debe ser un numero"

    # Se verifica que la tolerancia sea un numero positivo
    if tol < 0:
        return "tol debe ser un numero positivo"

    # Se verifica que el valor de graph sea uno o cero
    if graph != 1 and graph != 0:
        return "graph debe ser cero (desactivado) o uno (activado)"

    try:
        funcion = sympify(f)  # Se obtiene la funcion del string
        df = diff(funcion, 'x')  # Se deriva la funcion

        # Se evalua la sintaxis de la funcion evaluandola en xk
        float(funcion.subs({'x': xk}))
        float(df.doit().subs({'x': xk}))

    except:
        return "Sintaxis de la funcion es incorrecta"

    return 0
