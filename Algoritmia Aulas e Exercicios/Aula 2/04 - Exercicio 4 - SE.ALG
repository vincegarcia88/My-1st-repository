Algoritmo "semnome"
// Fazer um algoritmo que leia 2 n�meros inteiros A e B.
// Imprimir uma mensagem informando que A � maior que B.

Var
// Se��o de Declara��es das vari�veis 
n1, n2: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
escreva ("Informe o primeiro n�mero: ")
leia (n1)

escreva ("Informe o segundo n�mero: ")
leia (n2)

se (n1 > n2) entao
   escreva ("A � maior que B.")
   fimse

se (n2 > n1)entao
   escreva ("B � maior que A.")
   fimse
   
se (n2 = n1)entao
   escreva ("A e B s�o iguais.")
   fimse

fimalgoritmo