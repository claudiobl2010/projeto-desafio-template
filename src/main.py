from core.repository import Repository


class Main:

    def ordenar(self, numeros):
        return sorted(numeros)

    def descobrir_num_faltando(self, num_ordenados):
        num_faltando = None

        for i in range(len(num_ordenados)):
            # Se chegou ao último indice da lista é pq não há número faltante.
            if i == (len(num_ordenados) - 1):
                break

            if num_ordenados[i] != (num_ordenados[i + 1] - 1):
                num_faltando = num_ordenados[i + 1] - 1
                break

        return num_faltando

    def exibir(self, num_faltando):
        if num_faltando:
            print('O número faltando na lista é:', num_faltando)
        else:
            print('Não existe número faltando na lista.')

    def run(self):
        numeros = Repository().ler_numeros()
        num_ordenados = self.ordenar(numeros)
        num_faltando = self.descobrir_num_faltando(num_ordenados)
        self.exibir(num_faltando)


if __name__ == '__main__':
    Main().run()
