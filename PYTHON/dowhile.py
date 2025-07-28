"""
PROJETO Mini Game (do while)
Código para advinhar um número
"""
palpite = 0
numero = 7

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")


while True:  # Nós executamos sem verificar (= ao do while).
    print("Qual é o seu palpite?")
    palpite = int(input())
    if palpite == numero:  # Estamos verificando se o palpite é igual ao número
        print("Você acertou!")
        break
    else:
        print("Errado! Tente novamente.")
else:
    print("Erro na lógica do loop, isso não deve acontecer.")
    print(bool(palpite))

print("Parabéns! Você adivinhou o número:", numero)
print("Fim do jogo!")
