from math import sqrt

def ler_descricao(caminho_instancias, nome_arquivo):
    descricoes = []

    with open("{}/{}".format(caminho_instancias, nome_arquivo), "r") as arquivo:
        # lê todas as linhas do arquivo MAS ignorando as 6 primeiras
        # as 6 primeiras linhas tem informações de como interpretar os arquivos
        linhas = arquivo.readlines()[6:]

        for linha in linhas:
            # removemos o marcador -) que existe pra indicar que é
            # uma informação de uma instância
            linha = linha.replace("-)", "")

            # dividimos o nome da instância de seu valor ótimo
            linha = linha.strip().split("=")

            # obtêm o nome da instância e o seu valor ótimo
            nome_instancia = linha[0].strip()
            solucao_otima = int(linha[1])

            # adicionamos a informação dessa instância na lista de instâncias 
            descricoes.append([nome_instancia, solucao_otima])
    
    return descricoes
            


def ler_instancia(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        # faz a leitura do nome da instância [ex: NAME bayg29]
        # ignoramos pois não é preciso do nome da instância (por isso o _)
        _ = next(arquivo)

        # obtêm a dimensão da matriz dessa instância [ex: DIMENSION 29]
        dimensao = int(next(arquivo).split(":")[1].strip())
        
        # obtêm o tipo dessa entrada [ex: EDGE_WEIGHT_SECTION]
        tipo = next(arquivo).strip()

        # inicializa a matriz com a dimensão lida, com zeros
        # assume-se que as instâncias são matrizes simétricas
        matriz = [[0 for _ in range(dimensao)] for _ in range(dimensao)]

        # é uma matriz de adjacência pronta?
        if tipo == "EDGE_WEIGHT_SECTION":
            for i in range(dimensao):
                # recupera a próxima linha de valores da matriz no arquivo
                linha = next(arquivo).split()

                for j in range(dimensao):
                    # preenche cada linha da matriz com os valores lidos
                    # lê o próximo [j] da linha do arquivo e muda o [j] da matriz
                    matriz[i][j] = int(linha[j])
        
        # é uma lista de pontos?
        if tipo == "DISPLAY_DATA_SECTION":
            # lista de pontos (distâncias)
            pontos = []

            for _ in range(dimensao):
                # recupera a próxima linha do arquivo
                linha = next(arquivo).split()

                # da linha, obtêm os valores de x e y
                x, y = float(linha[1]), float(linha[2])

                # adiciona esses pontos à lista de pontos
                pontos.append((x, y))
            
            for i in range(dimensao):
                # obtemos os pontos X, Y de i
                xi, yi = pontos[i]

                for j in range(i, dimensao):
                    # obtemos os pontos X, Y de j
                    xj, yj = pontos[j]

                    # realiza o cálculo da distância euclidiana de dois pontos
                    d = sqrt( ((xi-xj)**2) + ((yi-yj)**2) )

                    # arredonda o valor para o mais próximo inteiro
                    d = round(d)

                    # salva o valor da distância na matriz de adjacência
                    matriz[i][j] = d
                    matriz[j][i] = d

    # retorna a matriz e a dimensão da matriz lida
    return (matriz, dimensao)