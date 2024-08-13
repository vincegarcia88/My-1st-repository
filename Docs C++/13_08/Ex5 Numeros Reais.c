#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

main() {
	
	float num1, num2;
	
	printf("Informe um numero: ");
	scanf ("%f", &num1);
	
	printf("Informe outro numero: ");
	scanf ("%f", &num2);
	
	printf("Os numeros escolhidos sao %.2f e %.2f:", num1, num2);
	return 0;
}
