Algoritmo "divisao"
// Disciplina   : [Linguagem e Lógica de Programação]
// Aluno   : Luiz Gabryel 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 02/03/2026
Var
// Seção de Declarações das variáveis 
n1, n2, r : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva ("Digite o 1º Valor: ")
leia (n1)
escreva ("Digite o 2º Valor: ")
leia (n2)
se n2 = 0 entao
   escreva ("Não podemos fazer tal operação")
senao
   r <-- n1 / n2
   escreval ("Resultado e:", r)

fimse
Fimalgoritmo