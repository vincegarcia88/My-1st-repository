#Faça um programa que mostre a tabuada
#de um número introduzido pelo
#utilizador.

num1 = int(input("Insira um número: "))

for c in range (1,11):
    print (f"{num1}x{c} = {num1 * c}")