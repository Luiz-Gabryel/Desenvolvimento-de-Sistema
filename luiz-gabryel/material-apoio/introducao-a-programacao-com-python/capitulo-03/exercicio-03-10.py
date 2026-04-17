salario = float(input("Digite o salário atual: "))
p_aumento = float(input("Digite a porcentagem de aumento: "))

aumento = salario * p_aumento / 100
novo_salario = salario + aumento

print(f"Um aumento de {p_aumento}% em um salário de R$ {salario}")
print(f"é igual a um aumento de R$ {aumento}")
print(f"Resultando em um novo salário de R$ {novo_salario}")