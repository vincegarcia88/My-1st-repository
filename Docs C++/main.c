#include <stdio.h>
#include <stdlib.h>  // Adiciona a biblioteca necess�ria

/ int main() {  // Adiciona o tipo de retorno na fun��o main
    int soma, num1, num2;
    
    printf("Informe o primeiro n�mero: ");
    scanf("%d", &num1);  // L� o primeiro n�mero
    
    printf("Informe o segundo n�mero: "); // Adiciona entrada para o segundo n�mero
    scanf("%d", &num2);  // Correto: l� o segundo n�mero

    soma = num1 + num2;  // Calcula a soma

    printf("Resultado da soma: %d", soma);  // Imprime o resultado da soma

    return 0;
    
/*****************************************************************    
/*****************************************************************

// Trabalhando com caractere e CHAR

void main ()
{
	char produto [30];
	printf("Informe o nome do produto: \n");
	scanf("\n[^\n]s", &produto);
	
	printf("Produto: %s \n", produto);
}

/******************************************************************
/******************************************************************

// Trabalhando com caractere e CHAR

void main ()
{
	char produto [30];
	printf("Informe o nome do produto: \n");
	scanf("\n[^\n]s", &produto);
	
	printf("Produto: %s \n", produto);
}

/*******************************************************************
/*******************************************************************

// Fun��o fgets()
 
// Outra forma de resolver o problema, apresentado pelo scanf() ao ler textos, � utilizar
// a fun��o fgets(). Ela armazena corretamente o texto, mesmo quando este � composto
// por 2, 3 ou mais palavras, desde que, seja respeitado o tamanho limite determinado para o CHAR.

void main ()
{
	char produto [30];
	printf("Informe o nome do produto: \n");
	fgets(produto, 30, stdin);
	
	printf("Produto: %s \n", produto);
}

/********************************************************************
/********************************************************************

void main () {
	int soma, num1, num2;
	//trecho respons�vel pela entrada dos dados
	
	printf("Informe o primeiro numero: ");
	scanf("%d", &num1); //leitura de num1
	
	printf("Informe o segundo numero: ");
	scanf("%d", &num2); 
	
	/* O trecho a seguir e responsavel pela soma dos valores
	
	soma = num1 + num2;
	
	printf("Resultado da soma: %d", soma);
}
