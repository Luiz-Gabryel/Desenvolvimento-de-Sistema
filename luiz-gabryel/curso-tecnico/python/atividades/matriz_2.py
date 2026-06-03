matriz = [ [2, 5, 1, 4],
         [7, 0, 3, 8],
         [6, 9, 2, 5] ]
qtd_linhas = len(matriz)

for linha in range(0, qtd_linhas):
    soma_linha = 0  
    
    for coluna in range(len(matriz[linha])):
        soma_linha += matriz[linha][coluna]  
        
    print(f"Soma da linha {linha+1} = {soma_linha}")
