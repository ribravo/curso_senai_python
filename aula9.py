

num_aluno_alto = 0
num_aluno_baixo = 0


for i in range(5):
    num_aluno = int(input(f"Informe o numero do {i + 1}º aluno: "))
    alt_aluno = int(input(f"Informe a altura do {i + 1}º aluno: "))
    alto = alt_aluno
    baixo = alt_aluno
    if alt_aluno > alto:
        alto = alt_aluno
        num_aluno_alto = num_aluno

        
print()
print(f"O aluno mais alto é {num_aluno_alto} e sua altura é {alto} cm")
print(f"O aluno mais baixo é {num_aluno_baixo} e sua altura é {baixo} cm")
