"""
Operadores lógicos em Python e o tipo booleano

Em ciência da computação, um valor booleano é um tipo de dado que pode ser:
- verdadeiro (True)
- falso (False).

Em Python, o tipo booleano é representado pela classe bool.

Os valores booleanos são frequentemente usados em expressões condicionais e
lógicas, como em estruturas de controle (if, while) e operações lógicas (and,
or, not).

"""

# Exemplo de operadores lógicos e tipo booleano
a = True
b = False
print(f"Valor de a: {a}, Tipo: {type(a)}")
print(f"Valor de b: {b}, Tipo: {type(b)}")

"""
TABELA VERDADE

Utilizando o "and" (E) lógico:
- True and True = True
- True and False = False
- False and True = False
- False and False = False

Utilizando o "or" (OU) lógico:
- True or True = True
- True or False = True
- False or True = True
- False or False = False

Utilizando o "not" (NÃO) lógico:
- not True = False
- not False = True

"""
# Exemplo de tabela verdade com operadores lógicos
nome_usuario = "admin"
senha_usuario = "1234"

usuario_autenticado = (nome_usuario == "admin") and (senha_usuario == "1234")
print(f"Usuário autenticado: {usuario_autenticado}")
