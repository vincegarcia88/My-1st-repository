#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

/* Faça um programa em C que leia um número inteiro e imprima o seu antecessor e o seu sucessor */

int main(int argc, char *argv[]) {
	
	int num1, antecessor, sucessor;
	
	printf("Escreva um numero: ");
	scanf ("%d", &num1);
	
	antecessor = num1 - 1;
	sucessor = num1 + 1;
	
	printf("O numero escolhido foi %d\n", num1);
	printf("o seu antecessor e %d\n", antecessor);
	printf("e o seu sucessor e %d\n", sucessor);
	
	return 0;
}
