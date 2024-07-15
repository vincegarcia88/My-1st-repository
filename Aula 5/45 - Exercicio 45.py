'''Escreva um programa que leia um número N inteiro qualquer e mostre os N
primeiros elementos de uma sequência de Fibonacci.'''

# ler um número inteiro
numero = int(input('Digite um número: '))

# pedir número que seja superior a 1, para validar o pedido anterior
while True:
    if numero < 1:
        print('Número inválido.')
        numero = int(input('Digite um número inteiro maior que zero: '))
    else:
        break

inicio, atual = 0, 1
contador = 0

while contador < numero:
    if contador == numero - 1:
        print(f'{inicio}', end='')
    else:
        print(f'{inicio} -> ', end='')
    inicio, atual = atual, inicio + atual
    contador += 1