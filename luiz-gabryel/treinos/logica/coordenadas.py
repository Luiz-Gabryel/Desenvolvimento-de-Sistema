posicao = [0, 0, 0]

print("--- Coordenadas ---")
print("1 = Sim ; 2 = Não")
escolha = int(input("Quer Digitar Coordenadas? "))

if  escolha == 1:
    posicao[0] = float(input("Digite X: "))
    posicao[1] = float(input("Digite y: "))
    posicao[2] = float(input("Digite z: "))
    print(f"Sua posição é: X={posicao[0]}, Y={posicao[1]}, Z={posicao[2]}")


elif escolha == 2:
    print("Ok, Adeus")

else:
    print("Erro")











# x = [0]
# y = [0]
# z = [0]

# coordenada_x = float(input("Qual sua coordenada x: "))
# coordenada_y = float(input("Qual sua coordenada y: "))
# coordenada_z = float(input("Qual sua coordenada Z: "))


# print(f"Sua cordenadas são: {x}, {y}, {z}")


