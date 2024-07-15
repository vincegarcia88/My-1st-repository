'''Crie um programa que leia o primeiro e último nome
de uma pessoa e exiba as mensagens:

1. “Olá nome, o seu registo está completo.”
2. “O seu email é nome@empresa.pt”

Ex email:
Alfredo Xavier
a.xavier.edu@empresa.pt'''

#Intro
print("")

print("=-=-=-=-=-=-=-=-==-=-=-=-=")
print("=-=-=-= REGISTRO =-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print("")

#Insira os dados
nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")
print("")

#Apresentar os resultados
print(f"Olá, {nome}! Seu registro está completo.\nO seu email é {email}")
print("")
print("Os melhores cumprimentos!")



