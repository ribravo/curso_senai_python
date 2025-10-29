# Lista vazia

# numero = []
# print(numero)

# numero.append(1)
# numero.append(2)
# numero.append(3)
# numero.append(4)
# numero.append(5)
# numero.append(6)

# print(numero)

# # Usando Loop:

# numero = []
# for i in range (1, 101):
#     numero.append(i)
# print(numero)

# # Alternativa

# numero = []
# cont = 0

# while cont < 100:
#     cont += 1
#     numero.append(cont)
#     # print(numero)
# print(numero)


# lista de max 5 pessoas

# lista = []

# for i in range (5):
#     lista.append(input("Insira um nome: "))

# print(lista)

# lista = []

# for i in range (5):
#     nome = input("Digite um nome: ")
#     lista.append(nome)

# print(lista)

# for i in lista:
#     print(i)

# # Contagem regressiva

# lista = []

# for i in range(10, -1, -1):
#     lista.append(i)
# print(lista)

# lista = []

# for i in range(11):
#     lista.insert(0, i)
# print(lista)

# lista = []

# for i in range(11):
#     lista.append(i)
# lista.reverse()
# print(lista)

# lista = []
# numero = ""

# while numero != 0:
#     numero = int(input("Digite um numero ou 0 para sair: "))
#     if numero == 0:
#         continue
#     lista.append(numero)

# # print(lista)

# numeros = []

# while True:
#     num = int(input("Digite um numero ou 0 para sair: "))
#     if num == 0:
#         break
#     numeros.append(num)
#     print(numeros)

# print(sum(numeros))

# # Função extende() -> Adiciona vários valores de uma vez:

# marcas = ["Fiat", "Renault", "Ford", "Toyota"]
# novos = ["JAC", "BYD", "Chevrolet"]

# marcas.extend(novos)

# print(marcas)

lista = []

for i in range(3):
    lista.append(i)
    lista.append(i + 10)
    
print(lista)

lista = []

for i in range(3):
    num = [i, i+10]
    lista.extend(num)
    
print(lista)

