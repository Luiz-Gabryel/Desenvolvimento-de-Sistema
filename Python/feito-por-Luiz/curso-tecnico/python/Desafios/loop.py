while True:
    print("=== Controle de estoque de Livro ===")
    print()
    print("1. Ver status de todos os livros")
    print("2. Ver ou Atualizar um livro")
    print("3. Adicionar novo livro")
    print("4. Sair")
    print()

    opcao = input("Diigite sua opção:")

    if opcao == "4":
        print("Saindo")
        break
    else:
        print("Tente Novamente")
        print("Sistema em Atualização")