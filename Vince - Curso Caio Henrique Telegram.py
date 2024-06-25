#Curso de Phyton (Para quem não tem tempo) - Caio Henrique Lemos Sampaio

#Aulas 1 a 2 (Instalação) - 01/03/2023

#-----------------------------------------------------------------------------------------

#Aulas 3 e 4 (Saída de dados e variáveis) 02/03/2023

#int = 8 | float = 8.6 | Bool = True|False | Str = "8"

#Código para saber o tipo de dado é:
#print (type (9)) Int
#print (type (9.7)) float
#print (type (true)) Bool
#print (type ("Oi")) Str

#Aqui aprendi o uso:
# Das chaves: Para denominar as variáveis nas frases
# Do Print: Para o escrito aparecer na tela
# Do Input: Para o usuário digitar
# \n :no final das frases para pular linha (Quebra de linha)
# \end :
#Exercício:

#nome = "Vince"
#idade = 34

#print( "Olá, {} ! Sua idade é {} anos.".format (nome, idade),end= " ")
#print ("Tudo bem com você?")
#música = input ("Qual seu estilo de música preferido? ")
#print ("Ah! Bacana! {} é muito bom!".format(música))
#vocalista = input ("E o seu vocalista preferido? ")
#guitarrista = input ("E na guitarra, quem vc curte? ")
#print ("Esses caras são muito bons! {} e {} são músicos de qualidade extraordinária".format(vocalista, guitarrista))

#filme = input ("Qual seu tipo de filme preferido? ")
#print ("Eu curto um pouco de {} também.".format(filme),end= "")
#print (" Mas prefiro os Sci-Fi.")

#----------------------------------------------------------------------------

#Aulas 5 e 6 - Entrada e Conversão de Dados (03/03/2023)

# Aqui aprendi a converter variáveis (De Str pra float por exemplo)
# No exercício abaixo calculei o tempo de casa de um funcionário,
# através do seu ano de entrada na empresa e o ano atual.
# Saber a idade da pessoa através do ano de nascimento.

#Exercício

#nome = input ("Digite o seu nome\n")
#ano_nascimento = input ("Digite seu ano de nascimento\n")
#idade = 2023 - int(ano_nascimento)
#print("Olá, {}. Sua idade é {}.".format(nome, idade))


#nome = input ("Olá, amigo. Qual o seu nome?\n")
#ano_de_entrada = input ("Ano de Matricula\n")
#tempo_de_empresa = 2023 - int(ano_de_entrada)
#print("Olá, {}. Você tem {} anos de empresa. ".format(nome, tempo_de_empresa))


#Aula 7 (Operadores relacionais)

# and = - True | True - ou  - False | False - (Fora esses 2 é False)
# or =  - False | True (True) - ou  - True |False (True) - 2 falses = (False)
# not = Inverte a expressão à frente

#Exemplos:

#x = 5 == 6
#print (x)
#False

#x = 7 > 3
#print (x)
#true

#x = not 3 > 1
#print (x)

#--------------------------------------------------------------------------------
#Aula 8 (Operadores lógicos)
#and só é True se todos forem True ou todos False
#or só será True se 1 deles for True

#x = (5>6 or 3==2) and (5==3 or 2==3)
#x = False and False
#print (x)
#x = False

#-----------------------------------------------------------------------------

#Aulas 9 e 10 (Estruturas de Decisão)

#if = Se for true será executada
#else: = Se IF for False, será executada
#elif = Se IF for true e = será executada

#idade = int (input ("Digite sua idade: "))
#if idade >= 18:
#    print("Você já pode ser preso, haha!")
#else:
#    print ("Garoto novo no Metal ainda.")


#if idade>18:
#    print("Você tem mais de 18 anos")
#elif idade == 18:
#    print ("Você tem 18 anos")
#elif idade < 18:
#    print ("Você tem menos de 18 anos")

#else:
#    print ("Não conseguimos determinar")


#Meu Exemplo:

