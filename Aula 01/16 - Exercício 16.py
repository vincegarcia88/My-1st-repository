'''Cria um programa que leia 5 notas introduzidas pelo utilizador
e que calcule a média aritmética entre eles.'''

#Pedir as 5 notas
nota1 = float(input("Escreva a sua primeira nota: "))
nota2 = float(input("Ok. Agora a segunda nota: "))
nota3 = float(input("Agora a sua terceira nota: "))
nota4 = float(input("Sua quarta nota: "))
nota5 = float(input("E, finalmente, sua quinta nota: "))

#Calcular as 5 notas pela média
media = (nota1 + nota2 + nota3 + nota4+ nota5) / 5

#Aqui ainda não estamos estudando if e elif
#porém eu quis adicionar para aumentar a dificuldade do exercício

print("A sua média final é", media)
if media <5:
    print("Você foi reprovado.\nTente ano que vem!")

elif media >5:
    print("Você foi aprovado.\nBoas férias!")