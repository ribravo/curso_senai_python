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



        


