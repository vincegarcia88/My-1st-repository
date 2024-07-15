'''Cria um programa que simule uma conversa:
Ex: Olá, eu sou um BOT, como te chamas?
Dou-te as boas vindas “nome”, Que idade tens?
Fantástico, já tens “idade” anos. És de onde?
Uau, “cidade”?? Nunca visitei!'''

from time import sleep

#Montar o diálogo e pedir os dados

print ("Olá, eu sou o Bot do Python!")
sleep(1)
print("...")
sleep (1)
print ("Como você se chama?")
sleep (1)

nome = input("Digite o seu nome -> ")
sleep(1)
print("...")
sleep(1)

print(f"Dou-te as boas vindas, {nome}!")
sleep(1)
print("...")
sleep(1)
print("Que idade tens?")
sleep(1)

idade = int(input("Informe a sua idade -> "))
sleep (1)
print("...")
sleep (1)

print(f"Fantástico! Já tens {idade} anos!")
sleep(1)
print("...")
sleep(1)
print("És de onde?")
sleep(1)

cidade = input("Informe a sua cidade -> ")
sleep(1)
print("...")
sleep (1)

print(f"Uau! {cidade}? Nunca visitei!")
sleep (1)
print("...")
sleep(1)
print("Sensacional, até mais!")