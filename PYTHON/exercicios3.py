"""
01 - Implemente um programa que receba a idade de uma pessoa e imprima uma
mensagem de acordo com os critérios:
- Menor de 16 anos: MENOR
- Entre 16 e 18 anos: EMANCIPADO
- Maior de 18 anos: MAIOR
"""
idade = input("Quantos anos você tem? ")
if int(idade) < 16:
    print("Menor")
elif 16 <= int(idade) <= 18:
    print("Emancipado")
else:
    print("Maior")

"""
02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras:

Categorias:
- Infantil A: 5 a 7 anos
- Infantil B: 8 a 10 anos
- Juvenil A: 11 a 13 anos
- Juvenil B: 14 a 17 anos
- Acima de 17 anos: Não pertence ao grupo de natação
"""
idade = input("Olá nadador! Quantos anos você tem? ")
if 5 <= int(idade) <= 7:
    print("Infantil A")
elif 8 <= int(idade) <= 10:
    print("Infantil B")
elif 11 <= int(idade) <= 13:
    print("Juvenil A")
elif 14 <= int(idade) <= 17:
    print("Juvenil B")
else:
    print("Você não pertence ao grupo de Natação")
