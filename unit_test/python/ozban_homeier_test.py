import unittest

from python.ozban_homeier import ozban_homeier


class TestOzbanHomeier(unittest.TestCase):

    def test_ozban_homeier(self):
        # Se prueba la restriccion en el formato de la funcion
        er_str_funcion = "La funcion debe ser un string"
        self.assertEqual(ozban_homeier(0, 0, 0, 2), er_str_funcion)

        # Se prueba la restriccion en el formato de xk
        er_x0 = "El xk debe ser un numero"
        self.assertEqual(ozban_homeier('x**2', 'a', 0, 0), er_x0)

        # Se prueba la restriccion en la tolerancia
        er_tol = "La tol debe ser un numero"
        self.assertEqual(ozban_homeier('x**2', 0, True, 0), er_tol)

        # Se prueba la restriccion en el valor de graph
        er_graph = 'La graph debe ser 0 (desactivado) o 1 (activado)'
        self.assertEqual(ozban_homeier('x + x', 0, 0, 'a'), er_graph)

        # Se prueba la sintaxis de la funcion
        er_sintaxis = "Sintaxis de la funcion es incorrecta"
        self.assertEqual(ozban_homeier('cos(2x)', 0, 0, 1), er_sintaxis)

        # Se prueba el resultado de una funcion
        funcion1 = 'cos(2*x)^2 - x^2'
        resultado1 = ozban_homeier(funcion1, 5 / 7, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado1, 4), 0.5149)

        # Se prueba el resultado de una funcion
        funcion2 = 'exp(x) - x - 2'
        resultado2 = ozban_homeier(funcion2, 3 / 4, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado2, 4), 1.1462)

        # Se prueba el resultado de una funcion
        funcion3 = 'cos(x)-x'
        resultado3 = ozban_homeier(funcion3, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado3, 4), 0.7391)

        # Se prueba el resultado de una funcion
        funcion4 = '(1 + x) * sin(x) - 1'
        resultado4 = ozban_homeier(funcion4, 1 / 5, 10 ** -5, 0)[0]
        self.assertEqual(round(resultado4, 4), 0.6508)

if __name__ == '__main__':
    unittest.main()