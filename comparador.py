import leitor
import heuristicas

import vns
import vnd

import math
import time
import csv


def calcular_gap(valor_heuristica, valor_otimo):
    # realiza o cálculo do gap de acordo com a fórmula dada
    return ((valor_heuristica - valor_otimo) / valor_otimo) * 100


def carregar_instancias():
    print("Carregando instâncias...")
    
    # caminho da pasta aonde estão as instâncias
    # lembrar de não usar um '/' ao final do caminho
    caminho_instancias = "./instancias/instancias_teste"

    # lê o arquivo de descrição, que tem o nome da instância e o seu valor ótimo
    descricao_instancias = leitor.ler_descricao(caminho_instancias, "descricao.txt")

    for i in range(len(descricao_instancias)):
        # obtemos o nome dessa instância
        nome = descricao_instancias[i][0]

        # faz a leitura da matriz com a função do leitor
        # assumimos aqui que as instâncias lidas da descrição estão na pasta
        # e assumimos que todas estão em TXT e estão no mesmo padrão para o leitor
        matriz, dimensao = leitor.ler_instancia("{}/{}.txt".format(caminho_instancias, nome))

        # adicionamos a matriz e a dimensão dessa instância
        descricao_instancias[i].append(matriz)
        descricao_instancias[i].append(dimensao)
    
    # retorna um array de: [nome_instancia, valor_otimo, matriz_instancia, dimensao_instancia]
    return descricao_instancias


def realiza_testes():
    # faz a leitura de todas as instâncias
    instancias = carregar_instancias()

    # lista onde os resultados serão armazenados
    resultados = []

    for nome, valor_otimo, matriz, dimensao in instancias:
        print("Realizando testes para instância '{}'...".format(nome))

        # informações da execução heurística construtiva (VND)
        vnd_total_tempo = 0
        vnd_total_custo = 0
        vnd_melhor_custo = math.inf      # valor arbitrário

        # número de execuções para essa instância
        numero_execucoes = 10

        # realiza as execuções para a construtiva & VND
        for i in range(numero_execucoes):
            # marca o tempo inicial
            tempo_inicial = time.time()

            # executa a heurística construtiva 
            origem = 0
            rotamv, customv = heuristicas.menor_vizinhanca(matriz, dimensao, origem)

            # executa o VND
            rotavnd, custovnd = vnd.vnd(matriz, rotamv, customv)

            # é a menor solução? salvamos-a
            if custovnd < vnd_melhor_custo:
                vnd_melhor_custo = custovnd

            # marca o tempo final
            tempo_final = time.time()

            # obtêm o tempo total necessário
            tempo_total = tempo_final - tempo_inicial

            # adicionamos à soma de custos e de tempo
            vnd_total_tempo += tempo_total
            vnd_total_custo += custovnd
        
        # informações da execução metaheurística (VNS)
        vns_total_tempo = 0
        vns_total_custo = 0
        vns_melhor_custo = math.inf      # valor arbitrário

        # realiza as execuções para a construtiva & VNS
        for i in range(numero_execucoes):
            # marca o tempo inicial
            tempo_inicial = time.time()

            # executa a heurística construtiva 
            origem = 0
            rotamv, customv = heuristicas.menor_vizinhanca(matriz, dimensao, origem)

            # executa o VNS
            maximo_iteracoes_vns = 10
            rotavns, custovns = vns.vns(matriz, rotamv, customv, maximo_iteracoes_vns)

            # é a menor solução? salvamos-a
            if custovns < vns_melhor_custo:
                vns_melhor_custo = custovns

            # marca o tempo final
            tempo_final = time.time()

            # obtêm o tempo total necessário
            tempo_total = tempo_final - tempo_inicial

            # adicionamos à soma de custos e de tempo
            vns_total_tempo += tempo_total
            vns_total_custo += custovns

        # ok, temos os valores, então fazemos os cálculos de média e gap
        vnd_media_tempo = (vnd_total_tempo / numero_execucoes)
        vnd_media_custo = (vnd_total_custo / numero_execucoes)
        vnd_gap = calcular_gap(vnd_melhor_custo, valor_otimo)

        vns_media_tempo = (vns_total_tempo / numero_execucoes)
        vns_media_custo = (vns_total_custo / numero_execucoes)
        vns_gap = calcular_gap(vns_melhor_custo, valor_otimo)

        # cria a lista com a informação desse resultado dessa instância
        resultado = []

        resultado.append(nome)              # adiciona o nome da instância        
        resultado.append(valor_otimo)       # adiciona o valor ótimo da instância

        resultado.append(vnd_media_custo)   # adiciona a média da solução vnd
        resultado.append(vnd_melhor_custo)  # adiciona a melhor solução vnd
        resultado.append(vnd_media_tempo)   # adiciona a média do tempo vnd
        resultado.append(vnd_gap)           # adiciona o gap da solução vnd

        resultado.append(vns_media_custo)   # adiciona a média da solução vns
        resultado.append(vns_melhor_custo)  # adiciona a melhor solução vns
        resultado.append(vns_media_tempo)   # adiciona a média do tempo vns
        resultado.append(vns_gap)           # adiciona o gap da solução vns

        # adiciona esse resultado à lista de resultados
        resultados.append(resultado)
    
    # retorna a lista de resultados dos testes
    return resultados


def salva_resultados(resultados):
    print("Salvando resultados no arquivo...")

    with open("resultados.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)

        # adiciona o cabeçalho do arquivo
        cabecalho = ("instancia", "otimo", 
                     "vnd_media_solucao", "vnd_melhor_solucao", "vnd_media_tempo", "vnd_gap", 
                     "vns_media_solucao", "vns_melhor_solucao", "vns_media_tempo", "vns_gap")
        
        escritor.writerow(cabecalho)

        # adiciona os resultados no arquivo
        for resultado in resultados:
            escritor.writerow(resultado)


def main():
    print("Inicializando comparador...")

    resultados = realiza_testes()

    salva_resultados(resultados)

    print("Finalizado!")


if __name__ == "__main__":
    ti = time.time()

    main()

    tf = time.time()

    print("\nTempo Total: %.2f segundos!" % (tf - ti))

