# Sistema onde calcula 2 notas e da a media, usando if

#variavel para armazenamento das notas e media
nota1 = 0.0
nota2 = 0.0
media = 0.0

#solicitacao das notas
nota1 = float(input("Digite a sua 1º Nota: "))
nota2 = float(input("Digite a sua 2º Nota: "))

#calula a media, usando media aritimetrica
media = (nota1 + nota2) / 2

#exibir sua media
print(f"Sua Media foi: {media}")

if media >= 6:
    print("Voce foi aprovado com louvor")

else:
    print("Nossa, Voce Repitiu")

