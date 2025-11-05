from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Exemplo de uso:
dia = int(input("Dia de nascimento: "))
mes = int(input("Mês de nascimento: "))
ano = int(input("Ano de nascimento: "))

data_nascimento = date(ano, mes, dia)
idade = calcular_idade(data_nascimento)

print(f"Você tem {idade} anos.")