#Programa onde dependendo do horario ele exiba a mensagem: Bom Dia, Boa Tarde, Boa Noite

#dia = input ("Qual Periodo é? (Manha, Tarde, Noite) ")

#if dia == "Manha" or dia == "manhã":
#    print("Bom Dia")
#elif dia == "Tarde" or dia == "tarde":
#    print("Boa Tarde")
#elif dia == "Noite" or dia == "noite":
#    print("Boa Noite")
#else:
#    print("As opções são: Manha, Tarde, Noite")

hora = int(input("Qual horas são: "))

if 0 <= hora < 12:
    print(f"Agora são {hora}h. Bom dia!")
elif 12 <= hora < 18:
    print(f"Agora são {hora}h. Boa tarde!")
else:
    print(f"Agora são {hora}h. Boa noite!")