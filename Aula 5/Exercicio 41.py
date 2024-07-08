#Desenvolva um programa que faça 3 perguntas ao utilizador
#e apenas aceite como resposta "V" ou "F". Caso esteja
#errado, peça para repetir a resposta até ter um valor correto.

p1 = input("Qual a cor do céu? ").strip().lower()
p2 = input ("Qual a estrela da seleção de Portugal? ").strip().lower()
p3 = int(input("Quanto é 1 + 1? "))

while True
    if p1 == "Azul":
        print (f"A resposta {p1} está correta.")
    else:
        print (f"Resposta errada!")

        if p2 == "Ronaldo":
            print (f"A resposta {p2} está correta.")

        else:
            print (f"Resposta errada!")

        if p3 == 2:
        print (f"A resposta {p3} está correta.")
        else:
        print (f"Resposta errada.")

        break

else:
    print ("A resposta está errada.")

