#Crie um programa que peça um número ao
#utilizador e que apresente a sua
#tabuada.

numero = int(input ("Digite um número: "))

for i in range  (1,10):
    resultado = numero * i
    print (f"{numero} * {i} = {resultado}")