# --- ENTRADA ---
idade_cliente = int(input("Digite a idade do cliente: "))

# --- PROCESSAMENTO ---
#1) idade menor ou igual a 12 anos
# 2) idade maior ou igual a 60 anos
if idade_cliente <= 12 or idade_cliente >= 60:
    # --- SAÍDA: tem desconto ---
    mensagem_final = "Cliente tem direito a desconto."
else:
    # --- SAÍDA: sem desconto ---
    mensagem_final = "Cliente não tem direito a desconto."

# Resultado
print(mensagem_final)