import math

def menor_vizinhanca(matriz, numero_vertices, origem):
    # conjunto de vértices ainda não visitados pela heurística
    # inicializamos com um conjunto de 0 até N (número de vértices)
    nao_visitados = {i for i in range(numero_vertices)}
    
    # o vértice atual que deve ser visitado
    # inicialmente visitamos a origem
    vertice_atual = origem

    # caminho encontrado pela heurística
    caminho_encontrado = []

    # custo total desse caminho
    custo_caminho = 0

    # enquanto tiver vértices não visitados, faça:
    while len(nao_visitados) > 0:
        # adicionamos o vértice atual ao caminho (estamos visitando-o agora)
        caminho_encontrado.append(vertice_atual) 

        # removemos esse vértice do conjunto de vértices não visitados
        nao_visitados.remove(vertice_atual)

        # armazenamos qual é o índice e valor do vértice de menor caminho
        # saindo do vertice que estamos para o próximo vértice
        # como não o encontramos ainda, inicializamos com valor infinito
        menor_vertice_encontrado = math.inf
        menor_custo_encontrado = math.inf
        
        # para cada vértice não visitado ainda, procure o vértice que,
        # saindo do que estamos até ele (atual -> vizinho), tenha a menor distância
        for vertice_vizinho in nao_visitados:
            # obtemos o custo de ir do vértice atual até esse vértice não visitado
            custo_atual = matriz[vertice_atual][vertice_vizinho]

            # esse custo é o menor que encontramos até então? (ir de atual -> vizinho)
            if custo_atual < menor_custo_encontrado:
                menor_vertice_encontrado = vertice_vizinho
                menor_custo_encontrado = custo_atual

        # encontramos um vizinho próximo a esse vértice atual
        # que seja o menor custo dentre os vértices não visitados?
        if menor_custo_encontrado != math.inf:
            # marcamos esse vizinho como o próximo vértice a ser visitado
            vertice_atual = menor_vertice_encontrado

            # adicionamos o custo que foi de ir do vértice atual ao vizinho
            # ao custo total dessa rota gulosa sendo criada
            custo_caminho += menor_custo_encontrado

    # adicionamos ao custo total o custo de ir 
    # do último vértice do caminho até a origem
    custo_caminho += matriz[caminho_encontrado[-1]][origem]

    # retornamos o caminho encontrado E o custo total dele
    return caminho_encontrado, custo_caminho


def two_opt(matriz, rota_inicial, custo_rota_inicial):
    # mantém o custo da rota encontrada até o momento
    # no início, o melhor custo é o custo da rota inicial
    custo_melhor_rota = custo_rota_inicial

    # índice de I e J ideais para fazer o corte e rotação dos vértices
    # não há valores de início pois eles serão preenchidos abaixo
    indice_i_ideal = None
    indice_j_ideal = None

    for i in range(1, len(rota_inicial) - 2):
        for j in range(i + 1, len(rota_inicial) - 1):
            # ignoramos possíveis trocas não significativas
            if j - i == 1:
                continue

            # obtêm os custos da rota anterior e da nova rota
            # primeiro faz o cálculo do custo com o corte de duas arestas (i-1 > i, j > j+1)
            # depois adiciona ao custo da nova rota o custo da adição das duas arestas (i-1 > j) e (i à j+1)
            # assumimos aqui que a matriz de distâncias é simétrica (distância de i à j é igual de j à i)]
            custo_nova_rota = custo_rota_inicial - matriz[rota_inicial[i-1]][rota_inicial[i]] - matriz[rota_inicial[j]][rota_inicial[j+1]]
            custo_nova_rota = custo_nova_rota + matriz[rota_inicial[i-1]][rota_inicial[j]] + matriz[rota_inicial[i]][rota_inicial[j+1]]

            # ficamos com a nova rota se ela tiver um custo menor que a melhor rota
            # marcamos também que a rota foi melhorada e há possibilidade de melhorar mais
            if custo_nova_rota < custo_melhor_rota:
                custo_melhor_rota = custo_nova_rota
                indice_i_ideal = i
                indice_j_ideal = j   

    # o algoritmo não conseguiu encontrar um corte ideal?
    # então não melhorou, retorne a rota que foi recebida
    if (indice_i_ideal is None):
        return (rota_inicial, custo_rota_inicial)
        
    # encontramos então uma rota que tem um custo menor?
    # cria a nova rota, inicialmente vazia
    nova_rota = []

    # adiciona a rota atual de 0 até o i - 1 à nova rota
    nova_rota.extend(rota_inicial[0:indice_i_ideal])

    # adiciona a rota de i até k em ordem reversa à nova rota
    nova_rota.extend(reversed(rota_inicial[indice_i_ideal:indice_j_ideal+1]))

    # adiciona a rota de k até n (tamanho da rota) à nova rota
    nova_rota.extend(rota_inicial[indice_j_ideal+1:])

    # retornamos a nova rota e o custo menor
    return nova_rota, custo_melhor_rota


def swap(matriz, rota, custo):
    # no início, a melhor rota e o melhor custo são os atuais
    melhor_rota = rota[:]
    melhor_custo = custo

    # inicializamos o vetor de nova rota
    # esse vetor que será modificado para checar se a rota está ok
    atual_rota = rota[:]

    for i in range(1, len(rota), 1):
        for j in range(1, len(rota), 1):
            # não faz sentido fazer uma troca de dois índices iguais
            if i == j:
                continue
            
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
            corte1 = matriz[atual_rota[aj]][atual_rota[j]]     # j com antecessor
            corte2 = matriz[atual_rota[j]][atual_rota[sj]]     # j com sucessor
            corte3 = matriz[atual_rota[ai]][atual_rota[i]]     # i com antecessor
            corte4 = matriz[atual_rota[i]][atual_rota[si]]     # i com sucessor 

            # realiza a troca de posições
            atual_rota[i], atual_rota[j] = atual_rota[j], atual_rota[i]

            # obtêm os novos valores de ligação
            ligacao1 = matriz[atual_rota[aj]][atual_rota[j]]     # j com antecessor
            ligacao2 = matriz[atual_rota[j]][atual_rota[sj]]     # j com sucessor
            ligacao3 = matriz[atual_rota[ai]][atual_rota[i]]     # i com antecessor
            ligacao4 = matriz[atual_rota[i]][atual_rota[si]]     # i com sucessor (origem)

            # inicializa o atual custo com o custo inicial
            atual_custo = custo

            # realiza o cálculo do novo custo
            atual_custo -= (corte1 + corte2 + corte3 + corte4)           # cortes
            atual_custo += (ligacao1 + ligacao2 + ligacao3 + ligacao4)   # ligacoes

            # o custo atual é menor que o melhor custo atual?
            if atual_custo < melhor_custo:
                # salva essa rota como a menor e também o seu custo
                melhor_rota = atual_rota[:]
                melhor_custo = atual_custo
            
            # desfaça a alteração feita, evitando criar uma nova cópia de vetor
            # para a próxima iteração do laço
            atual_rota[i], atual_rota[j] = atual_rota[j], atual_rota[i]
    
    return melhor_rota, melhor_custo
