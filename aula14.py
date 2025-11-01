import os

os.system("cls")

# # Copia de dicionarios

# # Criar uma cópia independente:

# dic1 = {
#     "nome": "Ricardo",
#     "idade": 39
#         }

# dic2 = dic1.copy()
# dic2["idade"] = 40
# print(dic1)
# print(dic2)

# # Criar uma referencia ao mesmo dicionário:

# dic1 = {
#     "nome": "Ricardo",
#     "idade": 39
#         }

# dic2 = dic1
# dic2["idade"] = 40
# print(dic1)
# print(dic2)

# # Adicionando dicionário dentro de dicionário

# dados1 = {
#     "nome": "Ricardo",
#     "idade": 39
# }

# dados2 = {
#     "Cidade": "São Paulo",
#     "Profissão": "Engenheiro"
# }

# # print(dados1 + dados2) # Errado

# dados1.update(dados2)

# print(dados1)

# # Tamanho do dicionario:

# print(len(dados1))

# # Dicionario alinhado:

# pessoa = {
#     "nome": "Ricardo",
#     "idade": 39,
#     "endereço": {
#         "logradouro": "Av. Brasil",
#         "numero": 188,
#         "cidade": "São Paulo"
#     }
# }

# print(pessoa)
# print(pessoa["nome"])
# print(pessoa["endereço"]["cidade"])

# # Dicionario de dicionario

# pessoas = {
#     "pessoa1": {
#         "nome": "Ricardo",
#         "idade": 39,
#         "altura": 1.74
#     },
#     "pessoa2": {
#         "nome": "Manoela",
#         "idade": 42,
#         "altura": 1.65
#     },
#     "pessoa3": {
#         "nome": "Lucca",
#         "idade": 1,
#         "altura": 0.83
#     },
#     "pessoa4": {
#         "nome": "Guilherme",
#         "idade": 18,
#         "altura": 1.72
#     }
# }

# print(pessoas["pessoa3"]["idade"])

# # Inserindo diversos valores no dicionario

# aluno = {
#     "nome": "joão",
#     "notas": {
#         "Matemática": 5,
#         "Português": 10,
#         "Geografia": 7.5
#     },
#     "materias": ["Matemática", "Português", "Geografia"]
# }

# print(aluno["nome"])
# print(aluno["notas"]["Português"])
# print(aluno["materias"][2])

# # inserindo uma chave dentro de um dicinario dentro do dicionario

# aluno["notas"]["inglês"] = 8.8

# # inserindo um valor dentro de uma lista dentro do dicionário

# aluno["materias"].append("inglês")

# print(aluno)


aluno = {}

aluno["nome"] = input("Digite um nome: ")
aluno["media"] = float(input("Digite a média: "))

if aluno['media'] >= 7:
    aluno["status"] = "aprovado"
elif aluno['media'] >= 5:
    aluno["status"] = "recuperação"
else:
    aluno["status"] = "reprovado"

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print(aluno)

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
