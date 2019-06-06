import sys
import math

def ler_matriz_adjacencia(arquivo):
    return [[int(x) for x in arquivo[i].split()] for i in range(len(arquivo))]

def ler_matriz_pontos(arquivo):
    pontos = [tuple(map(float, arquivo[i].split()[1:])) for i in range(len(arquivo))]
    matriz = [[0 for i in range(len(arquivo))] for j in range(len(arquivo))] 

    counti = 0
    countj = 0

    for i in range(0, len(pontos), 1):
        counti += 1

        for j in range(i, len(pontos), 1):
            Xi, Yi = pontos[i]
            Xj, Yj = pontos[j]

            v = math.sqrt(((Xi - Xj) ** 2) + ((Yi - Yj) ** 2))

            if abs(v - int(v)) > 0.5:
                v = math.ceil(v)
            else:
                v = math.floor(v)

            matriz[i][j] = v
            matriz[j][i] = v

            countj += 1

    return matriz

def ler_matriz(arquivo):
    # obtemos a forma de armazenamento dos dados (se é matriz de adjacência ou pontos)
    tipo_dados = arquivo[2]

    # removemos as 3 primeiras linhas pois não vamos utilizar mais para a leitura
    del arquivo[0:3]

    if tipo_dados == "EDGE_WEIGHT_SECTION":
        # realiza a leitura da matriz de adjacência
        return ler_matriz_adjacencia(arquivo)
    else:
        # removemos o EOF, pois não é necessário em Python
        del arquivo[-1]

        # realiza a leitura dos pontos para uma matriz de adjacências
        return ler_matriz_pontos(arquivo)

def ler_instancia(tipo_instancia, nome_arquivo):
    if tipo_instancia == "teste":
        caminho_arquivo = "./instancias/instancias_teste/" + nome_arquivo
    else:
        caminho_arquivo = "./instancias/instancias_tsp_cup/" + nome_arquivo
        
    with open(caminho_arquivo, "r") as arquivo:
        return ler_matriz([linha.strip() for linha in arquivo])