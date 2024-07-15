'''Cria um programa que peça o nome do utilizador e dê uma
mensagem de boas vindas com o nome do utilizador.

Ex: “Olá, Ricardo. Damos as boas vindas ao
nosso programa.”'''

from time import sleep

#Pedir o nome
nome = (input("Qual o seu nome? "))

print("A carregar...")
sleep (0.5)

#Imprimir a frase de boas vindas
print(f"Olá, {nome}! Damos as boas vindas ao nosso programa!")

