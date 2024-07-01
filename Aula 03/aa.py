
#Calculando IF com AND
nota = int(input("Insira sua nota final: "))
faltas = int(input("Insira quantas faltas você teve: " ))

if nota>5 and faltas <4:
    print ("Parabéns, você foi aprovado!")

else:
    print ("Você foi reprovado.")