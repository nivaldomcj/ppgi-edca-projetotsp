#Recupera distância percorrida através do caminho:
def obter_custo(matriz, caminho):
    # inicializa o custo total da distância da rota
    custo_total = 0

    for i in range(0, len(caminho) - 1, 1):
        # realiza o somatório da distância para ir da cidade i até a i+1
        custo_total += matriz[caminho[i]][caminho[i + 1]]

    # adiciona ao custo total o custo de ir da última cidade até a origem
    # assumindo aqui que SEMPRE a origem é a primeira cidade (0)
    custo_total += matriz[caminho[-1]][0]
    return custo_total

# ---------------- Heurística do menor vizinho:
def menor_vizinhanca(matriz, vertice, numero_vertices):
    # inicializa o conjunto de vértices
    conjunto = {i for i in range(numero_vertices)}

    # caminho encontrado pelo algoritmo
    caminho = []
    
    # distância do caminho a ser encontrado pelo algoritmo 
    distancia_caminho = 0
    
    while len(conjunto) != 1:
        # retorna o menor elemento não nulo de uma lista de adjacência
        l = min([e for e in matriz[vertice] if e > 0])

        # obtêm o índice (vertice) desse menor elemento não nulo
        i = matriz[vertice].index(l)

        if i not in conjunto:
            matriz[vertice][i] = max(matriz[vertice])
        else:
            caminho.append(vertice)
            conjunto.remove(vertice)

            vertice = i
            distancia_caminho += l
    
        # quando na última iteração (apenas 1 último elemento no conjunto)
        # adiciona esse último elemento e faz a distância do último elemento com a origem (0)
        if len(conjunto) == 1:
            lista = list(conjunto)
            caminho.append(lista[0])
            distancia_caminho += matriz[lista[0]][0]
        
    return caminho

# ---------- Heurística de Bellmore and NemHauser:
def bellmore_nemhauser(matriz, vertice1, numero_vertices):
    # inicializa o conjunto de vértices
    conjunto = {i for i in range(numero_vertices)}

    print(conjunto)

    # caminho encontrado pelo algoritmo
    caminho=[]

    # adiciona a origem a lista com o caminho encontrado
    caminho.append(vertice1)

    # retorna o menor elemento não nulo da lista de adjacência
    l = min([e for e in matriz[vertice1] if e > 0])

    # obtêm o vértice mais próximo do vértice 1
    vertice2 = matriz[vertice1].index(l)

    # adicionamos o vértice mais próximo do 1 no caminho
    # e removemos a origem e esse vértice mais próximo do conjunto de vértices a ser visitado
    caminho.append(vertice2)
    conjunto.remove(vertice1)
    conjunto.remove(vertice2)

    #print(vertice1)
    #print(vertice2)

    while len(conjunto) != 0:
        # inicializa o valor como máximo da lista
        # precisamos do maior para conseguir comparar e achar o menor
        valor1 = max(matriz[vertice1])
        valor2 = max(matriz[vertice2])

        # procura nas duas extremidades a menor distância
        for i in conjunto:
            if matriz[vertice1][i] <= valor1:
                valor1 = matriz[vertice1][i]
        for i in conjunto:
            if matriz[vertice2][i] <= valor2:
                valor2 = matriz[vertice2][i]

        if valor1 <= valor2:
            # obtêm o vértice desse valor1
            ind1 = matriz[vertice1].index(valor1)

            # adiciona-o no início do caminho
            caminho.insert(0, ind1)

            # removemos ele do conjunto de vértices a serem visitados
            conjunto.remove(ind1)

            # definimos o vértice 1 como a nova extremidade
            vertice1 = ind1
        else:
            # obtêm o vértice desse valor2
            ind2 = matriz[vertice2].index(valor2)

            # adiciona-o no fim do caminho
            caminho.append(ind2)

            # removemos ele do conjunto de vértices a serem visitados
            conjunto.remove(ind2)

            # definimos o vértice 2 como a nova extremidade
            vertice2 = ind2

    return caminho

