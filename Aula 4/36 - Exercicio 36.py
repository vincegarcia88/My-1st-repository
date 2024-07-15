'''Faça um programa que mostre a tabuada de um número introduzido pelo utilizador.'''

print("")
numero = int(input("Insira o número-> "))

for c in range (0,11):
    tabuada = c * numero
    print (f"{numero} x {c} = {tabuada}")