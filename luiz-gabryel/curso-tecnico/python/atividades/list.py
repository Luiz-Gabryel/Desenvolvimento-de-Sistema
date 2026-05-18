lista = [10, 20, 30, 20, 50]

print("--- Executando O(n²) ---")
comp_lento = 0
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        comp_lento += 1
        if lista[i] == lista[j]:
            print(f"Duplicado encontrado no O(n²): {lista[i]}")
print(f"Total de comparações O(n²): {comp_lento}\n")

print("--- Executando O(n) ---")
vistos = set()  
comp_rapido = 0
for elemento in lista:
    comp_rapido += 1
    if elemento in vistos:
        print(f"Duplicado encontrado no O(n): {elemento}")
    else:
        vistos.add(elemento)
print(f"Total de comparações O(n): {comp_rapido}")
