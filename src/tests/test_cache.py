import unittest

from core.cache import Cache


class TestCache(unittest.TestCase):

    def setUp(self):
        self.cache = Cache()

    def test_cache_numeros(self):
        numeros = [1, 2, 3, 4]

        self.cache.set_to_cache(numeros)

        numeros_cached = self.cache.get_from_cache()

        self.assertEqual(numeros, numeros_cached)
