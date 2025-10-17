# 1

numero = int(input("Informe um numero inteiro: "))

quad = numero ** 2
print(f"O numero quadrado de {numero} é {quad}")

# 2

nome = input("Digite o nome: ")
sobrenome = input("Digite o sobrenome: ")
idade = int(input("Digite a idade: "))
ra = int(input("Digite o RA: "))
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média da nota de {nome} {sobrenome} é {media:.2f}")

# 3

numero = int(input("Digite um numero: "))

print(f"A tabuada do {numero} é:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")