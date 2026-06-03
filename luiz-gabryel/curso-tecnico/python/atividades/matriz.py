matriz = [
    [5, 8, 2],
    [1, 9, 4],
    [7, 3, 6],
    [10, 11, 0]
]

#variaveis
soma_total = 0
minimo = matriz[0][0]
maximo = matriz[0][0]
pos_min = (1, 1)
pos_max = (1, 1)


soma_colunas = [0, 0, 0]

for linha in range(len(matriz)):
    soma_linha = 0
    
    for coluna in range(len(matriz[linha])):
        valor = matriz[linha][coluna]
        
        soma_linha += valor
        
        soma_colunas[coluna] += valor
        
        soma_total += valor
        
        if valor < minimo:
            minimo = valor
            pos_min = (linha + 1, coluna + 1)
        if valor > maximo:
            maximo = valor
            pos_max = (linha + 1, coluna + 1)
            
    media_linha = soma_linha / len(matriz[linha])
    
    print(f"Linha {linha+1} -> Soma: {soma_linha} | Média: {media_linha:.2f}")

print("-" * 40)


for c in range(len(soma_colunas)):
    print(f"Soma da Coluna {c+1} = {soma_colunas[c]}")

print("-" * 40)

print(f"3. Soma Total da Matriz: {soma_total}")
print(f"5. Mínimo: {minimo} na Posição (Linha {pos_min[0]}, Coluna {pos_min[1]})")
print(f"5. Máximo: {maximo} na Posição (Linha {pos_max[0]}, Coluna {pos_max[1]})")
