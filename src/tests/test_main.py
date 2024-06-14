import unittest

from main import Main


class TestMain(unittest.TestCase):

    def test_ordenar(self):
        numeros = [3, 4, 1, 2]
        ordenados = Main().ordenar(numeros)

        self.assertEqual(ordenados, [1, 2, 3, 4])

    def test_descobrir_num_faltando(self):
        num_ordenados = [1, 2, 4]
        num_faltando = Main().descobrir_num_faltando(num_ordenados)

        self.assertEqual(num_faltando, 3)
