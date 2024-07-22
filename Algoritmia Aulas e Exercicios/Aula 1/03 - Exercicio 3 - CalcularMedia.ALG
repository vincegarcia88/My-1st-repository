Algoritmo "CalcularMedia"

//Calcular e imprimir a média aritmética das notas de um grupo
//de três alunos. As notas deverão ser lidas, uma para cada aluno, através
//de uma unidade de entrada qualquer, por exemplo, o teclado.

Var
// Seção de Declarações das variáveis 

n1, n2, n3, media: real

Inicio

// Seção de Comandos, procedimento, funções, operadores, etc... 

escreva ("Insira a primeira nota: ")
leia (n1)
escreva ("Insira a segunda nota: ")
leia (n2)
escreva ("Insira a terceira nota: ")
leia (n3)

media <- (n1 + n2 + n3) /3
escreva ("A média aritmética das notas é: ",media)
leia (media)

Fimalgoritmo