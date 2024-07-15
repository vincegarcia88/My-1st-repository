'''Crie o seguinte menu:

--- Calculadora ---
[ 1 ] – Tabuada
[ 2 ] – Calculadora
[ 3 ] – Números Pares
[ 4 ] – Sair

Mediante a opção solicitada o sistema deve executar a ação do menu.'''

print("=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-Calculadora-=-=-=-=")
print("=-=-=-=-=-=-=-=-=-=-=-=-=\n")

print("Menu")
print("")
print("[1] - Tabuada")
print("[2] - Calculadora")
print("[3] - Números Pares")
print("[4] - Sair")
print("")

opcao = int(input("Insira o número de sua escolha: "))


print("")

if opcao == 1:
    numTabuada = int(input("Tabuada. Insira seu número -> "))
    for c in range (0,11):
        resultadoTabuada = numTabuada * c
        print(f"{numTabuada} x {c} = {resultadoTabuada}")

if opcao == 2:
    print("Soma - [+]")
    print("Subtração - [-]")
    print("Multiplicação - [x]")
    print("Divisão - [/]\n")


    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    calc = input("Escolha seu cálculo: ")

    if calc == "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    elif calc == "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    elif calc == "x":
        resultado = num1 * num2
        print(f"{num1} x {num2} = {resultado}")

    elif calc == "/":
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")

    else:
        print("Escolha inválida!\nTente novamente!")


if opcao == 3:
    opcaoPares = int(input("Números pares. Veja se o número é par -> "))
    if opcaoPares % 2 == 0:
        print(f"O número {opcaoPares} é PAR.")
    else:
        print(f"O número {opcaoPares} é IMPAR.")
if opcao == 4:
    print("Sair do sistema.")


