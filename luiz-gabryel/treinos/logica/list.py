# z = [15 , 8, 9]
# print(z)
# z[0] = 1
# print(z)

notas = [6, 7, 5, 8, 9] #35

soma = 0

x = 0

while x < 5:
    soma += notas[x]  # notas[0] = 6
    x += 1
print(f"Media: {soma / x}")




# x = 0 → pega notas[0] = 6 → soma = 0 + 6 = 6  → x vira 1
# x = 1 → pega notas[1] = 7 → soma = 6 + 7 = 13 → x vira 2
# x = 2 → pega notas[2] = 5 → soma = 13 + 5 = 18 → x vira 3
# x = 3 → pega notas[3] = 8 → soma = 18 + 8 = 26 → x vira 4
# x = 4 → pega notas[4] = 9 → soma = 26 + 9 = 35 → x vira 5
# x = 5 → para! (5 não é menor que 5)