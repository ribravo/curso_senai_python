import os

os.system("cls")

# # Funções:

# # Para criar uma função usamos a instrução def

# # EXEMPLO

# # print("Boa noite!")

# def saudacao():
#     print("Bom dia!")
#     print("Boa tade!")
#     print("Boa noite!")

# saudacao()

# # Sem função

# print("-" * 30)
# print("Cadastro de Clientes")
# print("-" * 30)

# # Com função

# def linhas():
#     print("-" * 30)

# def titulos():
#     linhas()
#     print("Cadastro de alimentos")
#     linhas()
#     linhas()
#     print("Cadastro de clientes")
#     linhas()
#     linhas()
#     print("Cadastro de vendas")
#     linhas()

# titulos()

# # Função com paramêtro:

def linhas():
    print("*" * 30)

# def titulos(texto):
#     linhas()
#     print(texto)
#     linhas()

# titulos("Cadastro de clientes")

# titulos("Cadastro de alimentos")

# titulos("Cadastro de vendas")

# # Não é boa prática usar a função como variavel. Porque quando precisar chamar a função vai dar erro:

# # Ex:
# # titulos = "Bravo"
# # titulos("Cadastro de Vandas")

# def cumprimentos(nome):
#     print(f"Olá {nome}! Seja bem-vindo(a)")

# linhas()
# cumprimentos("Ana")
# linhas()
# cumprimentos("Matheus")
# linhas()
# cumprimentos("João")
# linhas()


# for i in range(3):
#     nome = input("Informe um nome: ")
#     cumprimentos(nome)

# def valida(num):
#     if num % 2 == 0:
#         print(f"{num} é par")
#     else:
#         print(f"{num} é impar")

# num = int(input("Informe um numero: "))

# valida(num)

# # Função com retorno:

# def somar(n1,n2):
#     return n1 + n2

# print(f"A soma é: {somar(5, 3)}")

# res = somar(10, 3)

# print(f"A soma é: {res}")

# def div(n1,n2):
#     return n1 / n2

# print(div(10, 2))

# # Função com condicional:

# def validar(idade):
#     if idade >= 18:
#         return "Maior de Idade"
#     else:
#         return "Menor de Idade"
    
# id = int(input("Digite a idade: "))
    
# print(validar(id))
# print(validar(16))

# # Função sem return:
# # Nesse caso não daria para utilizar o print para exibir o resultado da função
# def somar(a, b):
#     print(a + b)

# somar(4, 7)
# # print({somar(4, 7)}) # Dá erro

# # Se fosse guardar o resultado em uma variavel?
# res = somar(4, 7)
# print(res) # Dá erro

# # Para corrigir, utilizamos o return:
# def somar(a, b):
#     return a + b
# print(somar(4, 7))

# res = somar(4, 7)

# print(res + 10)

# # Nota de aluno (sem return):

# def calcular(n1, n2):
#     print(f"A média é {(n1+n2)/2}")
# calcular(8,6)

# if calcular >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

# Dá erro, o correto é utilizar o retorn

# # Nota de aluno com return:

# def calcular(n1, n2):
#     return (n1 + n2) / 2

# media = calcular(8, 6)

# if media >= 7:
#     print("Aprovado")
# else:
#     print("Reprovado")

# # Resumindo
# # Funções com return -> entregam resultado para o programa.
# # Funções sem return -> apenas execultam uma tarefa.

# # Exemplo usando as duas:

# def somar(a, b):
#     return a + b

# def resultado(res):
#     print(f"O resultado é {res}")
    
# valor = somar(5,3)

# resultado(valor)

# Função com loop

def cont(num):
    for i in range(1, num + 1):
        print(i)

cont(5)