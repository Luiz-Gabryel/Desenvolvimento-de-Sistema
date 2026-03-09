#sistema de classificação de idade.

idade = int(input("Qual sua idade: "))

if idade <= 12:
    print("Entrada gratuita em cinemas")
elif 13 <= idade <= 17:  
    print("Meia entrada garantida")
elif 18 <= idade <= 64:  
    print("Pode dirigir e votar")
elif idade >= 65:
    print("Prioridade em filas")