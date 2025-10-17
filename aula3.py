# # Precedencias e/ou Prioridades

# print(2 + 5 * 3)        # Multiplicação > soma
# print((2 + 5) * 3)      # Parenteses > multiplicação
# print(1 + 5 ** 2)       # Exponenciação > soma
# print((1 + 5) ** 2)     # Parenteses > exponenciação
# print(8 + 5 - 10)       # Sem precedencia
# print(8 + (5 - 10))     # Multiplicação > soma

# print(2 + 3 ** 2 * 2)   # Exponenciação > multiplicação > soma
# print(2 ** 3 ** 4)      # Exponenciação -> Realiza o calculo da direira para esqueda ( 3^4 = 81 ---> 2^81)

# print(6 + 4 * 2)        # Multiplicação > soma
# print(4 * 9 + 5)        # Multiplicação > soma
# print((6 + 7) * 9)      # Parenteses > multiplicação
# print(15 + 20 - 30)     # Sem precedencia
# print(6 + 5 ** 2)       # Exponenciação > soma
# print(-5 -5)            # Sem precedencia

# print(-.01 + 0.10)      # .01 == 0.01

# print(abs(-5) -5)       # Absoluto remove o sinal

# # Operadores de Comparação

# print(6 > 3)    # Maior que ...
# print(4 < 8)    # Menor que ...
# print(8 <= 8)   # Manor ou igual que ...
# print(18 >= 9)  # Maior ou igual que ...
# # "=" -> Atribuição
# # "==" -> Comparação
# print(8 == 8)   # Igual que ...
# print(3 != 9)   # Diferente que ...

# Entrada de Dados

# Um "Imput" recebe string por padrão

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# idade = int(input("Digite sua idade: "))
# peso = float(input("Digite seu peso: "))
# altura = float(input("Digite sua altura: "))
# imc = round(peso / (altura * altura), 2)

# print(f"Olá, {nome} {sobrenome}!!")
# print(f"Você tem {idade} anos.")
# print(f"Seu IMC é de {imc}")

# # Exercicio

# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite outro numero: "))

# soma = n1 + n2
# multiplicacao = n1 * n2
# divisao = n1 / n2

# print(f"O resultado da soma é {soma}")
# print(f"O resultado da multiplicação é {multiplicacao}")
# print(f"O resultado da divisão é {divisao}")

# f-string:

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

print(f"Olá, {nome} {sobrenome}, sua idade é {idade} anos. Você pesa {peso}Kg e tem {altura}m de altura. Seu IMC é {imc} ")
print(f"Olá, {nome} {sobrenome}, sua idade é {idade} anos. Você pesa {peso}Kg e tem {altura}m de altura. Seu IMC é {imc:.2f} ")

# if imc < 17:
#     print("Muito abaixo do peso")
# elif imc <= 18.49:
#     print("Abaixo do peso")
# elif imc <= 24.99:
#     print("Peso normal")
# elif imc <= 29.99:
#     print("Acima do peso")
# elif imc <= 34.99:
#     print("Obesidade I")
# elif imc <= 39.99:
#     print("Obesidade II (severa)")   
# else:
#     print("Obesidade III (mórbida)")