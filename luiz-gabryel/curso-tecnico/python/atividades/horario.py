#Programa onde dependendo do horario ele exiba a mensagem: Bom Dia, Boa Tarde, Boa Noite.

nome = input("Qual seu nome: ")
hora = int(input("Qual horas são: "))

if 0 <= hora < 12:
    print(f"Olá {nome}, Agora são {hora}h. Bom dia!")
elif 12 <= hora < 18:
    print(f"Olá {nome}, Agora são {hora}h. Boa tarde!")
elif 18 <= hora <= 24:
     print(f"Olá {nome}, Agora são {hora}h. Boa noite!")
else:
    print(f"{nome}, coloque um horário válido (entre 0 e 24).")