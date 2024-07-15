'''Crie um programa que pergunte a quantidade de km percorridos por um
carro alugado e quantidade de dias que foi alugado.

Apresente o total a pagar sabendo que o carro custa 60€/dia e 0.456€/km.'''

#Pedir os dados
kmsPercorridos = float(input("Quantos km foram percorridos? "))
diasAlugado = float(input("Quantos dias ficou alugado? "))

#Fazer o cálculo
aluguel = 60
kmsCobrados = 0.456

custo = diasAlugado * aluguel
Kms = kmsPercorridos * kmsCobrados

valorTotal = (60 * diasAlugado) + (0.456 * kmsPercorridos)

#Apresentar o resultado
print(f"O total de kms percorridos foram de {Kms} kms.\nE o montante total a ser pago é de {valorTotal}€.")