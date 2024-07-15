'''Faça um programa que leia 10 números e conte quantos deles são pares.'''

numerosPares = 0

for c in range(0, 10):
    numero = int(input(f'Digite o {c+1}º número: '))
    if numero % 2 == 0:
        numerosPares += 1

print(f'Inseriu {numerosPares} números pares.')