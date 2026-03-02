#calculadora

print("---Vamos Calcular---")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

op = input("Qual operação? (+, -, *, /): ")

if op == "+":
    resultado = n1 + n2
    print(f"A soma de {n1} + {n2} é: {resultado}")
elif op == "-":
    resultado = n1 - n2
    print(f"A subtração de {n1} - {n2} é: {resultado}")
elif op == "*":
    resultado = n1 * n2
    print(f"A multiplicação de {n1} * {n2} é: {resultado}")
elif op == "/":
    if n2 == 0:
        print("Divisão com 0 não e valido")
    else:
        resultado = n1 / n2
    print(f"A divisão de {n1} / {n2} é: {resultado}")