# Heuristica de Menor Inserção:
def menor_insercao(matriz, vertice1, numero_vertices):
    # inicializa o conjunto de vértices
    conjunto = {i for i in range(numero_vertices)}

    # caminho encontrado pelo algoritmo
    caminho = []

    # definindo os três primeiros vertices da rota
    caminho.append(vertice1)

    # retorna o menor elemento não nulo da lista de adjacência
    l = min([e for e in matriz[vertice1] if e > 0])

    # obtêm o vértice mais próximo do vértice 1
    vertice2 = matriz[vertice1].index(l)

    # adicionamos o vértice mais próximo do 1 no caminho
    # e removemos a origem e esse vértice mais próximo do conjunto de vértices a ser visitado
    caminho.append(vertice2)
    conjunto.remove(vertice1)
    conjunto.remove(vertice2)

    # inicializa o valor como máximo da lista
    # precisamos do maior para conseguir comparar e achar o menor
    valor1 = max(matriz[vertice1])
    valor2 = max(matriz[vertice2])

    # procura nas duas extremidades a menor distância
    for i in conjunto:
        if matriz[vertice1][i] <= valor1:
            valor1 = matriz[vertice1][i]
    for i in conjunto:
        if matriz[vertice2][i] <= valor2:
            valor2 = matriz[vertice2][i]
    
    if valor1 <= valor2:
        # obtêm o vértice desse valor1
        ind1 = matriz[vertice1].index(valor1)

        # adiciona-o no início do caminho
        caminho.insert(0, ind1)

        # removemos ele do conjunto de vértices a serem visitados
        conjunto.remove(ind1)
    
        # definimos o terceiro vértice a ser visitado
        vertice3 = ind1
    else:
        # obtêm o vértice desse valor2
        ind2 = matriz[vertice2].index(valor2)

        # adiciona-o no fim do caminho
        caminho.append(ind2)

        # removemos ele do conjunto de vértices a serem visitados
        conjunto.remove(ind2)
        
        # definimos o terceiro vértice a ser visitado
        vertice3 = ind2

    # adicionamos o vértice 3 ao caminho
    caminho.append(vertice3)
        
    # percorrendo cada elemento remanescente de "conjunto" (vertices restantes do grafo)
    # para detectar o ponto de inserçao mínima
    for vertice in conjunto: 
        # cada elemento do conjunto é inserido na aresta que gere o menor custo
        custo = float("inf")

        for j in range(0, len(caminho)):
            # caso estamos no final do caminho, devemos adicionar
            # o custo para fechar o ciclo (final -> começo)
            if j == len(caminho)-1:
                custo_provisorio = matriz[caminho[j]][vertice] + matriz[vertice][0]    
            else:
                custo_provisorio = matriz[vertice][caminho[j]] + matriz[vertice][caminho[j+1]]
            
            # encontramos um custo menor do que o atual?
            if custo_provisorio <= custo:
                # então, salvamos esse custo como o menor atual
                custo = custo_provisorio            

                # representa a inserção do vértice no caminho que gere o menor custo
                indice2 = j+1 
                indice1 = vertice
        
        # inserimos os dois índices ao caminho
        caminho.insert(indice2, indice1)
    
    return caminho


# -----------------

def realiza_troca(rota_atual, i, k):
    # cria a nova rota, inicialmente vazia
    nova_rota = list()

    # adiciona a rota atual de 0 até o i - 1 à nova rota
    nova_rota.extend(rota_atual[0:i-1])

    # adiciona a rota de i até k em ordem reversa à nova rota
    nova_rota.extend(reversed(rota_atual[i-1:k]))

    # adiciona a rota de k até n (tamanho da rota) à nova rota
    nova_rota.extend(rota_atual[k:])

    return nova_rota

