import os

os.system('cls')

# # print("Olá Mundo!")

# # Variavel local -> declarada dentro de uma função:

# def exibir():
#     nome = "Ana"
#     print(f"Dentro da função: {nome}")

# exibir()

# # print(nome) # Não funciona, neste caso só existe dentro da função

# # Variavel global -> definida fora de uma função:

# nome = "João"

# def exibir_global():
#     print(f"Dentro da função: {nome}")

# exibir_global()

# print(f"Fora da função: {nome}")

# Alterar variavel global (sem global):
# Não pode modificar variavel dentro da função

# cont = 0

# def somar():
#     cont += 1 # Dessa forma vai dar erro
#     print(f"Dentro da função: {cont}")

# somar()

# # Alterar variavel global (sem global):

# cont = 0

# def somar():
#     global cont # Dizendo ao python que é a variavel global
#     cont += 1
#     print(f"Dentro da função: {cont}")

# somar()
# somar()

# print(f"Fora da função: {cont}")

# # Assim a função pode ser alterada o valor global

# # Local com o mesmo nome da global

# nome = "Bravo"
# def exibir_nome():
#     # global nome
#     nome = "Paulo"
#     print(f"Dentro da função: {nome}")

# exibir_nome()
# print(f"Fora da função: {nome}")

# # Misturando leituras e escritas:

# x = 100 # Variavel global

# def testar():
# #   x += 200 # Dá erro porque ele esta tentando incrementar em uma variavel que não exsite
#     global x # Quando inserido a função global, a variavel se torna local
#     # print("Antes", x)
#     x += 200 # Varivael local
#     print("Depois", x)


# testar()
# print(x)

# # Com return:

# def somar(x):
#     return x + 1
# cont = 0
# cont = somar(cont)

# print("Contador:", cont)

# # Input:

# def saudacao():
#     nome = input("Diga seu nome: ")
#     print(f"Olá, {nome}. Sejá bem-vindo")

# saudacao()

# # Input com return:

# def idades():
#     anos = int(input("Diga sua idade: "))
#     diaNasc = int(input("Diga o dia de nascimento: "))
#     mesNasc = int(input("Diga o mês de nascimento: "))
#     anoNasc = int(input("Diga o ano de nascimento: "))

#     return anos, diaNasc, mesNasc, anoNasc

# idade, dia, mes, ano = idades()

# print(f"Data de Nascimento {dia}/{mes}/{ano}. Idade: {idade}")

# def somar():
#     n1 = float(input("Digite o valor 1: "))
#     n2 = float(input("Digite o valor 2: "))
#     soma = n1 + n2
#     return soma

# res = somar()

# print(f"O resultado é {res}")

def calculadora():
    n1 = float(input("Digite o valor 1: "))
    n2 = float(input("Digite o valor 2: "))
    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    div = n1 / n2
    return soma, sub, mult, div

soma, sub, mult, div = calculadora()

print(f"O resultado da soma é {soma}")
print(f"O resultado da subtração é {sub}")
print(f"O resultado da muktiplicação é {mult}")
print(f"O resultado da divisão é {div}")
