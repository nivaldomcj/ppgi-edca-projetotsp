import leitor
import heuristicas
import vnd

import time


def main():
    tempo_inicial = time.time()

    matriz = leitor.ler_instancia("tsp_cup", "tsp1.txt")
    dimensao = len(matriz[0])
    origem = 0

    print("terminei de ler a matriz")

    #caminho_menor_insercao = heuristicas.menor_insercao(matriz, origem, dimensao)
    caminho_menor_vizinhanca = heuristicas.menor_vizinhanca(matriz, origem, dimensao)
    #caminho_bellmore_nemhauser = heuristicas.bellmore_nemhauser(matriz, origem, dimensao)

    print("terminei de construir")
    
    #vnd_menor_insercao = vnd.vnd(matriz, caminho_menor_insercao)
    vnd_menor_vizinhanca = vnd.vnd(matriz, caminho_menor_vizinhanca)
    #vnd_bellmore_nemhauser = vnd.vnd(matriz, caminho_bellmore_nemhauser)

    print("terminei de rodar o vnd")

    #custo_vnd_menor_insercao = heuristicas.obter_custo(matriz, vnd_menor_insercao)
    custo_vnd_menor_vizinhanca = heuristicas.obter_custo(matriz, vnd_menor_vizinhanca)
    #custo_vnd_bellmore_nemhauser = heuristicas.obter_custo(matriz, vnd_bellmore_nemhauser)

    print("terminei de obter o custo")

    tempo_final = time.time()

    #print("Custo VND Menor Inserção: ", custo_vnd_menor_insercao)
    print("Custo VND Menor Vizinhança: ", custo_vnd_menor_vizinhanca)
    #print("Custo VND Bellmore Nemhauser: ", custo_vnd_bellmore_nemhauser)

    print("\nTempo decorrido (segundos): ", (tempo_final - tempo_inicial))


    

if __name__ == "__main__":
    main()