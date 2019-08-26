import unittest

from SolNE.ud import *
from SolNE.fd import *


class TestSolNE(unittest.TestCase):
    ER_STR_FUNCION = "La funcion debe estar en un string"
    ER_X0 = "xk debe ser un numero"
    ER_A = "a debe ser un numero"
    ER_B = "b debe ser un numero"
    ER_A1 = "a1 debe ser un numero"
    ER_A2 = "a2 debe ser un numero"
    ER_B1 = "b1 debe ser un numero"
    ER_B2 = "b2 debe ser un numero"
    ER_ALPHA = "alpha debe ser un numero"
    ER_Y = "y debe ser un numero"
    ER_MAX_ITER1="max_iter debe ser un numero"
    ER_MAX_ITER2="max_iter debe ser un numero positivo"

    ER_TOL1 = "La tolerancia debe ser un numero"
    ER_TOL2 = "tol debe ser un numero positivo"
    ER_GRAPH = 'graph debe ser cero (desactivado) o uno (activado)'
    ER_SINTAXIS = "Sintaxis de la funcion es incorrecta"
    FUNCION1 = 'cos(2*x)**2 - x**2'
    FUNCION2 = 'exp(x) - x - 2'
    FUNCION3 = 'cos(x)-x'
    FUNCION4 = '(1 + x) * sin(x) - 1'
    FUNCION5 = 'x**3- x - 1'

    def test_sne_ud_1(self):
        """
        Metodo encargado de realizar el test de sne_ud_1
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_ud_1(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_ud_1('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_ud_1('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_ud_1('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_ud_1('x + x', 0, 0, 'v'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_ud_1('cos(x2)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_ud_1(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_ud_1(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_ud_1(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_ud_1(self.FUNCION4, 7 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_ud_2(self):
        """
        Metodo encargado de realizar el test de sne_ud_2
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_ud_2(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_ud_2('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_ud_2('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_ud_2('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_ud_2('x + x', 0, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_ud_2('cos(2x)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_ud_2(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_ud_2(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_ud_2(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_ud_2(self.FUNCION4, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_ud_3(self):
        """
        Metodo encargado de realizar el test de sne_ud_3
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_ud_3(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_ud_3('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_ud_3('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_ud_3('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_ud_3('x + x', 0, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_ud_3('cos(2x)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_ud_3(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_ud_3(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_ud_3(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_ud_3(self.FUNCION4, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_ud_4(self):
        """
        Metodo encargado de realizar el test de sne_ud_4
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_ud_4(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_ud_4('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_ud_4('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_ud_4('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_ud_4('x + x', 0, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_ud_4('cos(2x)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_ud_4(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_ud_4(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_ud_4(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_ud_4(self.FUNCION4, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6507)

    def test_sne_ud_5(self):
        """
        Metodo encargado de realizar el test de sne_ud_5
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_ud_5(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_ud_5('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_ud_5('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_ud_5('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_ud_5('x + x', 0, 0, 'v'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_ud_5('cos(x2)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_ud_5(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_ud_5(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_ud_5(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_ud_5(self.FUNCION4, 7 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_ud_6(self):
        """
        Metodo encargado de realizar el test de sne_ud_6
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_ud_6(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_ud_6('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_ud_6('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_ud_6('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_ud_6('x + x', 0, 0, 'v'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_ud_6('cos(x2)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_ud_6(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_ud_6(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_ud_6(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_ud_6(self.FUNCION4, 7 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_fd_1(self):
        """
        Metodo encargado de realizar el test de sne_fd_1
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_fd_1(0, 0, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_fd_1('x**2', 'a', 0, 0), self.ER_X0)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_fd_1('x**2', 0, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_fd_1('x + x', 0, -1, 1), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_fd_1('x + x', 0, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_fd_1('cos(x2)', 0, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_fd_1(self.FUNCION1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_fd_1(self.FUNCION2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_fd_1(self.FUNCION3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_fd_1(self.FUNCION4, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 2.881)

    def test_sne_fd_2(self):
        """
        Metodo encargado de realizar el test de sne_fd_2
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_fd_2(0, 0, 1, 0, 2), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_fd_2('x**2', 'a', 1, 0, 0), self.ER_X0)

        # Se prueba la restriccion en la constante y
        er_y = "La constante y no puede ser 0"
        self.assertEqual(sne_fd_2('x**2', 0, 0, 0, 0), er_y)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_fd_2('x**2', 0, 1, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_fd_2('x**2', 0, 1, -1, 0), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_fd_2('x + x', 0, 1, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_fd_2('cos(2x)', 0, 1, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_fd_2(self.FUNCION1, 5 / 7, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_fd_2(self.FUNCION2, 3 / 4, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_fd_2(self.FUNCION3, 1 / 5, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_fd_2(self.FUNCION4, 1 / 5, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_fd_4(self):
        """
        Metodo encargado de realizar el test de sne_fd_4
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_fd_4(0, 0, 1, 0, 0), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_fd_4('x**2', 'a', 1, 0, 0), self.ER_X0)

        # Se prueba la restriccion en la constante y
        self.assertEqual(sne_fd_4('x**2', 0, 'a', 0, 0), self.ER_Y)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_fd_4('x**2', 0, 1, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_fd_4('x**2', 0, 1, -1, 0), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_fd_4('x + x', 0, 1, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_fd_4('cos(2x)', 0, 1, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_fd_4(self.FUNCION1, 5 / 7, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        resultado2 = sne_fd_4(self.FUNCION2, 3 / 4, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_fd_4(self.FUNCION3, 1 / 5, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_fd_4(self.FUNCION4, 1 / 5, 1, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)
    def test_sne_fd_5(self):
        """
        Metodo encargado de realizar el test de sne_fd_5
        """
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_fd_5(0, 0, 1, 0, 0), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de a
        self.assertEqual(sne_fd_5('x**2', 'C', 1, 0, 0), self.ER_A)

        # Se prueba la restriccion en el formato de b
        self.assertEqual(sne_fd_5('x**2', -1, 'c', 0, 0), self.ER_B)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_fd_5('x**2', -1, 1, True, 0), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_fd_5('x**2', -1, 1, -1, 0), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_fd_5('x + x', -1, 1, 0, 'a'), self.ER_GRAPH)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_fd_5('cos(2x)', -1, 1, 0, 1), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_fd_5(self.FUNCION5, -1, 3, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 1.3247)

        # Se prueba el resultado de una funcion
        resultado2 = sne_fd_5(self.FUNCION2, -1, 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_fd_5(self.FUNCION3, -1, 3, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_fd_5(self.FUNCION4, -1, 2, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

    def test_sne_fd_6(self):
        """
        Metodo encargado de realizar el test de sne_fd_6
        """
        # sne_fd_6(str_funcion, xk,a1,a2,b1,b2, alpha, tol, graph=1, max_iter=200)
        # Se prueba la restriccion en el formato de la funcion
        self.assertEqual(sne_fd_6(2, 2, 1,2,3,4,0.5 ,5*10**-5,0,100), self.ER_STR_FUNCION)

        # Se prueba la restriccion en el formato de xk
        self.assertEqual(sne_fd_6("x**2", 'a', 1,2,3,4,0.5 ,5*10**-5,0,100), self.ER_X0)

        # Se prueba la restriccion en el formato de a1
        self.assertEqual(sne_fd_6("x**2", 2, 'a',2,3,4,0.5 ,5*10**-5,0,100), self.ER_A1)

        # Se prueba la restriccion en el formato de a2
        self.assertEqual(sne_fd_6("x**2", 2, 1,'a',3,4,0.5 ,5*10**-5,0,100), self.ER_A2)

        # Se prueba la restriccion en el formato de b1
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,'a',4,0.5 ,5*10**-5,0,100), self.ER_B1)

        # Se prueba la restriccion en el formato de b2
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,'a',0.5 ,5*10**-5,0,100), self.ER_B2)

        # Se prueba la restriccion en el formato de alpha
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,4,'a' ,5*10**-5,0,100), self.ER_ALPHA)

        # Se prueba la restriccion en la tolerancia
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,4,0.5 ,True,0,100), self.ER_TOL1)

        # Se pruena la restriccion en el valor de tol
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,4,0.5 ,-1,0,100), self.ER_TOL2)

        # Se prueba la restriccion en el valor de graph
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,4,0.5 ,5*10**-5,'a',100), self.ER_GRAPH)

        # Se prueba la restriccion en el formato de max_iter
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,4,0.5 ,5*10**-5,0,'a'), self.ER_MAX_ITER1)

        # Se prueba la restriccion en el valor de max_iter
        self.assertEqual(sne_fd_6("x**2", 2, 1,2,3,4,0.5 ,5*10**-5,0,-5), self.ER_MAX_ITER2)

        # Se prueba la sintaxis de la funcion
        self.assertEqual(sne_fd_6('cos(2x)', 2, 1,2,3,4,0.5 ,5*10**-5,0,100), self.ER_SINTAXIS)

        # Se prueba el resultado de una funcion
        resultado1 = sne_fd_6(self.FUNCION1, 2, 1,2,2.2,4,1 ,5*10**-5,0,100)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # # Se prueba el resultado de una funcion
        resultado2 = sne_fd_6(self.FUNCION2, 2, 1,2,2.2,4,1 ,5*10**-5,0,100)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        resultado3 = sne_fd_6(self.FUNCION3, 2, 1,2,2.2,4,1 ,5*10**-5,0,100)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        resultado4 = sne_fd_6(self.FUNCION5, 1, 1,2,2.2,4,1 ,5*10**-5,0,100)[0]
        self.assertEqual(round(resultado4, 4), 1.3247)

if __name__ == '__main__':
    unittest.main()
