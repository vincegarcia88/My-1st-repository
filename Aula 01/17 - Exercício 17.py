'''Cria um programa que peça o ano de nascimento do utilizador
e o ano atual, e que calcule a idade do utilizador.'''

from time import sleep

#Código básico abaixo:
anoNasc = int(input ("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

#Cálculo dos anos
idade = anoAtual - anoNasc

#Apresentar o resultado
print ("Você tem",idade,"anos de idade.")

sleep(1)
print("...")
sleep(1)

#A utilizar a biblioteca Datetime

import datetime

#Pedir o ano de nascimento
anoNasc = int(input("Insira o seu ano de nascimento -> "))

#Calcular conforme a biblioteca datetime
datetime

#Apresentar o resultado
print(f"A sua idade é de {idade} anos.")
