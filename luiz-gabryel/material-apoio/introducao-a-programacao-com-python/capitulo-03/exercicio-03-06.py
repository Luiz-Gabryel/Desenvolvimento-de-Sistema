#ele pergunta as notas, se todas for maior que 7, voce passou, se nao, triste pra voce
m1 = float(input('sua nota da matéria 1: '))
m2 = float(input('sua nota da matéria 2: '))
m3 = float(input('sua nota da matéria 3: '))

if m1 > 7 and m2 > 7 and m3 > 7:
    print("boa, voce passou")
else:
    print("puts, voce nao passou")