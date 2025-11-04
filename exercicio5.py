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
        print("Programa Finalizado")
        break
    if consulta in produtos:
        print(f"Produto {consulta} custa {produtos[consulta]}")
    elif consulta != produtos:
        print(f"Produto {consulta} não encontrado")
        descisao = input(f"Deseja cadastrar o produto {consulta}? S para SIM ou N para Não: ").upper()
        if descisao == "S":
            valor = float(input(f"Digite o valor do produto {consulta}: "))
            produtos[consulta] = valor
            print(f"O produto {consulta} foi cadastrado com o valor {valor} com sucesso.")
        else:
            print("Produto não foi cadastrado.")

print()
print("Segue a lista atualizada")
print()

for chave, valor in produtos.items():
    print(f"{chave}: {valor}")

print()