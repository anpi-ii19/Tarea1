from sympy import diff, sympify


def verificar_restricciones(str_funcion, xk, tol, graph):
    """
    Verifica las restricciones en los argumentos de los metodos
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: 0 si se cumplen las restricciones, o el string con el error
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

    # Se verifica que la tolerancia sea un numero positivo
    if tol < 0:
        return "tol debe ser un numero positivo"

    # Se verifica que el valor de graph sea uno o cero
    if graph != 1 and graph != 0:
        return "graph debe ser cero (desactivado) o uno (activado)"

    return 0


def ver_restr_ud(str_funcion, xk, tol, graph):
    """
    Verifica las restricciones de los metodos que usan derivada
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: 0 si se cumplen las restricciones, o el string con el error
    """
    # Se verifican las restricciones generales
    restr = verificar_restricciones(str_funcion, xk, tol, graph)

    if restr != 0:
        return restr

    # Se verifican las restricciones de las funciones que usan derivada
    try:
        funcion = sympify(str_funcion)  # Se obtiene la funcion del string
        df = diff(funcion, 'x')  # Se deriva la funcion

        # Se evalua la sintaxis de la funcion evaluandola en xk
        float(funcion.subs({'x': xk}))
        float(df.doit().subs({'x': xk}))

    except:
        return "Sintaxis de la funcion es incorrecta"

    return 0


def ver_restr_fd(str_funcion, xk, tol, graph):
    """
    Verifica las restricciones de los metodos que no usan derivada
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: 0 si se cumplen las restricciones, o el string con el error
    """
    # Se verifican las restricciones generales
    restr = verificar_restricciones(str_funcion, xk, tol, graph)

    if restr != 0:
        return restr

    # Se verifican las restricciones de las funciones que usan derivada
    try:
        funcion = sympify(str_funcion)  # Se obtiene la funcion del string

        # Se evalua la sintaxis de la funcion evaluandola en xk
        float(funcion.subs({'x': xk}))

    except:
        return "Sintaxis de la funcion es incorrecta"

    return 0
