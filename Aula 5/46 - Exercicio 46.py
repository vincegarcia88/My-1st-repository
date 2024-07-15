'''Crie um programa que leia vários números inteiros e que termine apenas
quando o utilizador digitar a opção para parar. No final mostre quantos
números o utilizador inseriu e qual a soma entre eles.'''

qtdNumeros = 0
soma = 0

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    else:
        qtdNumeros += 1
        soma += numero

print(f'Digitou {qtdNumeros} numeros')
print(f'A soma é {soma}')