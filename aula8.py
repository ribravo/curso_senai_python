# # função continue -> Pula o resto da iteração/não interrompe o loop

# for i in [1, 2, 3, 4, 5, 6]:
#     if i == 3:
#         continue
#     print(i)

# for i in [1, 2, 3, 4, 5, 6]:
#     if i == 3:
#         print("Pulando o numero 3...")
#         continue
#     print(i)

# # Pulando numeros pares:

# for i in range(11):
#     if i % 2 == 0:
#         continue
#     print(f"Numero impar: {i}")

# # Pulando numeros impares:

# for i in range(11):
#     if i % 2 != 0:
#         continue
#     print(f"Numero par: {i}")

# for i in [8, 10, -1, -7, 7, -5, 6]:
#     if i < 0:
#         print(f"Menor que 0: {i}")
#         continue
#     print(f"Maior que 0: {i}")

# # Função break -> Interrompe o looping

# for i in [1, 2, 3, 4, 5, 6]:
#     print(i)
#     if i == 3:
#         break

# print()

# for i in [1, 2, 3, 4, 5, 6]:
#     print(i)
#     if i == 3:
#         print(f"Numero {i} encontrado. Encerrando o loop... ")
#         break
# print("Fim do programa!!")

# nomes = ["Natan", "Alessandro", "Fernanda", "Julio", "Guilherme"]

# for nome in nomes:
#     if nome == "Fernanda":
#         print(f"{nome} nome encontrado!")
#         break
#     print(f"Verificando {nome}... ")


# nomes = ["Natan", "Alessandro", "Fernanda", "Julio", "Guilherme"]

# for nome in nomes:
#     if nome == "Julio":
#         print(f"{nome} nome encontrado!")
#         break
#     print(f"Verificando {nome}... ")
# else:
#     print(f"Carlos não encontrado")

# # utilizando "break" e "continue" juntos:

# for n in range(1, 8):
#     if n == 3:
#         print(f"Pulando o {n}...")
#         continue
#     if n == 6:
#         print(f"Numero {n} encontrado. Encerrando o looping...")
#         break
#     print(n)

# Loop alinhado:

# for x in range(1, 4):
#     for y in range(1, 4):
#         if y == 2:
#             break
#         print(f"x={x}, y={y}")

# # Exercicio tabuada

# num = int(input("Digite um numero: "))
# print()
# print(f"Tabuada do {num}")
# for i in range(1, 11):
#     res = i * num
#     print(f"{num} x {i} = {res}")

# # Exercicio 1

# for i in range(1, 101):
#     if i % 2 != 0:
#         continue
#     print(f"{i} é par")

# # Exercicio 2

# soma = 0

# for i in range(5):
#      num = float(input(f"Digite o {i + 1}º numero:  "))
#      soma += num
#      media = i + 1 # mesma coisa que soma + num

# res = soma / media
# print()
# print(f"Soma dos numeros: {soma}")
# print(f"Média dos numeros: {res}")

# Exercicio 3

alunos = int(input("Informe a quantiade de alunos na sala: "))
soma = 0

for i in range(alunos):
    num = int(input(f"Digite a idade do {1 + i}º aluno: "))
    soma += num

media = soma // alunos
print()
if media < 26:
    print(f"A idade média é {media}: Essa turma é jovem!")
elif media >= 26 and media <= 60:
    print(f"A idade média é {media}: Essa turma é adulta!")
else:
    print(f"A idade média é {media}: Essa turma é idosa")



