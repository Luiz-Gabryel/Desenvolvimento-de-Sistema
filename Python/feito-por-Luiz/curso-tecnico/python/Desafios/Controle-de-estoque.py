#Sistema de Controle de Estoque de Livros, com login e senha, e com opções de adicionar, remover, atualizar e ver status de todos os livros.
#ainda fazendo ajustes, ainda não está completo.
#luiz gabryel 2026 fev

print("Seja bem vindo ao Controle de Estoque de Livros")

# Pede usuário e senha
user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if user == "" or senha == "":  #se tiver faltando algo, ele ñ libera
    print("Por favor, tente novvamente, faltou algo")
else:
    print(f"Seja bem vindo, {user}")

livros = []  # lista onde fica livros

while True:
    print("Sistema")
    print("1 Ver todos os livros")
    print("2 Adicionar um livro")
    print("3 Deslogar")
    opcao = input("Diigite sua opção:")

    if opcao == "1":  # olha os livros
        print("--- Livros ---")
        for livro in livros:
            print(livro)
        print("- Fim -")

    elif opcao == "2":  #add livro
        livro = input("Digite o nome do livro: ")
        livros.append(livro)
        if livro =="" or livros =="":
            print("Tente novamente")
        else:
            print(f"O livro {livro} foi adicionado com sucesso!")

    elif opcao == "3":  #deslogar somente se a senha for inserida
        sair = input ("Confirme sua senha, para sair: ")
        if sair == senha:
            print(f"Volte sempre...")
            break
        else:
            print("Senha errada, tente novamente")

