notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota{x}: "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"nota {x}: {notas[x]}:")
    x += 1
print(f"Média: {soma / x}")