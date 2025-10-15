# # Variavel = valor

# nome = "Ricardo" # string
# sobrenome = "Bravo"
# fullName = nome + " " + sobrenome #Concatenação

# # Boas Praticas de Variavel

# # nomeCompleto
# # nome_completo

# print(fullName)

# n1 = 10
# n2 = 4
# soma = n1 + n2

# print(soma)

# # Declaração de Variavel Multipla

# pessoa1 = "Ricardo"
# pessoa2 = "Juliano"
# pessoa3 = "Bravo"

# print(pessoa1)
# print(pessoa2)
# print(pessoa3)

# #Alternativa

# pessoa1, pessoa2, pessoa3 = "Ricardo", "Juliano", "Bravo"

# print(pessoa1)
# print(pessoa2)
# print(pessoa3)

# # Atribui o mesmo valor a variaveis diferente

# fruta1 = "Melancia"
# fruta2 = "Melancia"
# fruta3 = "Melancia"

# # Alternativa

# fruta1 = fruta2 = fruta3 = "Melancia"

# # print(fruta1)
# # print(fruta2)
# # print(fruta3)

# largura = 2
# altura = 4

# formula Perimetro Triangulo retangulo = P = 2*Largura + 2*Altura
# perimetro = 2 * largura + 2 * altura

# print(perimetro)

# # Operadores Básicos

# n1 = 25
# n2 = 35
# print(n1)

# print("Soma: ", n1 + n2)
# print("Subtração: ", n1 - n2)
# print("Multiplicação: ", n1 * n2)
# print("Divisão float: ", n1 / n2)
# print("Divisão inteira: ", n1 // n2)
# print("Resto da Divisão: ", n1 % n2)
# print("Potenciação: ", n1 ** n2)

# # Operadores com numero float

# print(1 + 3.4)
# print(1.1 + 3.4)
# print(type(5/3))
# print(5/3)
# print(type(5//3))
# print(5//3)
# print(type(5//3.0))

# Conversão:

print(int(9))
print(type(9))

print(float(9))
print(type(float(9)))

print(int(6.8))
print(type(int(6.8)))

print(int("2"))
print(type("2"))
print(type(int("2")))

print(202510459863)
print(type(202510459863))
print(str(202510459863))
print(type(str(202510459863)))

print(type(True)) # True -> verdadeiro, sim ou 1
print(type(int(True)))
print(int(True))

print(type(False)) # False -> falso, não ou 0
print(type(int(False)))
print(int(False))

# Dá para converter numeros 0 e 1 em Bool

print(type(0))
print(type(bool(0)))
print(bool(0))

# Função numericas:
# Round() -> Arredonda o numero para o inteiro mais proximo

print(3.1479879876464679876167)
print(round(3.1439879876464679876167, 2))
print(round(3.1432879876464679876167, 4))

print(round(4.6))
print(round(4.4))
print(round(4.567, 2))

# Abs() -> Retorma valor absoluto (sem sinal)

print(abs(-10))
print(abs(5))

#pow() -> Eleva um numero a uma potencia (igual a **)

print(pow(2, 3)) # Mesma coisa que 2**3

# sum() -> Realiza o somatorio de uma lista

numeros =  [10, 20, 30]
print(sum(numeros))

# max() e min() -> Descobrir o valor máximo e minimo

numeros =  [4, 7, -1, 9, 3]
print(max(numeros))
print(min(numeros))