def two_opt(distancias, rota):
    print("Entrei no 2opt")
    # mantém a melhor rota encontrada até o momento
    # no início, a melhor rota É a rota de entrada
    melhor_rota = rota
    
    # 'flag' que mantém SE o algoritmo conseguiu fazer alguma melhora
    rota_melhorada = True

    # repete até que nenhuma melhora tenha sido feita
    while rota_melhorada:
        # não houve, até o momento, nenhuma melhora (marca como falso)
        # só haverá melhora se encontrar uma troca que tenha um custo menor
        rota_melhorada = False

        for i in range(1, len(rota) - 2):
            for j in range(i + 1, len(rota)):
                # ignoramos possíveis trocas não significativas
                if j - i == 1:
                    continue

                # cria a nova rota
                nova_rota = realiza_troca(rota, i, j)
                
                # obtêm os custos da rota anterior e da nova rota
                custo_nova_rota = obter_custo(distancias, nova_rota)
                custo_melhor_rota = obter_custo(distancias, melhor_rota)

                # ficamos com a nova rota se ela tiver um custo menor que a melhor rota
                # marcamos também que a rota foi melhorada e há possibilidade de melhorar mais
                if custo_nova_rota < custo_melhor_rota:
                    melhor_rota = nova_rota
                    rota_melhorada = True
        
        # persiste a melhor rota até o momento (melhor rota existente)
        # como a rota que deve ser usada para criar a próxima nova rota
        rota = melhor_rota

    print("saí do 2opt")
    
    # retorna a melhor rota encontrada pelo algoritmo
    return melhor_rota

# -----------------

#Heurísticas de Refinamento.

#Reinsertion.
#Temos que criar a vizinhança do "caminho" considerando a heurística 2-Opt -
#trocar cada vértice da solução 2 a 2.

def reinsertion(matriz, rota):
    print("entrei no reinsertion")

    #vetor onde será armazenada a rota de menor custo encontrada
    #- não necessariamente é a ótima!
    novo_caminho=rota
    #cópia de rota de forma a não modificar a variáivel "rota" - deepcopy
    vizinho = rota[:]
    #custo da rota inicial recebida na entrada
    distancia_inicial=obter_custo(matriz, rota)
    #para cada componente do vetor "rota", extraia-o e o reinsira na posição j
    #esse processo gera a quebra de duas arestas para cada elemento i do vetor "rota"
    for i in range(0,len(rota)):
        aux=rota[i]
        #nesse caso, consideramos um grafo com da a db igual db a da -
        #caso contrário, fazer j variar de zero a len(vizinho).
        for j in range(i,len(vizinho)):       
            vizinho.remove(aux)
            vizinho.insert(j,aux)
            #Aqui, caso a matriz adjacência seja simétrica, não precisaremos chamar
            #a função distância toda vez, basta incrementar novas arestas e excluir as
            #"quebradas"            
            distancia_vizinho=obter_custo(matriz, vizinho)
            #se encontrar caminho com custo menor do que o inicial, armazena o novo caminho
            if distancia_vizinho<distancia_inicial:
                distancia_inicial=distancia_vizinho
                novo_caminho = vizinho[:]
    
    print("saí do reinsertion")
    #retorna o novo caminho, se houver.
    return novo_caminho


# --------------

# ---------------

# #==============================================================================
# #Construção da Solução do Caxeiro Viajante
# #Iniciando o conjunto de vértices - 0 a d
# a=set()
# for i in range(0,d):
#     a.add(i)
# print(a)
# print("-="*40)
#==============================================================================
#Teste da heurística da menor_vizinhanca:
#caminho=menor_vizinhanca(n,0,a)
#print(caminho)
#print(distancia(caminho))
#==============================================================================
#Teste da Heuristica de BellmoreNemhauser:
#origem=0
#caminho=H_BellmoreNemHauser(n,origem,a)
#print(caminho)
#print(distancia(caminho))                  
#==============================================================================       
#Teste da Heuristica de Menor Inserção:
#caminho=Menor_Insercao(n,0,a)
#print(caminho)
#print
#print(distancia(caminho))
#print("-="*40)
#==============================================================================    
#Heurísticas de Refinamento.
#Teste da Reinsertion               
#print(caminho,Reinsertion(caminho),distancia(Reinsertion(caminho)))
#============================================================================== 

    

            
        

