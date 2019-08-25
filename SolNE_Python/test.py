import unittest

from SolNE.ud import *
from SolNE.fd import *


class TestSolNE(unittest.TestCase):
    ER_STR_FUNCION = "La funcion debe estar en un string"
    ER_X0 = "xk debe ser un numero"
    ER_TOL1 = "La tolerancia debe ser un numero"
    ER_TOL2 = "tol debe ser un numero positivo"
    ER_GRAPH = 'graph debe ser cero (desactivado) o uno (activado)'
    ER_SINTAXIS = "Sintaxis de la funcion es incorrecta"
    FUNCION1 = 'cos(2*x)^2 - x^2'
    FUNCION2 = 'exp(x) - x - 2'
    FUNCION3 = 'cos(x)-x'
    FUNCION4 = '(1 + x) * sin(x) - 1'

    def test_sne_ud_1(self):
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

    def test_sne_fd_1(self):
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


if __name__ == '__main__':
    unittest.main()
