#Desenvolva um programa que faça 3 perguntas ao utilizador
#e apenas aceite como resposta "V" ou "F". Caso esteja
#errado, peça para repetir a resposta até ter um valor correto.

perguntas = ["O céu é azul? (V/F): ", "Ronaldo já foi melhor do mundo? (V/F): ", "1 + 1 é 3? (V/F): "]

respostas_corretas = ["V", "V", "F"]

i = 0
#Enquanto i for menor que 3, que é o número de perguntas, ele vai repetir.
while i < 3:
    while True:
        resposta = input(perguntas[i]).strip().upper()
        if resposta in ["V", "F"]:
            break
        else:
            print("Resposta inválida. Por favor, responda com 'V' ou 'F'.")

    if resposta == respostas_corretas[i]:
        print("Resposta correta!")
    else:
        print("Resposta incorreta.")

    i += 1      #i += 1  # Incrementa o índice i em 1 para passar para a próxima pergunta
