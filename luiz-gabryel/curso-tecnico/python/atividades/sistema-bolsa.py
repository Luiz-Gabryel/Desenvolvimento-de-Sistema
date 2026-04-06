renda = float(input("Renda familiar: R$ "))
media = float(input("Média acadêmica: "))
medalha = input("Tem medalha olímpica? (S/N): ").upper() == 'S'
atleta = input("É atleta universitário? (S/N): ").upper() == 'S'


if (renda <= 1500 and media >= 8.5) or medalha:
    percentual = 100
elif (renda <= 3000 and media >= 7.0) or (atleta and media >= 6.0):
    percentual = 50
else:
    percentual = 0

print(f"Percentual de bolsa: {percentual}%")
