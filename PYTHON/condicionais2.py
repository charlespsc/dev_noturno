# FORMAS de encurtar o código:

a = 5
b = 3
c = 2

"""
if a < b: print("a é menor que b")
print("código executado após o if")
# multiple statements on one line (colon)Flake8(E701)

"""
"""
# Em Python não existe o operador ternário como em outras linguagens,
# mas podemos usar uma expressão condicional.
print("a é menor que b") if a < b else print("a não é menor que b")

"""

if a > b:
    print("a é maior que b")
    if a > c:
        print("a é maior que b e que c")
