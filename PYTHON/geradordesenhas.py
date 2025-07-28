"""
Gerador de Senhas Simples

# maiusculas, minusculas, numeros e simbolos

Security = chave
exemplo: 5ecur1ty

Podemos usar hexadecimal.

"""

chave = input("Digite a base da senha: ")

senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "@"
    elif letra in "Cc":
        senha = senha + "1."
    elif letra in "Dd":
        senha = senha + "1-3"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "$"
    elif letra in "Mm":
        senha = senha + "%"
    else:
        senha = senha + letra

print("Senha gerada:", senha)
