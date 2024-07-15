'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

#Pedir os dados
numero = int(input('Digite um número: '))
controle = 0

#
for c in range(0, numero):
    if numero % (c + 1) == 0:
        controle += 1

if controle == 2:
    print(f'O número {numero} É PRIMO.')
else:
    print(f'O número {numero} NÃO É PRIMO.')


