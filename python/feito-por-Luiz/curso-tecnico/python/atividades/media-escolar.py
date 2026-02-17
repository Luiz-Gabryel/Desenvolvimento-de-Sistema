n1 = float (input ('Qual sua primeira nota: '))
n2 = float (input ('Qual sua segunda nota: '))
n3 = float (input ('Qual sua terceira nota: '))
n4 = float (input ('Qual sua quarta nota: '))
m = (n1 + n2 + n3 + n4) / 4

if m <= 7:
    print("Sua nota e B")

print(f"sua nota final e {m}")