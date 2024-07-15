'''Cria um programa que peça o nome, idade e a cidade onde
mora. Depois faça uma apresentação com todos os
elementos recebidos.

Ex: “Olá, o meu nome é Ricardo, tenho 32 anos
e sou do Porto.”'''

from time import sleep

#Pedir os dados
nome = input("Insira o seu nome -> ")
idade = int(input("Informe a sua idade -> "))
cidade = input("Informa a cidade onde vives -> ")

sleep(0.5)
print ("A carregar...")
sleep(1)
print ("...")
sleep(1)

#Apresentar a frase
print(f"Olá, o meu nome é {nome}, minha idade é {idade} e minha cidade é {cidade}.")