#Sistema de classificação de idade.

idade = int(input("Qual sua idade: "))

if idade <= 12:
    print("Classficação: Criança")
    print("Permissão: Entrada gratuita em cinemas")
elif 13 <= idade <= 17:
    print("Classficação: Adolecente") 
    print("Permissão Meia entrada garantida")
elif 18 <= idade <= 64:
    print("Classificação: Adulto")
    print("Permissão: Pode dirigir e votar")
elif idade >= 65:
    print("Classificação: Idoso")
    print("Permissão: Prioridade em filas")