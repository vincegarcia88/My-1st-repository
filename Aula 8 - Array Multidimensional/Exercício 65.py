'''Crie um programa que sorteie a ordem de jogada num jogo ao
atirar um dado no ar. Cada jogador terá um número aleatório
associado dentro de um dicionário. No final ordene o ranking para ver a ordem de chegada.'''

from random import randint

jogo = {"Jogador1": randint(1,6),
      "Jogador2": randint(1,6),
      "Jogador3": randint(1,6),
      "Jogador4": randint(1,6)
      }

jogo_ordenado = list()

#Código para ordenar (Sorted) na ordem decrescente

for k,v in jogo.items():
      print(f"O {k} fez {v} pontos.")

jogo_ordenado = list(sorted(jogo.items(), key=lambda item: item[1], reverse= True))
print()
print (jogo_ordenado)
