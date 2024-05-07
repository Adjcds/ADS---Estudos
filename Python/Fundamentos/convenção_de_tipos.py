## 1 - parte 1: Em alguns momentos será necessário conveter o tipo de uma variável para manipular de forma diferente. Por exemplo:
##  Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

# Numérico para string
preco = 10.50
idade = 28

print(str(preco))
# >>> 10.5

print (str(idade))
# >>> 28

texto = f"idade {idade} preco {preco}"
print(texto)
# >>> idade 28 preco 10.5

# String para número

precostr = "10.50"
idade = "28"

print(float(precostr))
# >>> 10.50

print(int(idade))
# >>> 28

# Erro de conversão 

precoerro = "python" #(é uma sequencia de caracteres)
print(float(precoerro))
# >>>
# Traceback (most recent call last):
#   File "conversão_de_tipos.py", line 31, in <module>
#       print(float(precoerro))
# ValueError: could not convert string to float: 'python'

