cliente = input("Qual tipo de cliente voce e? (VIP / COMUN)").upper() 
valor = float(input("Qual valor da compra? "))
percentual = 0.15

if cliente == "VIP" and valor > 100:
    valor_final = valor - (valor * percentual)
    print(f"Desconto Valido! Sua compra ficara por R$ {valor_final:.2f}")
else:
    print(f"Sem descontos. Sua compra ficou por R$ {valor:.2f}")