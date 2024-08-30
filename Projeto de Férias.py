'''O projeto consiste em criar um sistema de lista de tarefas onde o utilizador pode
adicionar tarefas, definir prioridades, marcar tarefas como concluídas,
remover tarefas concluídas, e  exibir todas as tarefas pendentes
com as suas respectivas prioridades.

Funcionalidades:

Menu Principal com as opções:
- Adicionar Tarefa
- Mostrar Tarefas
- Marcar Tarefa como Concluída
- Remover Tarefas Concluídas
- Sair

Adicionar Tarefa: O utilizador pode adicionar uma tarefa fornecendo a descrição e a prioridade
(por exemplo, Alta, Média, Baixa).

Essas informações são armazenadas numa lista de dicionários.

Mostrar Tarefas:
Exibir uma lista de todas as tarefas pendentes, mostrando a descrição e a prioridade.
As tarefas podem ser exibidas por ordem de prioridade ou de registo.

Marcar Tarefa como Concluída:Permitir ao utilizador marcar uma tarefa como concluída,
removendo-a da lista de pendentes ou movendo-a para uma lista de tarefas concluídas.

Remover Tarefas Concluídas:Remover todas as tarefas que foram marcadas como concluídas da lista.

Sair:Encerrar o programa.

Requisitos Técnicos:Uso de Listas: A lista deve ser usada para armazenar todas as tarefas.
Uso de Dicionários: Cada tarefa deve ser representada
por um dicionário com as chaves descrição, prioridade e concluída.

Dicas:Comecem pelo menu principal e por implementar as funcionalidades básicas.
Pensem em como usar um dicionário para representar cada tarefa e como armazenar isso numa lista.
Ao marcar uma tarefa como concluída, considerem mudar o valor de uma chave concluída para True.
Implementem a funcionalidade de remover tarefas concluídas de maneira que
ela só apague as que estão marcadas como concluídas.

Desafio Adicional (Opcional):
- Adicionar uma funcionalidade para editar a descrição ou a prioridade de uma tarefa.
- Permitir ao utilizador ordenar as tarefas por prioridade ou data de registo antes de exibir.'''

from time import sleep

tarefas = []

while True:
    print("\n--- Menu Principal--- \n")
    print("[ 1 ] Adicionar Tarefa")
    print("[ 2 ] Mostrar Tarefas")
    print("[ 3 ] Marcar Tarefa como Concluída")
    print("[ 4 ] Remover Tarefas Concluídas")
    print("[ 5 ] Sair\n")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Adicione uma tarefa: ")
        print()
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
        tarefas.append({"tarefa": tarefa, "prioridade": prioridade, "concluida": False})
        sleep (1)
        print("...")
        sleep (1)
        print("Tarefa adicionada com sucesso!")

    elif escolha == "2":
        if tarefas:
            print("\nTarefas Pendentes:")
            contador = 1
            for tarefa in tarefas:
                if not tarefa["concluida"]:
                    print(f"{contador}. {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']}")
                    contador += 1

        else:
            print("Não há tarefas pendentes.")
            continue


    elif escolha == "3":
        if tarefas:
            print("\nTarefas Pendentes:")
            contador = 1
            tarefas_pendentes = []

            for tarefa in tarefas:
                if not tarefa["concluida"]:
                    print(f"{contador}. {tarefa['tarefa']} - Prioridade: {tarefa['prioridade']}")
                    tarefas_pendentes.append(tarefa)
                    contador += 1

            tarefa_concluida = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1

            if 0 <= tarefa_concluida < len(tarefas) and not tarefas[tarefa_concluida]["concluida"]:
                tarefas[tarefa_concluida]["concluida"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número inválido ou tarefa já concluída.")
        else:
            print("Não há tarefas para marcar como concluídas.")

    elif escolha == "4":
        tarefas = [tarefa for tarefa in tarefas if not tarefa["concluida"]]
        print("Tarefas concluídas removidas com sucesso!")

    elif escolha == "5":
        print("A fechar o programa.")
        sleep (1)
        print("...")
        sleep(1)
        print("Adeus!")
        break

    else:
        print("Opção inválida. Tente novamente.")
