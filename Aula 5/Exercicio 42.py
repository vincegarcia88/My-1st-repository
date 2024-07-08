0 a 10 e o utilizador deve adivinhar o
número escolhido. Só que agora o
jogador vai tentar adivinhar até
acertar. No final mostre quantas
tentativas foram necessárias.'''

from random import randint

numero = randint (0,10)
numero_escolhido = int(input("Adivinhe o número escolhido: "))
c = 0

while True:
    if numero == numero_escolhido:
        print("Parabéns, você acertou!")
        break
    else:
        print(f"Errou! Tente novamente. O número era {numero} . ")
        continue
