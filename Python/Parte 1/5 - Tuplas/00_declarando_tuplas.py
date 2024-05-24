# Uma tupla em Python é uma coleção ordenada de elementos, similar a uma lista, mas com uma diferença crucial: ela é imutável. Isso significa que, uma vez criada, uma tupla não pode ser modificada, adicionando, removendo ou alterando elementos. As tuplas são definidas utilizando parênteses `()`, embora os parênteses sejam opcionais em alguns contextos, e os elementos são separados por vírgulas.

# Por exemplo, uma tupla de números inteiros pode ser definida como `tupla_numeros = (1, 2, 3, 4, 5)`, uma tupla de strings como `tupla_strings = ("a", "b", "c", "d")`, e até mesmo uma tupla vazia como `tupla_vazia = ()`. 

# As tuplas podem conter elementos de diferentes tipos e até mesmo outras estruturas de dados, como outras tuplas. Por exemplo, `tupla_mista = ("python", 3.9, (1, 2, 3))`.

# As tuplas são frequentemente usadas em situações onde a imutabilidade é desejada, como para representar dados que não devem ser alterados, ou para retornar múltiplos valores de uma função. Além disso, elas consomem menos memória do que as listas e podem ser mais rápidas em algumas operações, devido à sua imutabilidade.

# Define uma tupla de frutas
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)  # ("laranja", "pera", "uva")

# Converte a string "python" em uma tupla de caracteres
letras = tuple("python")
print(letras)  # ('p', 'y', 't', 'h', 'o', 'n')

# Converte uma lista em uma tupla
numeros = tuple([1, 2, 3, 4])
print(numeros)  # (1, 2, 3, 4)

# Define uma tupla com um único elemento
pais = ("Brasil",)
print(pais)  # ("Brasil",)
