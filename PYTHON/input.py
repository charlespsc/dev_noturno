"""
Função input() - Função para entrada de dados do usuário

A concatenação de strings é feita com o operador (+) ou (,).
Outra forma de exibir mensagens é usando f-strings (f"texto {variável}").

"""
# Exemplo de uso da função input() para ler dados do usuário
print("Digite a cor favorita: ")
cor = "AZUL"
print("Sua cor favorita é: " + cor)  # Concatenação com o operador +
print("Sua cor favorita é:", cor)  # Concatenação com o operador ,

print("Digite seu nome: ")
nome = input()  # Lê a entrada do usuário e armazena na variável nome
print(f"Olá, {nome}!")  # Exibe uma mensagem de saudação com o nome do usuário.

# Outra forma de usar a função input:
idade = input("Digite sua idade: ")  # Solicita a idade do usuário
print(f"Você tem {idade} anos.")  # Exibe a idade informada pelo usuário.

# Outro exemplo de uso da função input:
altura = input("Digite sua altura: ")  # Solicita a altura do usuário
peso = input("Digite seu peso: ")  # Solicita o peso do usuário
print("Você tem {0} metros de altura e pesa {1} quilos.".format(altura, peso))
