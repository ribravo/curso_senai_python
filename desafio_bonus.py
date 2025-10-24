# Exercicio 1

print("Desafio da Tabuada")
print()
num = int(input("Digite um numero para treinar a tabuada: "))
print()
print(f"Tabuada do {num}")
print()
erro = 0
acerto = 0

for i in range(1, 11):
    tab = num * i
    res = int(input(f"{i} x {num} = "))
    if res == tab:
            print("CORRETO")
            acerto += 1
    else:
            print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {tab}")
            erro += 1

print(f"Total de acertos: {acerto}")
print(f"Total de erros: {erro}")

# Exercicio 2

alturaMax = 0
alturaMin = 1000
alunoMax = 0
alunoMin = 0

for i in range(10):
    nome = int(input(f"Informe o numero do {i + 1}º aluno: "))
    altura = int(input(f"Informe a altura do {i + 1}º aluno: "))

    if altura > alturaMax:
        alturaMax = altura
        alunoMax = nome
    if altura < alturaMin:
        alturaMin = altura
        alunoMin = nome


print()
print(f"O aluno mais alto é {alunoMax} e sua altura é {alturaMax} cm")
print(f"O aluno mais baixo é {alunoMin} e sua altura é {alturaMin} cm")

 
