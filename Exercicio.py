A = 10
B = 5

print("A = ",A)
print("B = ",B)

aux = A
A = B
B = aux

print("A = ",A)
print("B = ",B)

A, B = B, A

print("A = ",A)
print("B = ",B)