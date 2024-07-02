

print ("Seja bem-vindo!")

username = input("Insira seu nome: ")
email = input("Insira seu email: ")
password = input("Insira uma password: ")

print ("O registro está completo. ")

print("[1] - Login")
print("[2] - Sair")

opcao = int(input("----> "))

if opcao == 1:
    login = input("Digite seu login: ")
    password_login = int(input("Digite seu password: "))
    if login == username and password_login == password:
        print(username)

    if opcao == 1:
        print ("Login correto")
        print(f"Seja bem-vindo, {username}.")

    else:
        print ("Login errado")

elif opcao == 2:
    password_login = int(input("Digite seu password: "))
    if password_login == password:
        print ("Continue")

    login = input("Digite seu login: ")
    if login == username:
        print (username)
        print ("Continue")





