from time import sleep

nomes = 'Ricardo', 'Karine', 'Jean', 'José', 'Rita'

# imprimir o conteúdo do tuple de forma dinâmica
for nome in nomes:
    print(nome)

# imprimir a posição e o conteúdo de cada tuple de forma dinâmica
for pos, nome in enumerate(nomes):
    print(f'Na posição {pos} está o nome {nome}')

print(sorted(nomes)) # imprime o tuple por ordem, mas não muda!

print(nomes)