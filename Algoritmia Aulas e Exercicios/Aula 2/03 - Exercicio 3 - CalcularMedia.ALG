Algoritmo "CalcularMedia"

//Calcular e imprimir a m�dia aritm�tica das notas de um grupo
//de tr�s alunos. As notas dever�o ser lidas, uma para cada aluno, atrav�s
//de uma unidade de entrada qualquer, por exemplo, o teclado.

Var
// Se��o de Declara��es das vari�veis 

n1, n2, n3, media: real

Inicio

// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva ("Insira a primeira nota: ")
leia (n1)
escreva ("Insira a segunda nota: ")
leia (n2)
escreva ("Insira a terceira nota: ")
leia (n3)

media <- (n1 + n2 + n3) /3
escreva ("A m�dia aritm�tica das notas �: ",media)
leia (media)

Fimalgoritmo