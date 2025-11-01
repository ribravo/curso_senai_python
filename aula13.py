import os

os.system("cls")

# # Dicionarios -> é uma lista de associações composta por uma chave (de tipo mutável). É uma estrutura de dados que armazena chave-valor:

# # Sintaxe -> "Propriedade": Valor
# pessoa = {
#     "nome": "Ricardo",
#     "idade": 39,
#     "altura": 1.74
# }

# print(pessoa)
# print(type(pessoa))

# print(pessoa["nome"])
# print(pessoa["idade"])
# # print(pessoa["peso"]) # dá erro porque não existe a chave peso
# print(pessoa.get("peso")) # get() para não gerar erro caso não possua a chave
# print(pessoa.get("idade")) # get() para não gerar erro caso não possua a chave

# # Adicionando novas chaves:
# pessoa["peso"] = 96.5
# print(pessoa)

# # Alterar valores:

# pessoa["altura"] = 1.80
# print(pessoa)

# # Removendo itens:
# pessoa.pop("nome")
# print(pessoa)

# # Alternativa

# del pessoa["altura"]
# print(pessoa)

# pessoa["nome"] = "Manoela"
# print(pessoa)

# # Criando chave vazia e adicionando valores:

# aluno = {}

# aluno["nome"] = "Maria"
# aluno["media"] = 9.5
# aluno["turma"] = "3A"

# print(aluno)

# #   Iterando...

# pessoa = {
#     "nome": "Ricardo",
#     "idade": 39,
#     "altura": 1.74
# }

# print()

# # items() -> Retorna pares (chave, valor)
# for chave, valor in pessoa.items():
#     print(chave, valor)

# print()

# # keys() -> Retorna somente chaves
# for chave in pessoa.keys():
#     print(chave)

# print()

# # keys() -> Retorna somente valores
# for valor in pessoa.values():
#     print(valor)

# # Dicionario dentro de lista
# alunos = [
#     {"nome": "João", "nota": 8},
#     {"nome": "Maria", "nota": 6},
#     {"nome": "Lucas", "nota": 3}
# ]

# print(alunos)
# print(alunos[1])

# for i in alunos:
#     print(f"{i["nome"]} tirou nota {i["nota"]}")

# print()

# # Verificando se existe uma chave:

# pessoa = {
#     "nome": "Ricardo",
#     "idade": 39,
#     "altura": 1.74
# }

# if "idade" in pessoa:
#     print("Existe")
# else:
#     print("Não existe")

# # Limpar um dicionário:

# pessoa.clear()
# print(pessoa)

produtos = {
    "mouse": 50.90,
    "teclado": 125.98,
    "monitor": 899.90,
    "gabinete": 255.00,
    "headset": 789.36,
    "gpu": 5376.00,
    "cpu": 189.90
}

while True:
    consulta = input("Digite o produto (0 para sair): ").lower()
    if consulta == "0":
        break
    if consulta in produtos:
        print(f"Produto {consulta} custa {produtos[consulta]:.2f}")
    else:
        print(f"Produto {consulta} não encontrado")