import SolNE
from sympy import sympify
from numpy import isnan, isinf
from .graficar_error import graficar_error
from .verificar_restricciones import ver_restr_fd


def sne_fd_1(str_funcion, xk, tol, graph=1):
    """
    Metodo de Steffensen para encontrar el cero de una funcion
    :param str_funcion: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Se verifican las restricciones en los argumentos
    restr = ver_restr_fd(str_funcion, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    funcion = sympify(str_funcion)  # Se obtiene la funcion del string

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
            denominador_aux = float(funcion.subs(
                {'x': (xk + fxk)}))  # Se evalua la funcion

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


def sne_fd_2(f, xk, y, tol, graph=1):
    """
    Metodo del M8 para encontrar el cero de una funcion
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param y: constante que es un numero real, excepto cero.
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """
    # Se verifican las restricciones generales en los argumentos
    restr = ver_restr_fd(f, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    # Verificar que la constante y no sea cero
    if y == 0:
        return "La constante y no puede ser 0"

    # Variable que contiene la conversión de la ecuación simbólica
    ec = sympify(f)

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
            # Se calcula el wk y su imagen en la función
            wk = xk + (y * eval_ec)
            eval_wec = float(ec.subs('x', wk))

            # Verificar que no se indefina yk
            if (eval_wec - eval_ec) == 0:
                return "El yk se indefine"
            # Se calcula el yk y su imagen en la función
            yk = xk - (y * (eval_ec ** 2 / (eval_wec - eval_ec)))
            eval_yec = float(ec.subs('x', yk))

            # Se calcula el zk y su imagen en la función
            z1 = ((wk - yk) / ((xk - yk) * y))
            z2 = ((xk - yk) / ((wk - yk) * y * eval_ec)) * eval_wec
            z3 = ((wk + xk - 2 * yk) / ((xk - yk) * (wk - yk))) * eval_yec
            # Verificar que no se indefina zk
            if (z1 - z2 - z3) == 0:
                return "El zk se indefine"
            zk = yk - (eval_yec / (z1 - z2 - z3))
            eval_zec = float(ec.subs('x', zk))

            # Se calcula el xk+1 para la siguiente iteración
            h1 = (((yk - zk) * (wk - zk))) / ((xk - zk) * y * (xk - yk))
            h2 = ((((yk - zk) * (xk - zk)) / ((wk - zk) * (wk - yk) * (wk * xk)))
                  * eval_wec)
            h3 = (((wk * xk) - (wk * xk) - (xk * zk) + zk ** 2) /
                  ((yk - wk) * (yk - xk) * (yk - zk))) * eval_yec
            h4 = (((wk * xk) + (wk * yk) - (2 * wk * zk) + (xk * yk) - (2 * xk * zk) -
                   (2 * yk * zk) + (3 * zk ** 2)) / ((zk - wk) * (zk - xk) * (zk - yk)) *
                  eval_zec)
            # Verificar que no se indefina el zk
            if (h1 + h2 + h3 + h4) == 0:
                return "El xk+1 se indefine"
            # Se calcula el xk+1 para la siguiente iteración
            xk = zk - (eval_zec / (h1 + h2 + h3 + h4))
            # Se añade una iteración
            ite += 1

    # Si termina el ciclo, grafica el error y retorna el resultado
    if graph == 1:
        graficar_error(lista_iter, lista_fxk)
    # Se retorna el resultado final
    return [xk, ite]


def sne_fd_3(f, xk, tol, graph=1):
    """
    Metodo IODF (Improved Ostrowski's method free from derivatives)
    Obtenido de Steffensentypemethodsforsolvingnonlinearequations
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """
    # Se verifican las restricciones generales en los argumentos
    restr = ver_restr_fd(f, xk, tol, graph)
    if restr != 0:  # Si es diferente de cero significa un error
        return restr

    # Variable que contiene la conversión de la ecuación simbólica
    ec = sympify(f)

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []

    # Se inicializa el contador de iteraciones
    ite = 0

    while 1:
        # Variable que contiene la imagen de xk en la función
        fxk = float(ec.subs('x', xk))

        # Se guardan los valores para la grafica
        if graph == 1:
            lista_fxk += [abs(fxk)]
            lista_iter += [ite]

        # Verificar la condición de parada si la imagen del xk es menor o
        # igual que la tolerancia
        if abs(fxk) <= tol:
            break

        # f(xk + f(xk))
        f_aux_1 = xk + fxk
        f_aux_1 = float(ec.subs('x', f_aux_1))

        # f(xk - f(xk))
        f_aux_2 = xk - fxk
        f_aux_2 = float(ec.subs('x', f_aux_2))

        # Calcular yk
        yk = xk - ((2*(fxk**2)) / (f_aux_1 - f_aux_2))
        fyk = float(ec.subs('x', yk))

        # Calcular zk
        zk = yk - ((yk - xk)/(2*fyk - fxk)) * fyk
        fzk = float(ec.subs('x', zk))

        # Calcular nuevo xk+1 para la siguiente iteración
        xk = zk - ((yk - xk) / (2*fyk - fxk)) * fzk
        # Se añade una iteración
        ite += 1

    # Si termina el ciclo, grafica el error y retorna el resultado
    if graph == 1:
        graficar_error(lista_iter, lista_fxk)
    # Se retorna el resultado final
    return [xk, ite]
