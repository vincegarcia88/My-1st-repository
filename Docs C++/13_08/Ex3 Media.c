#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

/* 3. Fa�a um programa em C que imprima a m�dia aritm�tica entre os n�meros 5, 8, 12*/

int main(int argc, char *argv[]) {
	int nota1 = 5;
	int nota2 = 8;
	int nota3 = 12;
	int media = (nota1 + nota2 + nota3)/3;
	
	printf ("Media = %d.\n",media);
	
	return 0;
}
