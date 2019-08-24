# Importación del paquete simbólico de Python
from sympy import *
# Importación de la función para graficar
from Tarea1.graficar_error import graficar_error

def chun_kim(f, xk, tol, graph = 1):
    """
    Metodo de Chun-Kim para encontrar el cero de una funcion
    :param f: string con la funcion que se debe evaluar
    :param xk: valor de x inicial con el cual aplicar el metodo
    :param tol: tolerancia al fallo de debe tener el resultado final
    :param graph: valor 0 para no graficar o 1 para graficar
    :returns: lista con dos elementos, xk calculado y numero iteraciones
    """

    # Verificar que la función sea un string
    if type(f) != str:
        return "La función debe ser un string"

    # Verificar que x0 sea un float
    if type(xk) != float:
        return "El x0 debe ser un número"

    # Verificar que tol sea un float
    if type(tol) != float:
        return "La tol deber ser un número"

    # Verificar que el valor de graph
    if graph != 1 and graph != 0:
        return "La graph debe ser 0 (desactivado) o 1 (activado)"

    try:
        # Variable que contiene la conversión de la ecuación simbólica
        ec = sympify(f)
    except:
        return "Sintaxis de la función es incorrecta"

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
            # Variable que contiene la derivada de la función
            derivada_ec = diff(f, 'x')

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
            xk = xk - (1/2) * (3 - (eval_dec2 / eval_dec)) * (eval_ec / eval_dec)
            # Se añade una iteración
            ite += 1

    #Si termina el ciclo, grafica el error y retorna el resultado
    if graph == 1:
        graficar_error(lista_iter, lista_fxk)
    return [xk, ite]

#Ejemplo de prueba para el método de Chun-Kim
g = '(cos(2*x))**2 - (x**2)'
print(chun_kim(g, 3/4, 10**-5, 1))
