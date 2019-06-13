import heuristicas

def vnd(matriz, rota_inicial, custo_rota_inicial):
    # por enquanto a melhor rota é a inicial
    melhor_rota = rota_inicial
    custo_melhor_rota = custo_rota_inicial

    # número de heurísticas
    r = 2

    # tipo de heurística atual
    k = 1
    
    while (k <= r):
        if k == 1:
            nova_rota, custo_nova_rota = heuristicas.two_opt(matriz, melhor_rota, custo_melhor_rota)
        elif k == 2:
            nova_rota, custo_nova_rota = heuristicas.swap(matriz, melhor_rota, custo_melhor_rota)
        
        # se a nova rota é melhor que a atual 
        if (custo_nova_rota < custo_melhor_rota):
            melhor_rota = nova_rota
            custo_melhor_rota = custo_nova_rota
            k = 1
        else:
            k = k + 1

    return melhor_rota, custo_melhor_rota