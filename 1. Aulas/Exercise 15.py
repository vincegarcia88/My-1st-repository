#Cria um programa que leia 2
#valores introduzidos pelo
#utilizador e que apresente a
#sua SOMA, SUBTRAÇÃO,
#MULTIPLICAÇÃO, DIVISÃO e RESTO.


num1 = int (input ("Insira um número: "))
num2 = int (input ("Insira outro número: "))

soma = num1 + num2
subtracao = num1-num2
multiplicacao = num1*num2
divisao = num1/num2
resto = num1%num2

print ("A soma dos números inseridos é", soma,".")
print ("A subtração é", subtracao,".")
print ("A multiplicação dos valores é", multiplicacao,".")
print ("A divisão é", divisao,".")
print ("O resto é de", resto,".")
