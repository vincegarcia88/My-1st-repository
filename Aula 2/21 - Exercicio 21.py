'''Crie um programa que leia uma frase e mostre:

✓ Quantas vezes aparece a letra “A”;
✓ Em que posição aparece a primeira vez;
✓ Em que posição aparece a última vez.'''

name = input ("Escreva seu nome: ").lower().strip()

#Quantas vezes aparece a letra A
print("Quantidade de vezes que aparece a letra A: ", end="")
print(name.count("a"))

#Em que posição aparece a primeira vez
print("Posição que aparece a letra A pela 1a vez: ", end="")
print (name.find("a"))

#Em que posição aparece a última vez
print("Posição que aparece a letra A pela 2a vez: ", end="")
print(name.find("a", 2))
print("")

print("Obrigado e volte sempre!")