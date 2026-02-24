# Mini Calculadora
print("Vamos Calcular")

# pede os numeros
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# pergunta operacao
operacao = input("Qual operação? (+, -, *, /): ")

# numeros 
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 == 0:
        resultado = "nao pode"
    else:
        resultado = numero1 / numero2
else:
    resultado = "O"

# mostra resultado
print("O resultado é:", resultado)
