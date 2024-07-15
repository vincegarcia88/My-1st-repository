'''Crie o seguinte menu que leia a opção que escolheu:
--- Calculadora ---
[ 1 ] – Tabuada
[ 2 ] – Calculadora
[ 3 ] – Fatorial
[ 4 ] – Números primos
Escolheste a opção “opcao”'''

from time import sleep

#Entrada
print("=-=-=-=-=-=-=-=-=-=-=-=-=")
sleep(1)
print("=-=-=-Calculadora =-=-=-=")
sleep(1)
print("=-=-=-=-=-=-=-=-=-=-=-=-=\n")

sleep(1)

#Apresentar o menu
print("[1] - Tabuada")
print("[2] - Calculadora")
print("[3] - Fatorial")
print("[4] - Números primos\n")

#Pedir a opção desejada
opcao = int(input("Escolha a sua opção -> "))

#Apresentar o resultado
print(f"Você escolheu a opção {opcao} ")