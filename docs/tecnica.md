## Documentação técnica

Segue uma breve documentação técnica explicando cada método utilizado no projeto desafio.


#### main.py

- [main.py](../src/main.py)

##### Main().ordenar(self, numeros):

Devolve uma lista de números ordenada.

##### Main().descobrir_num_faltando(self, num_ordenados):

Dada uma lista de números ordenada, descobre o número faltante caso exista.

##### Main().exibir(self, num_faltando):

Exibe mensagem caso o número faltante exista, caso contrário alerta que não há número faltante na lista.

##### Main().run(self):

Executa todas as etapas para descoberta de número faltante na lista.


#### repository.py

- [repository.py](../src/core/repository.py)

##### Repository().ler_numeros(self):

Recupera números a partir de algum repositório.
No momento está sendo usado como repositório um arquivo CSV.


#### cache.py

- [cache.py](../src/core/cache.py)

##### Cache()set_to_cache(self, numeros):

Salva lista de números no cache em memória.

##### Cache()get_from_cache(self):

Recupera lista de números do cache em memória.
