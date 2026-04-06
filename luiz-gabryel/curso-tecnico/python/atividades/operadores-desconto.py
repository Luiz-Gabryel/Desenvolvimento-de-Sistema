#Exercícios
#1.	Testando operadores
print("Esse e o Exercicio 1")
print("Calculo: 10 > 5 = ", 10 > 5)
print("Calculo: 7 == 7 = ", 7 == 7)
print("Calculo: 15 < 1 = ", 15 < 1)
print("Calculo: 20 >= 2 = ", 20 >= 2)
print("Calculo: 8 <= 10 = ", 8 <= 10)
print("Calculo: 100 != 10 = ", 100 != 10)
print("Calculo: -5 < 0 = ", -5 < 0)
print("Calculo: 4 > 2 = ", 4 > 2)
#add mais 3
print("Calculo: 50 > 10 = ", 50 > 10)
print("Calculo: 100 <= 50 = ", 100 <= 50)
print("Calculo: 1.5 > 1.2 = ", 1.5 > 1.2)
print("Fim Exercicio 1")
#Fim do 1. Exercicio

#2.	Sistema de desconto
print("Esse e o exercicio 2")
compra = float(input("Qual o valor da sua compra? "))

if compra >= 100:
    print(f"Nossa, sua compra foi de {compra}, vamos entregar um desconto de 10% para voce")
    desconto = compra - (compra * 0.10)
    print(f"Sua compra agora ficou por {desconto}")

elif compra >= 200:
    print(f"Nossa, sua compra foi de {compra}, vamos entregar um desconto de 10% para voce")
    desconto = compra - (compra * 0.12)
    print(f"Sua compra agora ficou por {desconto}")

elif compra >= 300:
    print(f"Nossa, sua compra foi de {compra}, vamos entregar um desconto de 10% para voce")
    desconto = compra - (compra * 0.15)
    print(f"Sua compra agora ficou por {desconto}")
print("Fim do exercico 2")

#3. Decisão: O computador não fica na dúvida. Ou a resposta é sim ou é não. Se for verdade, ele segue um caminho; se for mentira, ele faz outra coisa. É assim que ele escolhe o que fazer.
#4. Regra: O > só serve se for maior mesmo. O >= aceita se for igual também. Você usa o >= quando o número do limite já é o suficiente.
#5. Senha: Você olha se o tamanho da senha >= 8. Se a pessoa digitar exatamente 8 letras, o sistema deixa passar.