import time
import os 

numero = int(input("Digite um numero: "))
for i, valor in enumerate(range(1, numero + 1)):
    if i %2 == 0:
        v = "Impa"
    else:
        v = "Par"
        

    print(f'O índice é {i} e o valor é {valor} e ainda e {v}')
    time.sleep(2)
    print("Limpando tela...")
    os.system('cls' if os.name == 'nt' else 'clear')
    
# for i, valor in enumerate(range(1, numero - 1 )):
#     print(f'O índice é {i} e o valor é {valor} e ainda e {v}')
#     time.sleep(2)
#     os.system('cls' if os.name == 'nt' else 'clear')

