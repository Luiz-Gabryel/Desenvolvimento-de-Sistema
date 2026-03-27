print("---Seja Bem-Vindo---")
print("Escolha uma Opção")
print("I - Infantil")
print("E - Estudante")
print("N - Normal")
print("Autismo - Pessoa com Deficiência")
print("IDOSO - Idoso")

opcao = input("Digite a sua opção: ")

if opcao == "I":
    print("O preço do ingresso Infantil é R$ 10,00")
elif opcao == "E":
    print("O preço do ingresso Estudante é R$ 15,00")
elif opcao == "N":
    print("O preço do ingresso Normal é R$ 30,00")
elif opcao == "IDOSO":
    print("O preço do ingresso Idoso é R$ 15,00")
elif opcao == "Autismo" or "autismo":
    codigo = input("Digite o código Autismo: ")
    if codigo == "CID F84" or "cid f84":
        print("Código válido! Seu ingresso é Gratuito.")
    else:
        print("Código inválido! Tente novamente.")
else:
    print("Opção inválida.")
