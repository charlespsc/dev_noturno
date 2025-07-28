"""
Exercício - Trocar valores de variáveis
"""

x = input("Digite o valor de x: ")
y = input("Digite o valor de y: ")

# Criando uma variável temporária para troca
temp = x
x = y
y = temp

print("Após a troca:")
print("x =", x)
print("y =", y)
