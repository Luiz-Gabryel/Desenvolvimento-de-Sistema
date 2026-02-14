#Sistema de Controle de Estoque de Livros, com login e senha, e com opções de adicionar e ver status de todos os livros.
#ainda fazendo ajustes, ainda não está completo.
#luiz gabryel 2026 fev

print("Seja bem vindo ao Controle de Estoque de Livros")
print("-" * 30)
# Pede usuário e senha
user = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
print("-" * 30)
if user == "" or senha == "":
    print("Por favor, tente novamente, faltou algo")
    exit()
else:
    print(f"Seja bem vindo, {user}")
print("-" * 30)
livros = []  # lista onde fica livros

while True: #opções
    print("--- Sistema ---")
    print("1 Ver todos os livros")
    print("2 Adicionar um livro")
    print("3 Deslogar")
    print("-" * 30)
    opcao = input("Diigite sua opção:")
    print("-" * 30)
    if opcao == "1":  # olha os livros
        print("--- Livros ---")
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in livros:
                print(livro)
        print("- Fim -")
                
        #for livro in livros:
            #print(livro)
        #print("- Fim -")

    elif opcao == "2":  #add livro
        livro = input("Digite o nome do livro: ")
        if livro == "":
            print("Tente novamente")
        else:
            livros.append(livro)
        print(f"O livro {livro} foi adicionado com sucesso!")

    elif opcao == "3":  #deslogar somente se a senha for inserida
        sair = input ("Confirme sua senha, para sair: ")
        if sair == senha:
            print(f"Volte sempre...")
            break
        else:
            print("Senha errada, tente novamente")

#So parte de codigo antigo

  #for livro in livros:
            #print(livro)
        #print("- Fim -")