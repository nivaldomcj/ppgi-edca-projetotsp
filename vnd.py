import heuristicas

def vnd(matriz, rota):
    # número de heurísticas
    r = 2

    # tipo de heurística atual
    k = 1

    while (k <= r):
        if k == 1:
            nova_rota = heuristicas.two_opt(matriz, rota)
        elif k == 2:
            nova_rota = heuristicas.reinsertion(matriz, rota)
        
        custo_nova_rota = heuristicas.obter_custo(matriz, nova_rota)
        custo_rota_inicial = heuristicas.obter_custo(matriz, rota)

        if (custo_nova_rota < custo_rota_inicial):
            rota = nova_rota
            k = 1
        else:
            k = k + 1

    return rota
