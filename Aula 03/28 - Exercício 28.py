'''Crie o jogo da adivinha v1.0.
O computador deve “pensar” num número de
0 a 7 e o utilizador deve adivinhar o número escolhido.

O programa deve apresentar se o utilizador venceu ou perdeu.'''

#Importar biblioteca
from random import randint

#Código do número da CPU e Indicar número do utilizador
numeroCPU = randint(0,7)
numero_escolhido = int(input("Insira o seu número -> "))

#Imprimir os resultados
if numero_escolhido == numeroCPU:
    print("Você acertou o número escolhido!")

else:
    print(f"Errou! O número escolhido foi {numeroCPU}.")



