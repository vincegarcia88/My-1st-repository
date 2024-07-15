'''Crie o jogo pedra, papel e tesoura'''
from random import randint
from time import sleep

print("")
print("=-=-=-=-=-=-= PEDRA =-=-=-=-=-=-=-=")
print("=-=-=-= PAPEL -=-=-=-==-=-=-=-=-=-=")
print("=-=-=-=-=-=-=-=-=- TESOURA -=-=-=-=\n")

print("[1] Pedra\n[2] Papel\n[3] Tesoura\n")

jogador = int(input("Escolha sua jogada: "))
print("")
numeroCPU = randint(1,3)

if jogador == 1 and numeroCPU == 1:
    print("Você escolheu PEDRA!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu PEDRA também!")
    sleep(1)
    print("...")
    sleep(1)
    print("Empate! Tente novamente!")

elif jogador == 1 and numeroCPU == 2:
    print("Você escolheu PEDRA!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu PAPEL!")
    sleep(1)
    print("...")
    sleep(1)
    print("Você PERDEU!")

elif jogador == 1 and numeroCPU == 3:
    print("Você escolheu PEDRA!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu TESOURA!")
    sleep(1)
    print("...")
    sleep(1)
    print("Você VENCEU!")

elif jogador == 2 and numeroCPU == 1:
    print("Você escolheu PAPEL!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu PEDRA!")
    sleep(1)
    print("...")
    sleep(1)
    print("Parabéns! Você venceu!")

elif jogador == 2 and numeroCPU == 2:
    print("Você escolheu PAPEL!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU tabém escolheu PAPEL!")
    sleep(1)
    print("...")
    sleep(1)
    print("Empate! Tente novamente!")

elif jogador == 2 and numeroCPU == 3:
    print("Você escolheu PAPEL!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu TESOURA!")
    sleep(1)
    print("...")
    sleep(1)
    print("Você perdeu!")

elif jogador == 3 and numeroCPU == 1:
    print("Você escolheu TESOURA!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu PEDRA!")
    sleep(1)
    print("...")
    sleep(1)
    print("Você PERDEU!")

elif jogador == 3 and numeroCPU == 2:
    print("Você escolheu TESOURA!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU escolheu PAPEL!")
    sleep(1)
    print("...")
    sleep(1)
    print("Você VENCEU!")
elif jogador == 3 and numeroCPU == 3:
    print("Você escolheu TESOURA!")
    sleep(1)
    print("...")
    sleep(1)
    print("A CPU também escolheu TESOURA!")
    sleep(1)
    print("...")
    sleep(1)
    print("Empate! Tente novamente!")

else:
    print("Obrigado por jogar!")





