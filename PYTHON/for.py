"""
Estrutura de repetição - LOOPS

- while
- for
- do while* (nao existe em Python)
- Switch* (nao existe em Python)

"""
# Estrutura de repetição - for
s = "pernambuco"

for i in s:
    print(i)

for i in range(6):
    print(i)

for i in range(5, 8):
    print(i)

for i in range(5, 20, 3):
    print(i)

for i in range(6):
    print(i)
else:
    print("Fim do loop")

for i in range(6):
    if i == 3:
        continue  # pula o valor 3
    print(i)
