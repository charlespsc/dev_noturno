# Exemplo de strings em Python
# Exemplo de strings com aspas simples e duplas
string1 = "Olá, Mundo!"  # String com aspas duplas
string2 = 'Olá, Mundo!'  # String com aspas simples
print(string1)
print(string2)

"""Exemplo de string com aspas triplas"""
string3 = """Olá, Mundo!
Esta é uma string de múltiplas linhas.
Ela pode conter aspas simples ' e aspas duplas " sem problemas."""
print(string3)
# Exemplo de string com escape de caracteres
string4 = "Olá, Mundo!\nEsta é uma string com uma quebra de linha.\
Ela também pode conter aspas simples ' e aspas duplas \" sem problemas."
print(string4)
# Exemplo de string com escape de caracteres
string5 = 'Olá, Mundo!\nEsta é uma string com uma quebra de linha.\
Ela também pode conter aspas simples \' e aspas duplas " sem problemas.'
print(string5)

# Métodos de strings
b = " Python é uma linguagem de programação. "
print(b.strip())  # Remove espaços em branco no início e no final da string
print(b.lower())  # Converte a string para minúsculas
print(b.upper())  # Converte a string para maiúsculas
print(b.replace("Python", "Java"))  # Substitui "Python" por "Java"
print(b.split())  # Divide a string em uma lista de palavras
print(b.split(" "))  # Divide a string em uma lista de palavras usando espaço como delimitador
print(b.split("a"))  # Divide a string em uma lista de palavras usando "a" como delimitador
print(b.find("Python"))  # Encontra a posição da substring "Python" na string
print(b.index("Python"))  # Encontra a posição da substring "Python" na string (gera erro se não encontrar)
print(b.count("a"))  # Conta quantas vezes a letra "a" aparece na string
print(b.startswith(" Python"))  # Verifica se a string começa com " Python"
print(b.endswith("programação. "))  # Verifica se a string termina com "programação. "
print(b.isalpha())  # Verifica se a string contém apenas letras (retorna False porque contém espaços e pontuação)
print(b.isalnum())  # Verifica se a string contém apenas letras e números (retorna False porque contém espaços e pontuação)
print(b.isdigit())  # Verifica se a string contém apenas dígitos (retorna False porque contém letras e espaços)
print(b.islower())  # Verifica se a string está em minúsculas (retorna False porque contém letras maiúsculas)
print(b.isupper())  # Verifica se a string está em maiúsculas (retorna False porque contém letras minúsculas)
print(b.title())  # Converte a string para o formato de título (primeira letra de cada palavra em maiúscula)
print(b.capitalize())  # Converte a primeira letra da string para maiúscula e o resto para minúscula
print(b.center(50, '*'))  # Centraliza a string em um campo de 50 caracteres, preenchendo com '*'
print(b.ljust(50, '*'))  # Alinha a string à esquerda em um campo de 50 caracteres, preenchendo com '*'
print(b.rjust(50, '*'))  # Alinha a string à direita em um campo de 50 caracteres, preenchendo com '*'
print(b.zfill(50))  # Preenche a string com zeros à esquerda até atingir 50 caracteres
print(b.splitlines())  # Divide a string em uma lista de linhas
print(b.partition("Python"))  # Divide a string em três partes: antes, a substring "Python" e depois
print(b.rpartition("Python"))  # Divide a string em três partes: antes, a substring "Python" e depois (começando do final)
print(b.removeprefix(" Python"))  # Remove o prefixo " Python" da string
print(b.removesuffix("programação. "))  # Remove o sufixo "programação. " da string 

