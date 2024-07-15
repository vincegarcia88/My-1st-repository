'''Crie um programa que peça um número ao
utilizador e que apresente a sua tabuada.'''

#Pedir o número
num1 = int(input("Digite um número: "))

#Cálculo
for i in range (1,11):
    resultado = num1*i

#Apresentar o resultado
    print(f"{num1} x {i} = {resultado}")

