Algoritmo "semnome"
// Elaborar um algoritmo que leia o sexo e a altura de uma pessoa e
// imprima o peso ideal.

// Dados: Peso ideal para o sexo masculino: altura (cm) *0,95 - 95
//Peso ideal para o sexo feminino: altura (cm) * 0.85 - 85

Var
// Se��o de Declara��es das vari�veis 

sexo:caractere
altura, peso:real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

escreva ("Informe o seu sexo (M) Masculino (F) Feminino: ")
leia(sexo)

escreva ("Informe a sua altura: ")
leia(altura)

se sexo = "M" entao
peso <- altura * 0.95 - 95
fimse

se sexo = "F" entao
peso <- altura * 0.85 - 85
fimse

escreva("O seu peso ideal �: ", peso)

Fimalgoritmo