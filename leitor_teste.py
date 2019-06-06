def ler_instancia(nome_arquivo):
    matriz = []

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            matriz.append([int(valor) for valor in linha.split()])

    return matriz

