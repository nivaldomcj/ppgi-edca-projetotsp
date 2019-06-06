def vizinho_proximo(matriz_distancias, numero_cidades, origem):
    # todas as cidades visitadas pelo algoritmo, na ordem de visitação (rota)
    cidades_visitadas = []

    # próxima cidade que deverá ser visitada, partindo da origem
    proxima_cidade = origem

    # enquanto não visitar todas as cidades (assumindo que a matriz é simétrica)
    # assume-se que as cidades visitadas ao final terá o mesmo número de cidades (total)
    while len(cidades_visitadas) < numero_cidades:
        # marcamos a próxima cidade como visitada
        cidades_visitadas.append(proxima_cidade)

        # variáveis onde terá a cidade com o menor custo encontrada (não inicializado)
        menor_custo_encontrado = -1
        menor_cidade_encontrada = -1
        
        # percorre todas as cidades no total de cidades
        # aqui assume-se que a matriz é simétrica
        for cidade_vizinha in range(numero_cidades):
            # ignora se essa cidade vizinha já foi visitada
            if cidade_vizinha in cidades_visitadas:
                continue
            
            # ignora se essa é a mesma cidade
            if cidade_vizinha == proxima_cidade:
                continue

            # obtêm o custo para ir da cidade atual para a próxima cidade vizinha
            custo_atual = matriz_distancias[proxima_cidade][cidade_vizinha]
            
            # guarda o menor custo/cidade SE a cidade encontrada é o menor custo encontrado no momento
            if (matriz_distancias[proxima_cidade][cidade_vizinha] < menor_custo_encontrado) or (menor_custo_encontrado == -1):
                menor_custo_encontrado = custo_atual
                menor_cidade_encontrada = cidade_vizinha

        # adiciona à rota essa cidade de menor custo, SE foi encontrada alguma
        if menor_cidade_encontrada != -1:
            proxima_cidade = menor_cidade_encontrada

    # retorna a rota (cidades visitadas)
    return cidades_visitadas