# == Igualdade
# != Diferente
# < Menor que
# <= Menor ou Igual
# > Maior que
# >= Maior ou igual

# Condicionais:

# # if -> Se
# # if (Condição) -> Sempre vai ser verdadeiro
# if (True):
#     print("Verdadeira")
# # else -> Senão
# # elif -> Se-Senão-Se
# Indentações são as tabulações/bloco de codigo

# idade = int(input("Digite a idade: "))

# if (idade >= 18):
#     print("Maior de Idade")
# print("Fim do Programa")

# media = float(input("Digite a média: "))

# if (media >= 7):
#     print("Aprovado!")

# Else -> Senão - Não precisa de condição

# idade = int(input("Digite a idade: "))

# if (idade >= 18):
#     print("Maior de Idade")
# else:
#     print("Menor de idade")
# print("Fim do Programa")


# media = float(input("Digite a média: "))

# if (media >= 7):
#     print("Aprovado!")
# else:
#     print("Reprovado")
# print("Fim do Programa")

# elif -> Senão-se

# nota = int(input("Digite a nota: "))

# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Bom!")
# elif nota >= 5:
#     print("Regular!")
# else:
#     print("Reprovado")


# "if" pode ser declarado sozinha, mas "elif" e "else" não
# Todo "elif" e "else" tem um "if". Mas nem todo "if" tem "elif" e "else"

# nota = int(input("Digite a nota: "))

# if nota >= 9:
#     print("Excelente!")
# if nota >= 7:
#     print("Bom!")
# if nota >= 5:
#     print("Regular!")
# if nota >= 0:
#     print("Reprovado")
# # Cada "if" é testado separadamente

# idade = int(input("Digite a Idade: "))

# if idade >= 18:
#     print("Menor de idade")
# if idade < 18:
#     print("Menor de idade")
# if idade == 20:
#     print("Tem extamente 20")


# # if aninhado:

# usuario = input("Digite o usuário: ")

# if usuario == "admin":
#     senha = input("Digite a senha: ")
#     if senha == "1234":
#         print("Acesso permitido!")
#     else:
#         print("Senha incorreta!")
# else:
#     print("Usuário incorreto!")


# usuario = input("Digite o usuário: ")
# senha = input("Digite a senha: ")

# if (usuario == "admin") and (senha == "1234"):
#     print("Acesso permitido!")
# else:
#     print("Usuário ou senha invádio")

# if de uma linha
idade = int(input("Digite a idade: "))
print("Maior de idade") if idade >= 18 else print("Menor de idade")
