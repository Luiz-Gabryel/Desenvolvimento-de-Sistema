#Sistema de Controle de Estoque de Livros, com login e senha, e com opções de adicionar,ver status de todos os livros, procurar livro e remover livro.
#ainda fazendo ajustes, ainda não está completo.
#luiz gabryel 2026 fev

print('Seja bem vindo ao Controle de Estoque de Livros')# Pede usuário e senha

user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
if user == '' or senha == '': # ele valida se tem algo, se nao tem, nao acessa
    print('Por favor, tente novamente, faltou algo')
    exit()
else:
    print(f'Seja bem vindo, {user}')

livros = []  # lista onde fica livros

while True: #opções
    print('--- Sistema ---')
    print('1 Ver todos os livros')
    print('2 Adicionar um livro')
    print('3 Procurar um Livro')
    print('4 Remover livro')
    print('5 Deslogar')
    print('-'*30)
    opcao = input('Digite sua opção:')

    if opcao == '1':  # olha os livros
        print('--- Livros ---')
    
        if not livros: #ve se tem livros, se tem, ele mostra
            print('Nenhum livro cadastrado.')
        else:
            for livro, quantidade in livros:
                print(f'{livro} - {quantidade} Livros')
        print('--- Fim ---')
                
    elif opcao == '2':
        livro = input('Digite o nome do livro: ')
        if livro == '':
            print('Tente novamente')
        else:
            quantidade = input('Digite a quantidade: ')
            livros.append((livro, quantidade))
            print(f'O livro {livro} foi adicionado com sucesso!')

    elif opcao == '3':
        busca = input('Digite o nome do livro: ')
        encontrado = False # so muda se tiver um livro foi encontrado
        for livro, quantidade in livros: #ve  toda a lista de livro, pegando o nome e quantidade
            if livro == busca: # se tiver ele vai mostrar livro e quantidade
                print(f'{livro} - {quantidade} quantidade')
                encontrado = True
                break
        if not encontrado:
            print('Livro não encontrado.')

    elif opcao == '4':
        remover = input('Qual livro quer remover? ')
        encontrado = False #comeca com false, se achar, vai pra true
        for livro, quantidade in livros: #ele ve  a lista toda
            if livro == remover:
                encontrado = True #marca como achou
                confirma = input('Digite sua senha para confirmar: ')
            if confirma == senha: #se senha for a mesma do confirmar ele removee
                livros.remove((livro, quantidade)) #senha certa = remove
                print(f'O livro {livro} foi removido com sucesso!')
            else: #senha errada = nao remove
                print('Senha errada, livro não removido.')
            break
    if not encontrado: #se nao achou
        print('Livro não encontrado.') 
                
    elif opcao == '5':  #deslogar somente se a senha for inserida
        sair = input('Confirme sua senha, para sair: ')
        if sair == senha:
            print(f'Volte sempre...{user}')
            break
        else:
            print('Senha errada, tente novamente')
            
            
    else:
        print('Opção inválida, tente novamente')