#time = str (input ("Qual é o seu time? "))
#if time ==  ("Botafogo"):
#    print("Torcedor do Glorioso Alvinegro Carioca. ")

#elif time == ("Vasco"):
#    print("Então tu é bacalhau! ")

#elif time == ("Fluminense"):
#    print("Tricolete, né mané! ")

#elif time == ("Flamengo"):
#   print("Torce pro mais mulambento. ")

#else:
#    print("Fora do Rio, ok. ")


#Exercício

#idade = int (input("Digite sua idade: "))
#carta = input("Digite sim, caso vc possua carta de motorista e não, caso não possua. ")

#if idade >= 18 and carta == "Sim":
#   print ("Você tem idade e está habilitado a dirigir. ")

#elif idade < 18 and carta == "Sim":
#    print ("Você não poderia ter carta na sua idade. ")

#elif idade <18 and carta == "Não":
#    print ("Aguarde os seus 18 anos para tirar uma carta. ")

#elif idade >=18 and carta == "Não":
#    print ("Você até tem idade, mas não tem carta para dirigir. ")

#------------------------------------------------------------------------------------


#Aula 11 (Exercícios e Operações)

#Exercício Nível 1 (Peça para o usuário digitar 2 números e em seguida dê
#a soma, a subtração, a multiplicação e divisão desses números.

#numero1 = float (input ("Escreva um número: "))
#numero2 = float (input ("Escreva outro número: "))
#soma = numero1 + numero2
#subtração = numero1 - numero2
#multiplicação = numero1 * numero2
#divisão = numero1 / numero2

#print ("A soma entre {} e {} é: {} ".format (numero1, numero2, soma))
#print ("A subtração entre {} e {} é: {} ".format (numero1, numero2, subtração))
#print ("A multiplicação entre {} e {} é: {} ".format (numero1, numero2, multiplicação))
#print ("A divisão entre {} e {} é: {} ".format (numero1, numero2, divisão))

# Exercicio 2 ---------------------------------------------------------------

#numero_1 = float (input ("Digite um número "))
#numero_2 = float (input ("Digite outro número "))

#soma = numero_1 + numero_2
#subtração = numero_1 - numero_2
#multiplicação = numero_1 * numero_2
#divisão = numero_1 / numero_2

#print ("A soma entre {} e {} é {}.".format(numero_1, numero_2, soma))
#print ("A subtração entre {} e {} é {}.".format(numero_1, numero_2, subtração))
#print ("A multiplicação entre {} e {} é {}.".format(numero_1, numero_2, multiplicação))
#print ("A divisão entre {} e {} é {}.".format (numero_1, numero_2, divisão))

#Exercício
#Pedir para o usuário 4 notas de uma prova e mostrar a média dessas notas.

#nota1 = float (input ("Escreva a nota da primeira prova. "))
#nota2 = float (input ("Escreva a nota da segunda prova. "))
#nota3 = float (input ("Escreva a nota da terceira prova. "))
#nota4 = float (input ("Escreva a nota da quarta prova. "))

#media = (nota1+nota2+nota3+nota4) /4

#print ("A média das provas é {}".format(media))

# Exercício (Continuação)
#Saber se o aluno foi aprovado ou reprovado
#A média é 6

#if media >=6:
#    print("Parabéns, você foi aprovado!")

#elif media <6:
#    print ("Desculpe, você foi reprovado! ")


#Exercício de mudança de temperatura
#Pedir para o usuário uma temperatura em Fahrenheit e transformá-la em Celsius
#C = 5 * ((F-32) / 9). (FÓRMULA FAHRENHEIT PRA CELSIUS)

#fahre = float (input ("Quantos graus tem hoje? "))
#c = 5 * (fahre - 32) / 9
#print ("Temperatura = {}".format(c))

#Outro exercício igual:

# c= 5 * ((Fahre-32) / 9

