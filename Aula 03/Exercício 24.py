#Crie um programa que leia um número
#inteiro introduzido pelo utilizador e
#que simule um radar de velocidade.

#>80km/h multado
#<=80km/h não multado

#A multa são 100€ + 7€ por cada km/h acima

# Solicitar o número inteiro (velocidade) do utilizador
velocidade = int(input("Introduza a velocidade do veículo em km/h: "))

# Verificar se a velocidade é maior que 80 km/h
if velocidade > 80:
    # Calcular a multa
    excesso = velocidade - 80
    multa = 100 + (7 * excesso)
    print(f"Multado! O valor da multa é de {multa}€.")
else:
    # Caso a velocidade esteja dentro do limite
    print("Não multado.")