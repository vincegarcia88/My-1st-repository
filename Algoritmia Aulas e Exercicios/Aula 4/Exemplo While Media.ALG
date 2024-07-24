Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/07/2024
Var
// Seção de Declarações das variáveis 
num, soma, cont: inteiro
media: real
op: caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
soma <- 0
cont <- 0
op <- "S"

   enquanto OP = "S" faca
            escreva ("Insira um número: ")
            leia (num)
            soma <- soma + num
            cont <- cont + 1
            escreva ("Deseja continuar? (S/N): ")
            leia op
   fimenquanto
   media <- soma / cont
   escreva ("Média = ", media)

fimalgoritmo

Fimalgoritmo