#Sistema de Controle de Estoque de Livros, com login e senha, e com opções de adicionar e ver status de todos os livros.
#ainda fazendo ajustes, ainda não está completo.
#luiz gabryel 2026 fev

print("Seja bem vindo ao Controle de Estoque de Livros")# Pede usuário e senha

user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
if user == "" or senha == "": # ele valida se tem algo, se nao tem, nao acessa
    print("Por favor, tente novamente, faltou algo")
    exit()
else:
    print(f"Seja bem vindo, {user}")

livros = []  # lista onde fica livros

while True: #opções
    print("--- Sistema ---")
    print("1 Ver todos os livros")
    print("2 Adicionar um livro")
    print("3 Deslogar")
    print("-"*30)
    opcao = input("Digite sua opção:")

    if opcao == "1":  # olha os livros
        print("--- Livros ---")
    
        if not livros: #ve se tem livros, se tem, ele mostra
            print("Nenhum livro cadastrado.")
        else:
            for livro, quantidade in livros:
                print(f"{livro} - {quantidade} Livros")
        print("--- Fim ---")
                
    elif opcao == "2":
        livro = input("Digite o nome do livro: ")
        if livro == "":
            print("Tente novamente")
        else:
            quantidade = input("Digite a quantidade: ")
            livros.append((livro, quantidade))
            print(f"O livro {livro} foi adicionado com sucesso!")

    elif opcao == "3":  #deslogar somente se a senha for inserida
        sair = input("Confirme sua senha, para sair: ")
        if sair == senha:
            print(f"Volte sempre...{user}")
            break
        else:
            print("Senha errada, tente novamente")