# # # Listas -> São coleções de objetos de qualquer tipos

# # # Criação fe uma lista vazia
# # bancos = []

# # # Uma lista com três elementos strings

# # bancos = ["Banco do Brasil", "Caixa", "Santander"]

# # # Cada item de uma lista possui um índice iniciando do zero

# # bancos = ["Banco do Brasil", "Caixa", "Santander"]
# # # Posição         0             1          2

# # print(bancos)

# # # Resultado: ['Banco do Brasil', 'Caixa', 'Santander']

# # # Uma lista pode conter varios tipos de dados
# # lista = ["Bravo", 25, 1.85, True]

# # print(lista)

# cidades = ["São Paulo", "Itu", "Santo André", "Osasco"]

# print(cidades)
# print(cidades[2]) # Retorna o valor da posição 2
# print(len(cidades)) # Retorna o tamanho da lista
# print(cidades[-1]) # -1 Retorna o ultimo valor

# cidades[1] = "Carapicuiba" # Atualizar o valor da lista
# print(cidades)

# # Incrementando novos valores

# cidades = cidades + ["São Roque", "Ibiuna", "Juquitiba"] # ou cidades += ["São Roque", "Ibiuna", "Juquitiba"]
# print(cidades)

# # Função .append() - Sempre adiciona valores no final da lista

# cidades.append("Barueri")
# print(cidades)

# # Função .insert() - Adiciona na posição informada na lista

# cidades.insert(0, "Itapevi")
# print(cidades)
# cidades.insert(3, "Ferraz de Vasconselos")
# print(cidades)

# # Função .remove() - Para remover elementos

# cidades.remove("Ibiuna")
# print(cidades)

# # Função .pop() - Remove o ultimo elemento

# cidades.pop()
# print(cidades)
# cidades.pop(2)
# print(cidades)
# print(len(cidades)) # Exibe o tamanho da lista

# # Função .sort() - Ordena os elementos (Alfaetica ou numerica)

# cidades.sort()
# print(cidades)

# # Função .reverse() - Ordena os elementos (Alfaetica ou numerica) em ordem decrescente

# cidades.reverse()
# print(cidades)

# # Função .count - Conta quantas vezes aparece um item na lista

# cidades.append("São Paulo")
# cidades.append("São Paulo")

# print(cidades.count("São Paulo"))

# # # Verificar se o elemento existe na lista

# # localizar = input("Digite a cidade: ")

# # if localizar in cidades:
# #     print(f"Tem {localizar}")
# # else:
# #     print(f"Não tem {localizar}")

# # # Função del - Deleta um elemento da lista

# # del cidades[2]
# # print(cidades)

# # # Funçaõ .clear - Limpa a lista toda

# # cidades.clear()

# # print(cidades)

# # Iterando a lista (Percorrendo uma lista)

# for cidades in cidades:
#     print(cidades)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum(numeros))

# # Colocar em Maiusculo
# # for i in range(len(cidades)):
# #     cidades[i] = cidades[i].upper()
# # print(cidades)

# # Lista dentro de lista (Matriz):

# notas = [[8, 7, 9], [10, 5, 3], [2, 4, 8]]

# print(notas)
# print(notas[1][2])

# # Alinhar bairros com a região:

# bairros = [
#            ["Brasilandia", "Pirituba", "Jaragua"],
#            ["Tiradentes", "Guaianazes", "São Matheus"],
#            ["Grahau", "Jd. Miriam", "Capão Redondo"],
#            ["Lapa", "Vl. Leopoldina", "Villa Lobos"]
#            ]

# regioes = ["Zona Norte", "Zona Leste", "Zona Sul", "Zona Oeste"]

# for i in range(len(bairros)):
#     print((f"{regioes[i]}: {bairros[i]}"))

# compra = [10.2, 3.25, 16.3, ["Tomate", "Sabonete", "Arroz"]]
# produtos = compra[3]
# total = compra[0] + compra[1] + compra[2]
# print(total)
# print(produtos)

# letra = ["a", "b", "c"]
# numeros = [1, 2, 3]
# concat = [letra + numeros]
# print(concat)
# tudo = [letra, numeros]
# print(tudo)

# print(f"Letras: {tudo[0]}")
# print(f"Numeros: {tudo[1]}")


# Descobrir posião do elemento:

frutas = ["berinjela", "pimentão", "pepino", "chuchu", "tomate"]

procurar = input("Digite a fruta: ").strip().capitalize()

if procurar in frutas:
    print("Esta na posição:", frutas.index(procurar))
else:
    print("Esta fruta não está na lista!")

# Função .capitalize() -> Altera as iniciais em maiusculo Ex. Tomate
# Funçao .lower() -> Altera as letras para minusculas Ex. tomate
# Função .upper() -> Altera as letras para maiusculas Ex. TOMATE
# Função .strip() -> Remove os espaços do inicio e fim