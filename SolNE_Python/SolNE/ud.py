from sympy import diff, sympify
from numpy import isnan, isinf
from .graficar_error import graficar_error
from .verificar_restricciones import ver_restr_ud


def sne_ud_1(str_funcion, xk, tol, graph=1):
    """
    Metodo de Weerakoon-Fernando para encontrar el cero de una funcion
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Se verifican las restricciones en los argumentos
    restr = ver_restr_ud(str_funcion, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    funcion = sympify(str_funcion)  # Se obtiene la funcion del string
    df = diff(funcion, 'x')  # Se deriva la funcion

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
            # Se calcula el valor de xk en la derivada de f
            df_xk = float(df.doit().subs({'x': xk}))

            if df_xk == 0:  # Se verifica para evitar division entre cero
                break

            # Variable auxiliar para el calculo del denominador
            denominador_aux = float(xk - fxk / df_xk)

            # Se calcula el denominador entero
            denominador = float(df_xk + df.doit().subs({'x': denominador_aux}))

            # Si verifica denominador para evitar division entre cero
            if denominador == 0:
                break

            # Se verifica que el nuevo xk no se indefina
            nuevo_xk = xk - ((2 * fxk) / denominador)
            if isnan(nuevo_xk) or isinf(nuevo_xk):
                print('Este metodo no es apto para la funcion ingresada')
                break

            xk = nuevo_xk
            itr += 1

    if graph == 1:
        graficar_error(lista_iter, lista_fxk)

    return [xk, itr]


def sne_ud_2(f, xk, tol, graph=1):
    """
    Metodo de Chun-Kim para encontrar el cero de una funcion
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Se verifican las restricciones en los argumentos
    restr = ver_restr_ud(f, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    # Variable que contiene la conversión de la ecuación simbólica
    ec = sympify(f)
    # Variable que contiene la derivada de la función
    derivada_ec = diff(f, 'x')

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []

    # Se inicializa el contador de iteraciones
    ite = 0

    while 1:
        # Variable que contiene la imagen de xk en la función
        eval_ec = float(ec.subs('x', xk))

        # Se guardan los valores para la grafica
        if graph == 1:
            lista_fxk += [abs(eval_ec)]
            lista_iter += [ite]

        # Verificar la condición de parada si la imagen del xk es menor o
        # igual que la tolerancia
        if abs(eval_ec) <= tol:
            break
        # Si NO se cumple la condición de parada
        else:
            # Variable que contiene la imagen de xk en la derivada de la función
            eval_dec = float(derivada_ec.subs('x', xk))
            # Verificar que la imagen anterior no indefina el resultado
            if eval_dec == 0:
                return "La imagen de un xk en la derivada de la funcion se indefine"

            # Variable que contiene el resultado del metodo de Newton-Raphson
            nr = xk - (eval_ec / eval_dec)
            # Variable que contiene la imagen del nr en la derivada de la función
            eval_dec2 = float(derivada_ec.subs('x', nr))

            # Se calcula el xk+1 para la siguiente iteración
            xk = xk - (1 / 2) * (3 - (eval_dec2 / eval_dec)) * (eval_ec / eval_dec)
            # Se añade una iteración
            ite += 1

    # Si termina el ciclo, grafica el error y retorna el resultado
    if graph == 1:
        graficar_error(lista_iter, lista_fxk)
    # Se retorna el resultado final
    return [xk, ite]


def sne_ud_3(f, xk, tol, graph=1):
    """
    Metodo de Ozban-Homeier para encontrar el cero de una funcion
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Se verifican las restricciones en los argumentos
    restr = ver_restr_ud(f, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    # Variable que contiene la conversión de la ecuación simbólica
    ec = sympify(f)
    # Variable que contiene la derivada de la función
    derivada_ec = diff(f, 'x')

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []

    # Se inicializa el contador de iteraciones
    ite = 0

    while 1:
        # Variable que contiene la imagen de xk en la función
        eval_ec = float(ec.subs('x', xk))

        # Se guardan los valores para la grafica
        if graph == 1:
            lista_fxk += [abs(eval_ec)]
            lista_iter += [ite]

        # Verificar la condición de parada si la imagen del xk es menor o
        # igual que la tolerancia
        if abs(eval_ec) <= tol:
            break
        # Si NO se cumple la condición de parada
        else:
            # Variable que contiene la imagen de xk en la derivada de la función
            eval_dec = float(derivada_ec.subs('x', xk))
            # Verificar que la imagen anterior no indefina el resultado
            if eval_dec == 0:
                return "La imagen de un xk en la derivada de la funcion se indefine"

            # Variable que contiene el resultado del metodo de Newton-Raphson
            nr = xk - (eval_ec / eval_dec)
            # Variable que contiene la imagen del nr en la derivada de la función
            eval_dec2 = float(derivada_ec.subs('x', nr))
            # Verificar que la imagen anterior no indefina el resultado
            if eval_dec2 == 0:
                return "La imagen del Newton-Raphson en la derivada se indefine"

            # Se calcula el xk+1 para la siguiente iteración
            xk = xk - (1 / 2) * ((eval_ec / eval_dec) + (eval_ec / eval_dec2))
            # Se añade una iteración
            ite += 1

    # Si termina el ciclo, grafica el error y retorna el resultado
    if graph == 1:
        graficar_error(lista_iter, lista_fxk)
    # Se retorna el resultado final
    return [xk, ite]


def sne_ud_4(str_funcion, xk, tol, graph=1):
    """
    Metodo de Darvishi-Barati para encontrar el cero de una funcion
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """
    # Se verifican las restricciones en los argumentos
    restr = ver_restr_ud(str_funcion, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    funcion = sympify(str_funcion)  # Se obtiene la funcion del string
    df = diff(funcion, 'x')  # Se deriva la funcion

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
            # Se calcula el valor de xk en la derivada de f
            df_xk = float(df.doit().subs({'x': xk}))

            if df_xk == 0:  # Se verifica para evitar division entre cero
                break

            # Variable auxiliar para el calculo del numerador
            numerador_aux = float(xk - fxk / df_xk)

            # Se calcula el numerador
            numerador = float(funcion.subs({'x': numerador_aux}))

            # Se verifica que el nuevo xk no se indefina
            nuevo_xk = xk - (fxk / df_xk) - (numerador / df_xk)
            if isnan(nuevo_xk) or isinf(nuevo_xk):
                print('Este metodo no es apto para la funcion ingresada')
                break

            xk = nuevo_xk
            itr += 1

    if graph == 1:
        graficar_error(lista_iter, lista_fxk)

    return [xk, itr]
