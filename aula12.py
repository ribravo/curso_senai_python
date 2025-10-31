# # Tuplas são semelhantes as listas, porem é imutável. Não pode ser adicionado, modificado ou removido valores.
# # Tuplas são dados fisicos

# linguagens = ("Assembly", "Cobol", "C", "C++")
# print(linguagens)

# linguagens = "Python", "Java", "Go", "C#"
# print(linguagens)
# print(linguagens[2])
# print(linguagens[1:3])

# for i in linguagens:
#     print(i)

# lista_linguagens = list(linguagens)
# print(lista_linguagens)

# lista = ["Vermelho", "Azul", "Amarelo", "Laranja"]
# lista.append("Verde")
# lista[0] = "Preto"
# print(lista)

# # Listas são mutáveis

# tupla = ("Vermelho", "Azul", "Amarelo", "Laranja")
# print(tupla)
# print(tupla[0])

# tupla = ()
# print(tupla)
# print(type(tupla))

# tupla = ("Bravo") # Dessa forma a variavel se torna uma string. Para ser uma tupla precisa de ao menos uma ","
# print(tupla)
# print(type(tupla))

# # Tupla sem parenteses (empacotamento):

# tupla = "Bravo", "Ricardo"
# print(type(tupla))
# print(tupla)

# # Posição e fatiamento:
# num = 10, 20, 30, 40, 50
# print(num[2])
# print(num[-1])
# print(num[1:4])

# # Iterando
# tupla = ("Vermelho", "Azul", "Amarelo", "Laranja")

# for i in tupla:
#     print(i, end=", ")

# print()

# # Verificar valor na tupla

# tupla = ("Vermelho", "Azul", "Amarelo", "Laranja")

# cor = input("Digite a cor: ").capitalize()

# if cor in tupla:
#     print("SIM")
# else:
#     print("NÃO")


# # Verificar quantidade e posição
# num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 5, 6, 2, 8, 2)
# print("Quantidade: ", num.count(2))
# print("Posição: ", num.index(3))

# # Concatenar tuplas:

# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)
# concat = tupla1 + tupla2
# print(concat)

# # Desempacotamento:

# tuplaCarros = ("Uno", "Ranger", "Golf")
# carro3, carro1, carro2 = tuplaCarros

# print(f"Carro 1: {carro1}")
# print(f"Carro 2: {carro2}")
# print(f"Carro 3: {carro3}")

# print(type(carro3))

# pessoa = ("Bravo", 25, 1.85)
# nome, idade, altura = pessoa
# print(type(nome))
# print(type(idade))
# print(type(altura))

# # Desempacotamento em sequencia:

# tuplaCarros = ("Uno", "Ranger", "Golf", "Tucson", "Elantra", "Fiesta")
# carros1, *carros = tuplaCarros
# print(carros1)
# print(*carros)

# # Desempacotamento fora de  sequencia:

# tuplaCarros = ("Uno", "Ranger", "Golf", "Tucson", "Elantra", "Fiesta")
# *carros, carro1, carro2 = tuplaCarros
# print(*carros)
# print(carro1)
# print(carro2)

# tuplaCarros = ("Uno", "Ranger", "Golf", "Tucson", "Elantra", "Fiesta")
# carro1, *carros, carro2 = tuplaCarros
# print(carro1)
# print(*carros)
# print(carro2)

# # Converter Lista em Tupla:
# lista = ["Uno", "Ranger", "Golf", "Tucson", "Elantra", "Fiesta"]

# tupla = tuple(lista)

# print(type(tupla))
# print(tupla)
# # tupla.append("KA") -> Dá erro, tupla não recebe dados

# Converter tupla em lista

tupla = "Uno", "Ranger", "Golf", "Tucson", "Elantra", "Fiesta"

lista = list(tupla)

print(type(lista))
print(lista)
lista.append("Fusca")
print(lista)