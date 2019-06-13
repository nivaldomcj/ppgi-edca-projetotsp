def naive_show_matrix(matriz):
    # dimensão da matriz
    print("\nDIMENSION {} X {}".format(len(matriz), len(matriz[0])))

    # matriz
    for i in range(len(matriz)):
        print("[", end="")

        for j in range(len(matriz[i])):
            print("{:5}".format(matriz[i][j]), end="")

        print("]\n", end="")


def naive_get_cost(matriz, caminho):
    # inicializa o custo total da distância da rota
    custo_total = 0

    for i in range(0, len(caminho) - 1, 1):
        # realiza o somatório da distância para ir da cidade i até a i+1
        custo_total += matriz[caminho[i]][caminho[i + 1]]

    # adiciona ao custo total o custo de ir da última cidade até a origem
    # assumindo aqui que SEMPRE a origem é a primeira cidade (0)
    custo_total += matriz[caminho[-1]][0]
    return custo_total


def naive_matrix_query(matriz):
    while True:
        i, j = map(int, input("enter line index & column index: ").split())

        print("value: {}\n".format(matriz[i][j]))


def naive_shake(matriz, rota, custo):
    nova_rota = rota[:]

    # índice de onde um elemento vai sair e pra onde ele vai
    i = 6 #len
    j = 3

    # realiza a troca de elementos na lista
    nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]

    return nova_rota, naive_get_cost(matriz, nova_rota)


def naive_swap(matriz, rota, custo):
    melhor_rota = rota[:]
    melhor_custo = custo

    for i in range(1, len(rota), 1):
        for j in range(1, len(rota), 1):
            # não faz sentido fazer uma troca de dois índices iguais
            if i == j:
                continue

            # faz a troca da rota diversas vezes (naive)
            atual_rota = rota[:]
            atual_rota[i], atual_rota[j] = atual_rota[j], atual_rota[i]

            # faz o cálculo do custo (naive)
            atual_custo = naive_get_cost(matriz, atual_rota)

            if atual_custo < melhor_custo:
                melhor_custo = atual_custo
                melhor_rota = atual_rota
    
    return melhor_rota, melhor_custo