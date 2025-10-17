# # Variaves de imprssão (Interpolação)

# nome = "Ricardo"
# idade = 39
# peso = 96.1525

# print("Nome:", nome, "Idade:", idade, "Peso:", round(peso,2)) # Padrão
# print(f"Nome: {nome} Idade: {idade} Peso: {peso:.2f}") # f-string (moderno)
# print("Nome: %s Idade: %i Peso: %.2f" %(nome, idade, peso)) # Formatação por % (antigo)
# print("Nome: {} Idade: {} Peso: {:.2f}" .format(nome, idade, peso)) # Formatação por .format() (Intermediario)

# # Variações .format():

# print("Nome: {} Idade: {} Peso: {:.2f}" .format("Bravo", 38, 74.1252))
# print("Nome: {0} Idade: {1} Peso: {2:.2f}" .format("Bravo", 38, 74.1252)) # Por posição
# print("Nome: {nome} Idade: {idade} Peso: {peso:.2f}" .format(nome="Bravo", idade=38, peso=74.1252)) # Por nome

# idade = 25
# print(f"Idade atual: {idade}. Daqui 5 anos terá: {idade + 5}")

# # Alinhamento

# print("{:>20}".format("python")) # Alinhamento a direita
# print("{:<20}".format("python")) # Alinhamento a esquerda
# print("{:^20}".format("python")) # Centralizado

# # Formatação numérica

# print("{:.2f}".format(3.14656874)) # Arredondamento
# print("{:08d}".format(42)) # Preenchido com zeros
# print("{:,}".format(1102080)) # Separador de decimais
# print("{:,.2f}".format(1102080)) # Separador de decimais e Arredondamento

# Operadores de Atribuições

x = 1
# x = x + 1 # Literal
x += 1 # Forma correta
print(x)

y = 1
# y = y - 0
y -= 1
print(y)

z = 1
# z = z * 1
z *= 1
print(z)

w = 1
# w = w / 1
w /= 1
print(w)

v = 1
# v = v % 1
v %= 1
print(v)

u = 1
# u = u ** 1
u **= 1
print(u)

x = 8
x += 4
print (x)

# Raiz quadrada:

x = 25
res = x ** 0.5
print(res)

x = 25
res = x ** (1/2)
print(res)

# Raiz Cubica

y = 8
cub = y ** (1/3)
print(cub)