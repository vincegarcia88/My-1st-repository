'''Cria um programa que leia um número introduzido pelo utilizador
e que mostre o seu antecessor e sucessor.'''

#Pedir o número
n1 = int(input ("Escolha um número: "))

#Fazer o cálculo
antecessor = n1 - 1
sucessor = n1 + 1

#Apresentar a solução
print ("O antecessor de", n1, "é", antecessor, "\nE seu sucessor é",sucessor,".")