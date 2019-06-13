import heuristicas
import vnd

import random

def shake(matriz, rota, custo):
    # inicializamos o valor da nova rota e do novo custo
    nova_rota = rota[:]
    novo_custo = custo

    for i in range(5):
        # obtêm os valores de i e j aleatoriamente, valores únicos
        # (i, j) tem que começar de 1 (excluindo a origem) até o fim da rota
        i, j = random.sample(range(1, len(rota) - 1), k=2)

        # vértice i está no final da rota?
        if i == (len(rota) - 1):
            ai, si = i-1, 0         # índice do vértice antecessor e sucessor de i (origem)
            aj, sj = j-1, j+1       # índice do vértice antecessor e sucessor de j
        # vértice j está no final da rota?
        elif j == (len(rota) - 1):
            ai, si = i-1, i+1       # índice do vértice antecessor e sucessor de i 
            aj, sj = j-1, 0         # índice do vértice antecessor e sucessor de j
        # vértice i e j estão no meio da rota
        else:
            ai, si = i-1, i+1       # índice do vértice antecessor e sucessor de i
            aj, sj = j-1, j+1       # índice do vértice antecessor e sucessor de j

        # obtêm os valores que serão cortados
        corte1 = matriz[nova_rota[aj]][nova_rota[j]]     # j com antecessor
        corte2 = matriz[nova_rota[j]][nova_rota[sj]]     # j com sucessor
        corte3 = matriz[nova_rota[ai]][nova_rota[i]]     # i com antecessor
        corte4 = matriz[nova_rota[i]][nova_rota[si]]     # i com sucessor 

        # realiza a troca de posições
        nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]

        # obtêm os novos valores de ligação
        ligacao1 = matriz[nova_rota[aj]][nova_rota[j]]     # j com antecessor
        ligacao2 = matriz[nova_rota[j]][nova_rota[sj]]     # j com sucessor
        ligacao3 = matriz[nova_rota[ai]][nova_rota[i]]     # i com antecessor
        ligacao4 = matriz[nova_rota[i]][nova_rota[si]]     # i com sucessor (origem)

        # realiza o cálculo do novo custo
        novo_custo -= (corte1 + corte2 + corte3 + corte4)           # cortes
        novo_custo += (ligacao1 + ligacao2 + ligacao3 + ligacao4)   # ligacoes

    return nova_rota, novo_custo

def vns(matriz, rota, custo, max_iteracoes):
    # inicialização da rota global com a rota de entrada
    # no momento a rota de entrada é a melhor global
    melhor_rota_global = rota[:]
    melhor_custo_global = custo

    # inicializa o número de iterações atual
    i = 0

    # condição de parada (número de iterações)
    while (i < max_iteracoes):
        # inicializa o número de shakes atual
        k = 1

        # inicializa o número máximo de shakes
        max_shakes = 2

        # enquanto não realizar o número de shakes máximo
        while (k <= max_shakes):
            # realiza a perturbação (shake)
            rota1, custo1 = shake(matriz, melhor_rota_global, melhor_custo_global)
                
            # realiza a busca local com a rota perturbada
            rota2, custo2 = vnd.vnd(matriz, rota1, custo1)
            
            # o custo encontrado pela perturbação é menor que o do VND?
            # salvamos a rota do VND como a melhor rota local
            if custo1 < custo2:
                melhor_rota_local = rota1              
                melhor_custo_local = custo1
            # o custo encontrado pelo VND é melhor que o da perturbação?
            # salvamos a rota da perturbação como a melhor rota local
            else:
                melhor_rota_local = rota2
                melhor_custo_local = custo2
            
            # o custo local é menor que o custo global?
            if melhor_custo_local < melhor_custo_global:
                melhor_rota_global = melhor_rota_local[:]       # salva essa rota como a melhor global
                melhor_custo_global = melhor_custo_local        # salva esse custo como o melhor global
                k = 1                                           # continua a fazer perturbações
            else:
                k = k + 1                                       # aumenta a quantidade de perturbações
  
        i = i + 1       # incrementa a quantidade de iterações

    return melhor_rota_global, melhor_custo_global