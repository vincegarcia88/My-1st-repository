#Crie um programa que leia vários números inteiros e que
#termine

contadorNumeros = 0
somaNumeros = 0

#Condição de saída = ZERO
while numero != 0:
    numero = int(input("Digite um número: [ZERO para parar] "))
    if numero == 0:
        break
    contadorNumeros += 1
    somaNumeros += numero

print(f"Foram digitados {contadorNumeros} números.")
print(f"A soma dos números é {somaNumeros}.")
