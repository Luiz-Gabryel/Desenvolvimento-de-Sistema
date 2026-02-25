#determina se uma pessoa deve ou não pagar imposto.

nome = input("Qual o seu nome: ")
salario = float(input("Qual seu salario: "))
imposto = float(1200)

if salario >= imposto:
    print(f"{nome}, voce vai ter que pagar imposto pelo seus R$ {salario}")

else:
    print(f"{nome}, voce não paga imposto pelo seus R$ {salario}")