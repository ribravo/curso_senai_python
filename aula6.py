# Operadores Lógicos

# and -> Conjunção(E) -> &&
# or -> Disjunção(OU) -> ||
# not -> Negação(NÃO) -> !

# print((5 > 2) and (10 > 3))
# print((5 < 2) and (10 > 3)) # "AND" retorna True se todas as condições fores True

# print((5 < 2) or (10 > 3))
# print((5 < 2) or (3 > 10)) # "OR" retorna True se uma das condições forem True

# print(not (5 == 5))
# print(not (5 > 5)) # "NOT" Retorna o resultado inverso

# Tabela Verdade and

# |  A  |  B  | AeB |
# |  F  |  F  |  F  |
# |  F  |  V  |  F  |
# |  V  |  F  |  F  |
# |  V  |  V  |  V  |

# Tabela Verdade or

# |  A  |  B  | AeB |
# |  F  |  F  |  F  |
# |  F  |  V  |  V  |
# |  V  |  F  |  V  |
# |  V  |  V  |  V  |

# Tabela Verdade not

# |  A  | Não A |
# |  F  |   V   |
# |  V  |   F   |

# idade = int(input("Idade: "))
# documento = (input("Possui documento? ")).upper()

# if idade >= 18 and (documento == "SIM" or documento == "S"):
#     print("Entrada liberada")
# elif idade >= 18 and (documento == "NÃO" or documento == "N"):
#     print("Maior de 18 ano, porèm sem documento. Entrada negada!!")    
# else:
#     print("Entrada Negada")

feriado = False
fds = False

if feriado or fds:
    print("Pode descansar!")
else:
    print("Dia de trabalho!")

idadeLucas = 15
idadeAna = 17

if (idadeLucas >= 18 or idadeAna >= 18):
    print("Pelo menos um dos dois são maior de idade!")
else:
    print("Ninguem é maior de idade")

idadeLucas = 15
idadeAna = 17

if not (idadeLucas >= 18 or idadeAna >= 18):
    print("Pelo menos uma pessoa não é maior de idade!")



