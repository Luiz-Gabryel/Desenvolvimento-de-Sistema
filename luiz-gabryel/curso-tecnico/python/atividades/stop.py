import random 


opcoes_a = ["Ana", "Arthur", "Alice"]
opcoes_b = ["Bruno", "Beatriz", "Bia"]

letra = input("Digite uma letra: ").lower()

if letra == 'a':
    sorteado = random.choice(opcoes_a)
    print(f"Nome sorteado com A: {sorteado}")

elif letra == 'b':
    sorteado = random.choice(opcoes_b)
    print(f"Nome sorteado com B: {sorteado}")

else:
    print("Letra não cadastrada para sorteio.")
