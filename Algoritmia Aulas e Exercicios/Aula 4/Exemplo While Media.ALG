Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/07/2024
Var
// Se��o de Declara��es das vari�veis 
num, soma, cont: inteiro
media: real
op: caractere

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
soma <- 0
cont <- 0
op <- "S"

   enquanto OP = "S" faca
            escreva ("Insira um n�mero: ")
            leia (num)
            soma <- soma + num
            cont <- cont + 1
            escreva ("Deseja continuar? (S/N): ")
            leia op
   fimenquanto
   media <- soma / cont
   escreva ("M�dia = ", media)

fimalgoritmo

Fimalgoritmo