nota = [0, 0, 0, 0]
soma = 0
x = 0 

while x < 4:
    escolha = float(input(f"Qual sua nota{x + 1}: "))
    nota[x] = escolha
    x += 1
    soma += escolha
print(f"Sua media ficou em {soma / 4}")
print(nota)