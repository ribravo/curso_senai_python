# # Loop/Laço de repetição

# # Enquanto uma condição for verdadeira, vai ficar repetindo

# # Sintaxe -> for "referncia" in "sequencia":

# # for v in ranger(argumento(s)):
# #   bloco de código

# # for e while

# # Exemplo de códigos

# # for n1 in [8, 7, 17, 25, 38]:
# #     print(n1)

# # seq = [3, 57, 67, 22, 8]

# # for n2 in seq:
# #     print(n2)

# # Os valores começam a partir do 0 (zero)

# for i in range(10): # range é o gerador de numeros
#     print(i)
# print("Fim do programa!")

# # Range(fim) -> range(5) Gera de 0 a 4
# # range(inicio, fim) -> range(1, 6) Gera de 1 a 5
# # range(incio, fim, intervalo) -> range(0, 10, 2)

# for i in range(1, 6): # "i" siginifica dentro do range
#     print(i)
#     print("SENAI")

# for i in range(0, 10, 2):
#     print(i)

# for i in range(0, 30, 3):
#     print(i)

# # Iterando string

# escola = "SENAI"

# for i in escola:
#     print(i)

# # Alternativa

# for i in "SENAI":
#     print(i)

# for i in "SENAI":
#     print(i, end="")

# # for pode percorer uma lista

# for i in [1, 2, 3, 4, 5]:
#     print(i)

# for i in range(10):
#     print(f"{i} elefante incomoda muita gente!")

# # Contagem progressiva
# for i in range(0, 11):
#     print(i)

# # Contagem regressiva
# for i in range (10, -1, -1):
#     print(i)
# print("Feliz Ano Novo!")

# # Realizar soma dos valores

# soma = 0

# for i in range(5):
#     n = int(input(f"Digite o {i+1}º numero: "))
#     soma += n
# print(f"A soma é: {soma}")

# for numero in range(101):
#     if numero % 2 == 0:
#         print(f"{numero} Par")
#     else:
#         print(f"{numero} Impar")

inicio = int(input("Digite o primeiro valor: "))
fim = int(input("Digite o ultimo valor: "))
int = int(input("Digite o intervalo: "))

for i in range(inicio, fim, int):
    print(i)
