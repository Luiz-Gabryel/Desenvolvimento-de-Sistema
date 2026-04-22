dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

preco_total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R$ {preco_total}')

#carro custa R$ 60 por dia e R$ 0,15 por km rodado
