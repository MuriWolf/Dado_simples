# 1. SIMULADOR DE DADO
# Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir)
# e permitir que o usuário rode o script quantas vezes quiser.


from random import randint

while True:
    denovo = input("\nDeseja usar o dado?[s/n]:  ")

    # analisa sua resposta e decide oq fazer
    if denovo == "s":
        pass
    elif denovo == "n":
        print("\nPrograma encerrado.")
        break
    while denovo != "n" and denovo != "s":
        print("\nDigite um valor valido.")
        denovo = str(input("Deseja usar o dado?[s/n]:  "))

    # informacoes dos dados
    lados = int(input("\nDigite quantos lados o dado tem (normal- 6): "))
    qtdeDados = int(input("\nDigite quantas vezes deseja rodar esses dados: "))

    # print
    print("\nResultado dos dados\n")
    for i in range(qtdeDados):
        numero_dado = randint(1, lados)
    
        print(f"Dado {i+1}: {numero_dado}")

