# # função while(Condição Verdadeira) -> Enquanto for verdadeira, faça...

# x = 0

# while x < 10:
#     print(x)
#     x += 1

# while True:
#     print("SENAI")
#     break

# Esperando condição do usuário
# senha = input("Digite a senha: ")

# while senha != "1234":
#     senha = input(f"Senha \"{senha}\" incorreta! Digite novemante: ")

# print("Acesso Liberado!!")

# # Loop infinito com break:

# while True:
#     cmd = input("Digite um comando: ").lower()
#     if cmd == "parar":
#         break
#     print("Você digitou: ", cmd)
# print("Programa encerrado!")

# # Validação de entrada:

# nota = float(input("Digite a nota: "))
# while nota < 0 or nota > 10:
#     nota = float(input("Insita uma nota de 0 à 10: "))
# print(f"Nota Registrada: {nota}")

# # Contagem progressiva

# n = 1

# while n <= 10:
#     print(n)
#     n += 1
# print("Contagem concluida")


# # Contagem regressiva

# n = 10

# while n >= 0:
#     print(n)
#     n -= 1
# print("Feliz Ano Novo")

# # Somar os numeros difitados:

# soma = 0
# resp = int(input("Digite um numero ou 0 para sair: "))

# while resp != 0:
#     soma += resp
#     resp = int(input("Digite outro numero ou 0 para sair: "))
#     print(f"Resultado parcial: {soma}")

# print(f"O resultado final é {soma}")

# # Tabuada em While

# n = int(input("Infore um numero: "))
# tab = 0

# while tab != 10:
#     tab += 1
#     res = n * tab
#     print(f"{tab} x {n} = {res}")

# # Maior numero digitado

# n = 1
# max = 0

# while n != 0:
#     n = int(input("Digite um numero ou 0 para sair: "))
#     if n > max:
#         max = n

# print(f"O maior numero digitado foi {max}")

# # Continue:

# cont = 0

# while cont < 10:
#     cont += 1
#     if cont == 5:
#         print("Pulou o", cont)
#         continue # Pula o 5
#     print(cont)

# # Montar um programa que solicite as notas, e faça a média

# i = 0
# nota = ""
# soma = 0
# ref = 0

# while nota != -1:
#     ref += 1
#     nota = float(input(f"Digite a {ref}º nota ou 0 para sair: "))
#     if nota != -1:
#         i += 1
#     soma += nota

# res = soma / i

# print(f"A média das notas é {res}")


i = 0
ref = 0
soma = 0

while True:
    ref += 1
    nota = float(input(f"Digite a {ref}º nota ou 0 para sair: "))
    if nota != -1:
        i += 1
    else:
        break
    soma += nota

res = soma / i

print(f"A média das notas é {res}")

total = 0
cont = 0

while True:
    nota = float(input("Digite a nota (ou -1 para encerrar: )"))
    if nota == 1:
        break
    total += nota
    cont += 1
media = total / cont
print(f"Média: {media}")
