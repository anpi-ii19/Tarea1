import unittest

from python.darvishi_barati import darvishi_barati


class TestDarvishiBarati(unittest.TestCase):

    def test_darvishi_barati(self):
        # Se prueba la restriccion en el formato de la funcion
        er_str_funcion = "La funcion debe estar en un string"
        self.assertEqual(darvishi_barati(0, 0, 0, 2), er_str_funcion)

        # Se prueba la restriccion en el formato de xk
        er_x0 = "xk debe ser un numero"
        self.assertEqual(darvishi_barati('x**2', 'a', 0, 0), er_x0)

        # Se prueba la restriccion en la tolerancia
        er_tol = "La tolerancia debe ser un numero"
        self.assertEqual(darvishi_barati('x**2', 0, True, 0), er_tol)

        # Se pruena la restriccion en el valor de graph
        er_graph = 'graph debe ser cero (desactivado) o uno (activado)'
        self.assertEqual(darvishi_barati('x + x', 0, 0, 'a'), er_graph)

        # Se prueba la sintaxis de la funcion
        er_sintaxis = "Sintaxis de la funcion es incorrecta"
        self.assertEqual(darvishi_barati('cos(x2)', 0, 0, 1), er_sintaxis)

        # Se prueba el resultado de una funcion
        funcion1 = 'cos(2*x)^2 - x^2'
        resultado1 = darvishi_barati(funcion1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        funcion2 = 'exp(x) - x - 2'
        resultado2 = darvishi_barati(funcion2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        funcion3 = 'cos(x)-x'
        resultado3 = darvishi_barati(funcion3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        funcion4 = '(1 + x) * sin(x) - 1'
        resultado4 = darvishi_barati(funcion4, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6507)


if __name__ == '__main__':
    unittest.main()
