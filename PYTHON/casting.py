# int 
x = int(2)  # Converte o número 2 para um inteiro
y = int(2.5)  # Converte o número 3.5 para um inteiro (resultado será 3)
z = int("2")  # Converte a string "10" para um inteiro
print(x, y, z)  # Exibe os valores

# float
x = float(2)  # Converte o número 2 para um float
y = float(2.5)  # Converte o número 2.5 para um float
z = float("2.5")  # Converte a string "2.5" para um float
w = float("2")  # Converte a string "2" para um float
print(x, y, z, w)  # Exibe os valores

# str
x = str(2)  # Converte o número 2 para uma string
y = str(2.5)  # Converte o número 2.5 para uma string
z = str("2")  # Converte a string "2" para uma string (sem alteração)
w = str(2 + 3j)  # Converte o número complexo 2 + 3j para uma string
print("A variavel x eh do tipo:", type(x), "e seu valor eh:", x)
print("A variavel y eh do tipo:", type(y), "e seu valor eh:", y)
print("A variavel z eh do tipo:", type(z), "e seu valor eh:", z)
print("A variavel w eh do tipo:", type(w), "e seu valor eh:", w)    