#fahre = float (input ("Temperatura: "))
#c = 5 * (fahre-32) / 9
#print ("A temperatura em celsius é {}. ".format(c))

#Fórmula (Celsius to Fahrenheit)
# 9 * c / 5 + 32

#c = float (input ("Temperatura: "))
#f = ((9 * c) / 5) + 32
#print ("{} graus fahrenheit. ".format(f))


# Exercício Mix criado por mim
# A pessoa escolhe 2 números, utilize IF e ELIF, desses números faça as 4 contas básicas
# depois calcule a média de todas elas, mantendo o bom humor. :)

#numero1 = float (input ("Escreva um número. "))
#numero2 = float (input ("Escreva outro número. "))

#print ("Você escolheu os números {} e {}. \n".format (numero1, numero2))
#resposta = (input ("Correto? "))

#if  resposta == "Sim":
#    print ("Então faremos as contas com eles. \n")
#    w = (input ("Partiu? "))

 #   n1 = numero1 + numero2
  #  n2 = numero1 * numero2
   # n3 = numero1 - numero2
 #   n4 = numero1 / numero2

 #   print ("Então, a soma entre esses números dá {}. ".format(n1))
  #  p = (input (" "))
  #  print ("A multiplicação dá {}. ".format(n2))
#    p1 = (input (""))
#    print ("A subtração dá {}. ".format (n3))
#    p2 = (input (""))
#    print ("E a divisão dá {}. ".format(n4))
#    p3 = (input ("Ok?\n"))

#    x = (input ("O pai é brabo, pode falar. Mas não pára por aí!\n "))

#    print ("Agora vamos calcular a média destes números.")
#    m = (input ("Vamos lá?\n"))

#    print (input ("Calcula aqui, calcula ali... chegamos ao valor!"))

#    media = ((n1 + n2 + n3 + n4) / 4)
#    print ("A média destes números é {}. ".format(media))
#    x33 = (input(""))
#    y = (input ("E ai, gostou da máquina? Haha!\n"))
#    x12 = (input ("O pai é sinistro! "))
#    print ("Forte abraço e até mais!")

#elif resposta == "Não":
#    print ("Então terminamos por aqui. Faça de novo.")

#--------------------------------------------------------------------

# Exercício
# Como saber se um número é par ou impar
#Numa divisão por 2: Número par, o resto é 0. Número ímpar, o resto é 1.

#n = int (input ("Choose a Number: "))

#if  n % 2: == O
#    print("Even")
#else:
#    print("Weird")

#---------------------------------------------------

# Exercício
# Como saber se o número escolhido é múltiplo de 3 ou não:

#n = int (input ("Digite um número: "))

#if not (n % 3):
#    print ("É múltiplo de 3. ")

#else:
#    print ("Não é múltiplo de 3. ")

# Explicação: Um número é múltiplo de 3, se o resto da divisão dele for 0.
# Então fazemos o teste: numero % 3
# Se o resultado for 0, o IF não é executado, pois dá falso. Por isso o IF NOT.
# Sempre que algo for TRUE o not transforma em FALSE e vice-versa.
# Assim, colocamos um NOT antes do (n %3) e quando for múltiplo de 3, a expressão NOT (n%3)
# vira TRUE e cai no IF dizendo que é múltiplo de 3.

#--------------------------------------------------------------------------------------------

# AULA 20 - Estruturas de repetição

#i = 1
#while i < 11:
#    print (i)
#    i = i + 1
#print ("Encerrou...")

#---------------------------------------
#n = int (input("Digite um número: "))
#for c in range (0, 7):
#    print (c)
#print ("Fim.")

#----------------------------------------

#i = int (input ("Início: "))
#f = int (input ("Fim: "))
#p = int (input ("Passo: "))
#for c in range (i, f+1, p):
#    print (c)
#print ("Fim")
#-----------------------------------------

# Contagem regressiva de 10 a 0:

#from time import sleep
#for count in range (10, -1, -1):
#    print (count)
#    sleep (0.5)
#print ("Feliz Ano novo! ")

