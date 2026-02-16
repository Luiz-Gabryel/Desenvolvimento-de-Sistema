#ele pega texto e transforma em binario
#luiz gabryel 2026 fev

texto = input("digite qualquer coisa: ")

binario = ''
for letra in texto: # pega letra por letra
    numero = ord(letra) # transforma em numero
    bin_letra = format(numero, '08b')  # faz o número em 8 zeros e uns
    binario += bin_letra + ' ' # junta em linha e espaço 

print(f"Ficou assim: {binario}")