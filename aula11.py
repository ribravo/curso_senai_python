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

# lista = []

# for i in range(3):
#     lista.append(i)
#     lista.append(i + 10)
    
# print(lista)

# lista = []

# for i in range(3):
#     num = [i, i+10]
#     lista.extend(num)
    
# print(lista)

# # Fatiamentos -> Fatiamento serve para pegar partes especificas
# # Lista[inicio:fim:intervalo]

# num = [10, 20, 30, 40, 50, 60]
# print(num[1:5]) # fatiamento com inicio e fim
# print(num[:3]) # fatiamento com fim
# print(num[2:]) # fatiamento com inicio
# print(num[::2]) # fatiamento com intervalo
# print(num[-3:]) # fatiamento de traz para frente
# print(num[::-1]) # fatiamento de traz para frente. Como não tem inicio e fim, ele mostra todos os valores da lista em ordem decrescente

# nome = "SENAI"
# print([nome[0:3]]) # O resultado será tipo lista
# print([nome[-3:]])

# # Substituindo valores da lista
# num = [10, 20, 30, 40, 50, 60]
# print(num[3:7])
# num[1:4] = [2, 3, 4] # Substitui os valores dentro dessa posição
# print(num)


# num = [10, 20, 30, 40, 50, 60]
# print(num[:]) # Retorna a lista completa

# num = [10, 20, 30, 40, 50, 60]
# print(num[:])
# num[:] = []
# print(num) # Retorna a lista vazia


par = []
impar = []
lista = []


for i in range(1, 21):
    num = int(input(f"Digite o {i}º numero inteiro: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Os numeros informados são {lista}")
print(f"Numeros pares: {par}")
print(f"Numeros impares: {impar}")

# notas = []
# acima_media = 0

# for i in range(6):
#     for y in range(4):
#         nota = float(input(f"Digite a {y +1} nota do {i + 1} aluno: "))
#         notas.append(nota)
#     media = sum(notas) / 4
#     if media >= 7.0:
#         acima_media += 1
#     print(f"A média desse aluno é {media}")
#     notas = []

# print(f"{acima_media} alunos com nota maior ou igual a 7")
