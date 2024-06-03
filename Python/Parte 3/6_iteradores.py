# Define uma classe chamada 'MeuIterador' que implementa um iterador personalizado
class MeuIterador:
    # Método de inicialização da classe, aceita uma lista de inteiros como argumento
    def __init__(self, numeros: list[int]):
        self.numeros = numeros  # Atribui a lista de inteiros à variável de instância 'numeros'
        self.contador = 0  # Inicializa o contador com 0

    # Método '__iter__' retorna o próprio objeto iterador
    def __iter__(self):
        return self

    # Método '__next__' retorna o próximo valor na sequência ou levanta uma exceção 'StopIteration' quando não houver mais elementos
    def __next__(self):
        try:
            # Obtém o número atual da lista usando o contador
            numero = self.numeros[self.contador]
            # Incrementa o contador para a próxima chamada de '__next__'
            self.contador += 1
            # Retorna o número multiplicado por 2
            return numero * 2
        except IndexError:
            # Levanta a exceção 'StopIteration' quando o contador ultrapassar o tamanho da lista
            raise StopIteration

# Cria uma instância de 'MeuIterador' com a lista de números [38, 13, 11]
# Usa um loop 'for' para iterar através do objeto 'MeuIterador'
for i in MeuIterador(numeros=[38, 13, 11]):
    # Imprime o valor retornado por cada iteração
    print(i)
