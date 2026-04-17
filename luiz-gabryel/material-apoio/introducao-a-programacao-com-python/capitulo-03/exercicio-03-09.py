dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos

print(f"Total de segundos: {total} segundos")

# 1 minuto = 60 segundos
# 1 hora = 60 minutos = 60 × 60 = 3600 segundos
# 1 dia = 24 horas = 24 × 3600 = 86400 segundos