"""
Operadores de comparação em Python

Operador de igualdade (==)
Operador de desigualdade (!=)
Operador maior que (>)
Operador menor que (<)
Operador maior ou igual a (>=)
Operador menor ou igual a (<=)

Operador de identidade (is)
Operador de não identidade (is not)
Operador de associação (in)
Operador de não associação (not in)

"""

# Exemplo de operadores de comparação
a = 10
b = 20
print(f"{a} == {b}: {a == b}")  # Igualdade
print(f"{a} != {b}: {a != b}")  # Desigualdade
print(f"{a} > {b}: {a > b}")    # Maior que
print(f"{a} < {b}: {a < b}")    # Menor que
print(f"{a} >= {b}: {a >= b}")  # Maior ou igual a
print(f"{a} <= {b}: {a <= b}")  # Menor ou igual a

# Exemplo de operadores de identidade
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(f"x is y: {x is y}")      # x e y são o mesmo objeto
print(f"x is z: {x is z}")      # x e z são objetos
print(f"x is not z: {x is not z}")  # x e z não são o mesmo objeto

# Exemplo de operadores de associação
frutas = ['maçã', 'banana', 'laranja']
print(f"maçã in frutas: {'maçã' in frutas}")  # 'maçã' está na lista
print(f"uva not in frutas: {'uva' not in frutas}")  # 'uva' não está na lista

nome = "Python"
print(f"nome in 'Python': {'P' in nome}")  # 'Python' está na string
print(f"Java not in nome: {'Java' not in nome}")  # 'Java' não está na string
