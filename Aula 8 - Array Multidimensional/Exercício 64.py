'''Um programa que guarde nome e media de um aluno
guardando também a situação em um dicionário.

No final mostre o conteúdo da estrutura na tela:'''

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

aluno = {"Nome": "Carlos", "Media": media}

print (f"O aluno {aluno['Nome']} ficou com média {aluno['Media']}")

if media <9.5:
    print (f"O Aluno {aluno['Nome']} está reprovado pela media {aluno['Media']}")

if media>=9.5:
    print(f"O aluno {aluno['Nome']} está aprovado devido a media de {aluno['Media']}")





