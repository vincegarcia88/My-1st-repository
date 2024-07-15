'''Faça um programa que leia 5 números inteiros e mostre a soma desses números.'''

print("")
soma = 0
numeros = 0

for c in range(0,5):
    numeros = int(input(f'Digite o {c+1}º número: '))
    soma += numeros

print(f'A soma dos números é: {soma}')