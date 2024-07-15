

username = input("Insira um username: ")
email = input("Insira o seu email: ")
password = int(input("Insira uma password: "))

print("O seu registo foi executado com sucesso.")
print("")
print("[1] - Login")
print("[2] - Sair")
print("")
opcao = int(input("----> "))
print("")

if opcao == 1:
    login = input("Digite o seu login: ")
    password_login = int(input("Digite a sua password: "))

if  login == username and password_login == password:
    print(username)
    print("Login correto.\n")
    print(f"Seja bem-vindo(a), {username}.")

else:
    print ("Login incorreto.")
    print("")
    print("Tente novamente!")
    print("")
    login = input("Digite o seu login: ")
    password_login = int(input("Digite a sua password: "))

if login == username and password_login == password:
        print(username)
        login = input("Digite o seu login: ")
        password_login = int(input("Digite a sua password: "))

else:
    print("Login incorreto.")
    print("")
    print("A sua conta encontra-se bloqueada e será terminada.")

if  opcao == 2:
    login = input("Digite o seu login: ")
    password_login = int(input("Digite a sua password: "))
    print ("Adeus! Até à próxima!")