preco = float(input('Qual valor da sua compra: '))
porcentagem = input('Possue algum desconto: ').lower()

if porcentagem == 's':
    porcentagem = float(input('Qual porcentagem do desconto: '))
    v_desconto = preco * (porcentagem / 100)
    preco_fim = preco - v_desconto
    print(f'Voce ira pagar {preco_fim}')

else:
    print(f'Voce ira pagar {preco}')