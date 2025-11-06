import os

os.system('cls')

# try Except:

#  Estrutura do bloco de codigo:
# try:
#   bloco_codigo (o que eu quero tentar fazer)
# except tipo_erro:
#   bloco_codigo (o que fazer caso de erro)


# # Sem tratamento de erro

# valor = input("Digite o valor: ")

# soma = int(valor) + 10
# res = soma / int(valor)

# print(res)

# # try Except:

# valor = input("Digite o valor: ")

# try:
#     soma = int(valor) + 10
#     res = soma / int(valor)
#     print(res)
# except:
#     print("Ocorreu um erro")

# valor = input("Informe um valor: ")

# try:
#     soma = int(valor) + 10
#     res = soma / int(valor)
#     print(res)
# except ZeroDivisionError:
#     print("Ocorreu uma divisão por zero!")
# except ValueError:
#     print("Ocorreu um erro")

# # Try else -> executa quando não ocorre erro

# valor = input("Informe um valor: ")

# try:
#     soma = int(valor) + 10
#     res = soma / int(valor)
#     print(res)
# except ZeroDivisionError:
#     print("Ocorreu uma divisão por zero!")
# except ValueError:
#     print("Ocorreu um erro")
# else:
#     print("Não deu erro")

# # Try finally -> opcional - sempre será executado de erros ou não

# valor = input("Informe um valor: ")

# try:
#     soma = int(valor) + 10
#     res = soma / int(valor)
#     print(res)
# except ZeroDivisionError:
#     print("Ocorreu uma divisão por zero!")
# except ValueError:
#     print("Ocorreu um erro")
# else: # Opicional
#     print("Não deu erro")
# finally: # Opicional
#     print("Fim do programa")

# # Companando if/else e try/except:

# num = int(input("Digite o denominador: "))
# if num != 0:
#     res = 10/num
#     print("Resultado:", res)
# else:
#     print("Não é possivel divisão por zero!")

# # Se não digitar numero o programa da erro e vai finalizar

# try:
#     num = int(input("Digite o denominador: "))
#     res = 10 // num
#     print("Resultado", res)
# except ZeroDivisionError:
#     print("Não exixtem divisão por zero!")
# except ValueError:
#     print("Digite apenas numeros!")

# # Com loop:

# while True:
#     try:
#         num = int(input("Digite um numero inteiro: "))
#         break
#     except ValueError:
#         print("Digite apenas numeros!")
# print(f"Agora você digitou certo: {num}")

# # Usando dicionário:

# dados = {
#     "nome": "Bravo",
#     "idade": 39,
#     "altura": 1.74
#     }

# try:
#     valor = input("Insira um valor: ").lower()
#     print(dados[valor])
# except KeyError:
#     print(f"Chave {valor} não foi encontrado")
    
# # Abrir arquivo:

# try:
#     arquivo = open("comando.txt")
#     conteudo = arquivo.read()
#     print(conteudo)
# except FileNotFoundError:
#     print("Arquivo não encontrado")

# os.system('teste.xlsx')

print(os.name)




