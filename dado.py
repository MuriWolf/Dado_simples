# 1. SIMULADOR DE DADO
# Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir)
# e permitir que o usuário rode o script quantas vezes quiser.

# Habilidades praticas a aplicar:

# Tratamento de exceções
# Condicionais If/Else
# Input de dados
# Geração de valores
# Print


from random import randint

while True:
    denovo = input("\nDeseja usar o dado?[s/n]:  ")
    if denovo == "s":
        pass
    elif denovo == "n":
        print("\nPrograma encerrado.")
        break
    while denovo != "n" and denovo != "s":
        print("\nDigite um valor valido.")
        denovo = str(input("Deseja usar o dado?[s/n]:  "))

    numero_dado = randint(1, 6)
    print("\nResultado do dado:")
    print(numero_dado)