#______________________________________________

#Todos os números pares de 1 até 50:

#for c in range (2,51, 2):
#    print (c)

# Explicação: 2 = Início | 51 = fim | 2 = de 2 em 2

#----------------------------------------------

# Programa que calcula a soma entre todos os numeros impares
# que são multiplos de 3 e que se encontram no intervalo de 1 a 500.

#soma = 0
#count = 0
#for c in range (1,501,2):
#    if c % 3 == 0:
#        count = count + 1
#        soma = soma + c
#print ("A soma dos {} valores é {}".format(count,soma))
#---------------------------------------------------------------

# Programa que calcula a soma entre todos os numeros pares
# e quantos se encontram no intervalo de 1 a 20.

#soma = 0
#count = 0
#for c in range (1, 20):         #Começa do 1 e vai até o 20
#    if c % 2 == 0:              #Pegamos c e dividimos por 2, os que dão 0 são pares
#        soma = soma + c         #Fazemos a soma final que será a soma de todos os pares até 18
#        count = count + 1       #Pegamos a cont final que será a cont inicial + 1
#print ("A soma final é {} e a count é {}.".format (soma, count))
#S---------------------------------


#n = int (input("Escreva um número: "))
#if n % 2 > 0 == 0:                              #Encontramos se o número é par
#    print ("{} é um número par.".format(n))
#elif n % 2 == 1:                                #Encontramos se é ímpar
#    print ("{} é um número ímpar.".format (n))
#else:
#    print ("Neutro.")                           #Se for zero é neutro

#-------------------------------------------------
#Como encontrar números pares:

#for c in range (1,51):
#    if c % 2 == 0:
#        print (c, end=" ")

#-------------------------------------------------
#Como encontrar os números ímpares:

#for c in range (1, 51):
#    if c % 2 == 1:
#        print (c, end=" ")
#-------------------------------------------------

#ENCONTRAR O MAIOR NÚMERO
#c = int (input("Digite um número: "))
#c2 = int (input ("Digite outro número: "))
#c3 = int (input ("Digite mais um número: "))

#if c > c2 and c > c3:
#    print (c)
#elif c2 > c and c2 > 3:
#    print (c2)
#else:
#    print (c3)

#----------------------------------------------------------------------------

#WHILE
#import time
#x = 90
#while x > 10:
#   time.sleep (1)      #Função para o processamento demorar 1 seg a cada número
#    print (x)          # #Aqui será impresso o número 90 eternamente
                        # 90 sempre será maior que 10 e o print está no laço.

#-------------------------------


#y = 0
#while y <= 72:      #Enquanto Y for < ou = a 72...
#    if y % 10 == 0: #... me mostre os mútiplos de 10, entre 0 e 72...
#        print (y)   #Pode imprimir...
#    y = y + 1       #A cada laço do while ele vai receber +1

#--------------------------------------
# Sara mora numa rua comprida que vai de número 1 até 1000
# O número da casa da Sara é divisível por 17
# E ela tem certeza que o numero da casa não termina com 0 nem com 6

#Como identificar o último algarismo de um numero:
# Usa o operador módulo com o divisor 10:
#100 % 10 = 10,0 (Sobra 0)
#101 % 10 = 10,1 (Sobra 1)
#106 % 10 = 10,6 (Sobra 6)

#n = 0
#while n < 1000:
#    n += 1
#    if n % 10 == 0 or n % 10 == 6:
#        continue
#    if n % 17 == 0:
#        print (n)

#--------------------------------

# Sara mora numa rua comprida que vai de número 1 até 1000
# O número da casa da Sara é divisível por 17
# E ela tem certeza que o numero da casa não termina com 0 nem com 6

#c = 0
#while c < 1000:
#    c+= 1
#    if c % 17 == 0:
#        print (c)
#        if c % 10 == 0 or c % 10 == 6:
#            continue
#print ("")


# -----------------------------------------





