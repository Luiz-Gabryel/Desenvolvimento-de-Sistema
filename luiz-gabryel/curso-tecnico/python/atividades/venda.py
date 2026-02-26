#sistema para calcular o valor final de uma venda
valor_total = float(input("Qual o valor total dos produtos: R$ "))

desconto_aplicado = 0
valor_frete = 0
#desconto
if valor_total > 500:
    desconto_aplicado = valor_total * 0.10
elif valor_total > 100:
    desconto_aplicado = valor_total * 0.05

#frete
if valor_total < 200:
    valor_frete = 15

#calculo do valor final
valor_final = valor_total - desconto_aplicado + valor_frete

#resultados
print("-" * 30)
print(f"Subtotal: R$ {valor_total}")
print(f"Desconto aplicado: R$ {desconto_aplicado}")
print(f"Valor do frete: R$ {valor_frete}")
print(f"TOTAL FINAL: R$ {valor_final}")
print("-" * 30)