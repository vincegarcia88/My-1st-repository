#include <stdio.h>
#include <stdlib.h>  // Adiciona a biblioteca necessária

/ int main() {  // Adiciona o tipo de retorno na função main
    int soma, num1, num2;
    
    printf("Informe o primeiro número: ");
    scanf("%d", &num1);  // Lê o primeiro número
    
    printf("Informe o segundo número: "); // Adiciona entrada para o segundo número
    scanf("%d", &num2);  // Correto: lê o segundo número

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

// Função fgets()
 
// Outra forma de resolver o problema, apresentado pelo scanf() ao ler textos, é utilizar
// a função fgets(). Ela armazena corretamente o texto, mesmo quando este é composto
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
	//trecho responsável pela entrada dos dados
	
	printf("Informe o primeiro numero: ");
	scanf("%d", &num1); //leitura de num1
	
	printf("Informe o segundo numero: ");
	scanf("%d", &num2); 
	
	/* O trecho a seguir e responsavel pela soma dos valores
	
	soma = num1 + num2;
	
	printf("Resultado da soma: %d", soma);
}
