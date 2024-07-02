#Crie um programa que leia um numero inteiro
#introduzido pelo utilizador e que simule um
#radar de velocidade.

#>80km/h multado
#<=80 km/h não multado

#A multa são 100 euros + 7 euros por cada
#km/h acima.

#================================================

velocidade = int(input("Indique sua velocidade: "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = 100 + (excesso *7)
    print (f"Excesso de velocidade. \nO valor da multa é de {multa} euros. ")

elif velocidade <=80:
    print ("Você não está multado.")
