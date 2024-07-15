'''Cria um programa que leia 2 valores introduzidos pelo utilizador
e que apresente sua SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO e RESTO.'''

#Pedir os valores
num1 = int(input ("Introduza um número: "))
num2 = int (input ("Introduza outro número: "))

#Criar o cálculo
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

#Apresentar o resultado
print("A soma dos valores é",soma,"." "\nA subtração é",subtracao,".\nA multiplicação é",multiplicacao,
".\nJá a divisão dos valores é", divisao,"\nE,finalmente ,o resto é" ,resto,".")