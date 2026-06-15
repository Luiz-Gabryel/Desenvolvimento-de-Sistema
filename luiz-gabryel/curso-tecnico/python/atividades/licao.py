# Programa de Gerenciamento de Tarefas

def exibir_lista_tarefas(lista_de_tarefas):
    """Exibe cada tarefa da lista no console.
    
    Esta função NÃO possui retorno (retorna None por padrão).
    """
    if not lista_de_tarefas:
        print("(Nenhuma tarefa cadastrada)")
    for tarefa in lista_de_tarefas:
        print(f"- {tarefa}")


def contar_total_tarefas(lista_de_tarefas):
    """Conta e retorna a quantidade de itens na lista.
    
    Esta função POSSUI retorno (inteiro).
    """
    return len(lista_de_tarefas)


def obter_primeira_tarefa(lista_de_tarefas):
    """Retorna o primeiro item da lista ou 'vazio' se estiver vazia.
    
    Esta função POSSUI retorno (string).
    """
    if len(lista_de_tarefas) == 0:
        return "vazio"
    return lista_de_tarefas[0]


# --- Bloco de Testes Otimizado ---

# Caso 1: Teste com lista normal
tarefas = ["estudar", "treinar", "entregar trabalho"]

print("--- LISTA NORMAL ---")
print("Lista:")
exibir_lista_tarefas(tarefas)
print("Qtd:", contar_total_tarefas(tarefas))
print("Primeira:", obter_primeira_tarefa(tarefas))

print("\n" + "="*20 + "\n")

# Caso 2: Teste com lista vazia
tarefas_vazias = []

print("--- LISTA VAZIA ---")
print("Lista:")
exibir_lista_tarefas(tarefas_vazias)
print("Qtd:", contar_total_tarefas(tarefas_vazias))
print("Primeira:", obter_primeira_tarefa(tarefas_vazias))
 #Feito por luiz