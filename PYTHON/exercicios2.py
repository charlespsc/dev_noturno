# 01 - Criar a variável
idade = input("Quantos anos voce tem? ")

# por estar em "" o valor é str
if int(idade) < 16:
    print("Menor")
elif int(idade) > 18:
    print("Maior")
else:
    print("Emancipado")


# 02 - Buscar a idade de nadador e classificar na tabela:
idade = input("Ola nadador! quantos anos voce tem? ")

if int(idade) > 4 and int(idade) < 8:
    print("Infantil A")
elif int(idade) > 7 and int(idade) < 11:
    print("Infantil B")
elif int(idade) > 10 and int(idade) < 14:
    print("Juvenil A")
elif int(idade) > 13 and int(idade) < 18:
    print("Juvenil B")
else:
    print("Voce nao pertence ao grupo de Natacao")
