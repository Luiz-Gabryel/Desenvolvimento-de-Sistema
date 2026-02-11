livros = []
  
while True:
    print("\n--- Controle de Estoque de Livros ---")
    print("1. Ver status de todos os livros")
    print("2. Ver ou Atualizar um livro")
    print("3. Adicionar novo livro")
    print("4. Sair\n")
    
    livros = []
    
    opcao = input("Diigite sua opção:")

    if opcao == "4":
        print("Saindo")
        break
    
    elif opcao == "3":
        livros = input("Qual o nome do livro? ")
        livros.append (livros)
        
    elif opcao =="2":
        print = (livros)
        
    
    else:
        print("Tente Novamente")
        print("Sistema em Atualização")