pontucao = [80, 100, 60, 120]
menor = pontucao[0]
maior = pontucao[0]
soma = 0

for ponto in pontucao:
    if ponto < menor:
        menor = ponto
    
    if ponto > maior:
        maior = ponto
    
    soma += ponto

media = soma / len(pontucao)

print(f"Pontuação do jogador Menor: {menor} - Maior {maior} - Soma {soma} - Média {media}")
