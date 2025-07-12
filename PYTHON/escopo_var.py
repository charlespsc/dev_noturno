# Escopo de variáveis em Python

# Variáveis globais e locais

x = 10  # Variável global
y = 5  # Variável global

def funcao_exemplo():
    global x  # Declara que x é uma variável global
    x += 5  # Modifica a variável global x
    y = 20  # Variável local, só acessível dentro desta função
    print(f"Variável local y: {y}")
    print(f"Variável global x dentro da função: {x}")

funcao_exemplo()  # Chama a função que modifica x e imprime y
print(f"Variável global x fora da função: {x}")  # Imprime o valor de x fora da função  
# A variável y não pode ser acessada aqui, pois é local à função
print(f"Variável local y fora da função: {y}")  # Isso causaria um erro SE y não ESTIVER definida

