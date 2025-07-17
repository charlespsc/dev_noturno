"""
Exercícios de Python

Obs.: Todos os exercícios devem utilizar a função input(),
de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais,
     qual será o valor do mesmo com desconto de (??)%.
04 - área de um círculo (pi = 3,141592)
05 - conversão de reais para dólares
06 - conversão de dólares para reais
"""
# Exercício 01 - Área de um retângulo:

print("Calcule a area de um retângulo em metros")

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura

print(f"A área do retângulo é: {area} m²")

# Exercício 02 - Área de um quadrado:
print("Calcule a área de um quadrado em metros")
lado = float(input("Digite o lado do quadrado: "))
area_quadrado = lado ** 2
print(f"A área do quadrado é: {area_quadrado} m²")

# Exercício 03 - Valor do produto com desconto:
print("Calcule o valor de um produto com desconto")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_com_desconto = preco - (preco * desconto / 100)
print(f"O valor do produto com desconto é: R$ {valor_com_desconto:.2f}")

# Exercício 04 - Área de um círculo:
print("Calcule a área de um círculo em metros")
raio = float(input("Digite o raio do círculo: "))
pi = 3.141592
area_circulo = pi * (raio ** 2)
print(f"A área do círculo é: {area_circulo:.2f} m²")

# Exercício 05 - Conversão de reais para dólares:
print("Converta reais para dólares")
valor_reais = float(input("Digite o valor em reais: "))
taxa_cambio = float(input("Digite a taxa de câmbio (R$ para US$): "))
valor_dolares = valor_reais / taxa_cambio
print(f"O valor em dólares é: US$ {valor_dolares:.2f}")

# Exercício 06 - Conversão de dólares para reais:
print("Converta dólares para reais")
valor_dolares = float(input("Digite o valor em dólares: "))
taxa_cambio = float(input("Digite a taxa de câmbio (US$ para R$): "))
valor_reais = valor_dolares * taxa_cambio
print(f"O valor em reais é: R$ {valor_reais:.2f}")

# Fim dos exercícios
