import random

dados = {
    "A": ["Abacaxi", "Alice", "Aranha"],
    "B": ["Banana", "Bruno", "Baleia"],
    "C": ["Caju", "Caio", "Cachorro"],
    "D": ["Damasco", "Daniel", "Dinossauro"],
    "E": ["Ervilha", "Eduarda", "Elefante"],
    "F": ["Figo", "Felipe", "Formiga"],
    "G": ["Goiaba", "Gabriel", "Gato"],
    "H": ["Heiki", "Hugo", "Hipopótamo"],
    "I": ["Ingá", "Isabela", "Iguana"],
    "J": ["Jaca", "João", "Jacaré"],
    "K": ["Kiwano", "Kevin", "Krill"],
    "L": ["Laranja", "Luana", "Leão"],
    "M": ["Manga", "Mariana", "Macaco"],
    "N": ["Nectarina", "Natan", "Naja"],
    "O": ["Oiti", "Otávio", "Onça"],
    "P": ["Pêra", "Paula", "Panda"],
    "Q": ["Quinoa", "Quiteria", "Quati"],
    "R": ["Romã", "Ricardo", "Rato"],
    "S": ["Siriguela", "Sofia", "Sapo"],
    "T": ["Tangerina", "Tiago", "Tigre"],
    "U": ["Uva", "Uriel", "Urubu"],
    "V": ["Vagem", "Vitor", "Vaca"],
    "W": ["Wampi", "Wagner", "Wombat"],
    "X": ["Xixá", "Xênia", "Xexéu"],
    "Y": ["Yacon", "Yuri", "Yorkshire"],
    "Z": ["Zimbro", "Zeca", "Zebra"]
}

letra = input("Digite uma letra: ").upper()

if letra in dados:
    sorteado = random.choice(dados[letra])
    print(f"O sorteio para a letra {letra} deu: {sorteado}")
else:
    print("A letra {letra} não e valida")