from core.cache import Cache


class Repository:

    def ler_numeros(self):
        numeros = Cache().get_from_cache()

        if not numeros:
            file = open('../dados/numeros.csv', 'r')
            for linha in file:
                num_int, _ = linha.split(',')
                numeros.append(int(num_int))
            file.close()

            Cache().set_to_cache(numeros)

        return numeros
