Algoritmo "semnome"
// Fazer um algoritmo que leia 2 números inteiros A e B.
// Imprimir uma mensagem informando que A é maior que B.

Var
// Seção de Declarações das variáveis 
n1, n2: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreva ("Informe o primeiro número: ")
leia (n1)

escreva ("Informe o segundo número: ")
leia (n2)

se (n1 > n2) entao
   escreva ("A é maior que B.")
   fimse

se (n2 > n1)entao
   escreva ("B é maior que A.")
   fimse
   
se (n2 = n1)entao
   escreva ("A e B são iguais.")
   fimse

fimalgoritmo