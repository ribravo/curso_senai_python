#4

idade = int(input("Digite a idade: "))

if idade < 16:
    print("Não está apto a votar!")
elif (idade >= 16 and idade < 18) or idade >= 70:
    print("Voto facultativo")
else:
    print("Voto obrigatório")

#5

idade = int(input("Digite a idade do nadador: "))

if idade < 5:
    print("Não tem categoria para essa idade")
elif idade >= 5 and idade < 8:
    print("Categoria: Infantil A")
elif idade >= 8 and idade < 12:
    print("Categoria: Infantil B")
elif idade >= 12 and idade < 14:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade < 18:
    print("Categoria: Juvenil B")
else:
    print("Categoria: Adulto")

#6

n1 = float(input("Digite um numero: "))
oper = (input("Informe a opetação matematica: (*) Soma | (-) Subtração | (*) Multiplicação | (/) Divisão: " ))
n2 = float(input("Digite um numero: "))


if oper == "+" or oper == "-" or oper == "*" or oper == "/":
    if oper == "+":
        print(n1 + n2)
    elif oper == "-":
        print(n1 - n2)
    elif oper == "*":
        print(n1 * n2)
    elif oper == "/" and n2 == 0:
        print("ERRO : Não existe divisão por 0")
    elif oper == "/":
        print(n1 / n2)
else:
    print("Operador invalido")