a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))  # Mostra o tipo da variavel
print('Só tem espaços? ', a.isspace())  # Verifica se tem apenas espaços
print('É um número? ', a.isnumeric())  # Verifica se é apenas por números
print('É alfabético? ', a.isalpha())  # Verifica se tem apenas letras
print('É alfanumérico? ', a.isalnum())  # Verifica se tem letras ou números
print('Está em maiúsculas? ', a.isupper())  # Verifica se todas as letras estão maiúsculas
print('Está em minúsculas? ', a.islower())  # Verifica se todas as letras estão minúsculas
print('Está capitalizada? ', a.istitle())  # Verifica se está no formato Título