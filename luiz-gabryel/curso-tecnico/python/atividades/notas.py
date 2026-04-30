qtd_aluno = int(input("Quantidade de alunos: "))
soma_notas = 0
cont = 0

while cont < qtd_aluno:
    entrada = input(f"Digite a nota do aluno {cont + 1}: ")
    
    if entrada == "-1":
        print("Tchau")
        break
    
    soma_notas += float(entrada)
    cont += 1

if cont > 0:
    media = soma_notas / cont
    print(f"Média da turma: {media:.2f}")
