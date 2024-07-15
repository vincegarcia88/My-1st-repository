'''Desenvolva um programa em Python que permita ao
utilizador calcular o seu Índice de Massa Corporal (IMC).

O programa deve solicitar ao utilizador a sua
altura e o seu peso. De seguida, deve calcular o IMC e o
programa deve exibir uma mensagem com base no valor do
IMC calculado.

● IMC abaixo de 18,5: Abaixo do peso
● IMC entre 18,5 e 24,9: Peso normal
● IMC entre 25,0 e 29,9: Sobrepeso
● IMC entre 30,0 e 34,9: Obesidade grau 1
● IMC entre 35,0 e 39,9: Obesidade grau 2
● IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)

from time import sleep

altura = float(input("Informe a sua altura: "))
peso = int(input("Informe o seu peso corporal: "))

Imc = peso / (altura*altura)
print("A calcular...")
sleep (1)
print(f"O seu IMC é de {Imc:.2f}.")

if Imc < 18.5:
    print ("Você está abaixo do peso.")

elif Imc >= 18.5 and Imc <= 24.9:
    print ("Você está no peso ideal.")

elif Imc >=25.0 and Imc < 29.9:
    print ("Você tem sobrepeso.")

elif Imc >=30.0 and Imc <=34.9:
    print ("Você tem obesidade grau 1.")

elif Imc >= 35.0 and Imc <=39.9:
    print ("Você tem obesidade grau 2.")

elif Imc >=40:
    print ("Você tem obesidade mórbida.")'''