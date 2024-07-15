'''Crie um programa que leia 5 notas de um aluno e calcule a sua média.

#>=9.5 passou
#>8 e < 9.5 em recuperação
#<8 reprova'''

#Insira as notas
nota1 = float(input("Insira sua 1a nota: "))
nota2 = float(input("Insira sua 2a nota: "))
nota3 = float(input("Insira sua 3a nota: "))
nota4 = float(input("Insira sua 4a nota: "))
nota5 = float(input("Insira sua 5a nota: "))

#Fazer o cálculo
media = (nota1+nota2+nota3+nota4+nota5)/ 5
print (media)

#Apresentar os resultados
if media >=9.5:
    print("Aprovado!")

elif media >8 and media <9.5:
    print("Em recuperação!")

else:
    print("Reprovado!")