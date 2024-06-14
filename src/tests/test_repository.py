import unittest

from core.repository import Repository


class TestMain(unittest.TestCase):

    def setUp(self):
        self.repository = Repository()

    def test_ler_numeros(self):
        numeros = [3, 1, 5, 4, 2, 6, 8, 10, 9]

        numeros_lidos = self.repository.ler_numeros()

        self.assertEqual(numeros, numeros_lidos)
