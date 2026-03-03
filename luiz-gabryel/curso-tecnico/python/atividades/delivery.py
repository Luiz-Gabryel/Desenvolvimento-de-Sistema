#Entrada
preco_pizza = float(input("Valor da pizza: R$ "))
distancia = float(input("Distância (km): "))
valor_pago = float(input("Cliente vai pagar: R$ "))

#Configuração
tx_km = 1.50 
tempo_base = 20
min_km = 3

#Procesamento 
taxa_entrega = distancia * tx_km
total = preco_pizza + taxa_entrega
tempo_entrega = tempo_base + (distancia * min_km)
troco = valor_pago - total

#Saida
print("--- Nota ---")
print(f"Total: R$ {total} (Entrega: R$ {taxa_entrega})")
print(f"tempo estimado: {tempo_entrega} min")
print(f"Troco: R${troco}")