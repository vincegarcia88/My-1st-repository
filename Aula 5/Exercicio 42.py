'''Crie o jogo da adivinha v2.0. O
computador deve “pensar” num número de
0 a 10 e o utilizador deve adivinhar o
número escolhido. Só que agora o jogador vai tentar adivinhar até
acertar. No final mostre quantas tentativas foram necessárias.'''

from random import randint

numero = randint(0, 10)
numero_escolhido = int(input("Adivinhe o número escolhido: "))
c = 0
'''copiar em casa'''
while opcao != opcao:
    opcao = int(input("Palpite: "))
    tentativas += 1

    if opcao < numero_escolhido:
        print("Parabéns, você acertou!")
        c += 1
    elif numero > numero_escolhido:
        print(f"Errou! Tente novamente. O número era {numero} . ")
        c += 1
    else:
        print(f'WIN and {c}')
    break