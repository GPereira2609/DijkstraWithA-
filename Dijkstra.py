import sys
from heapq import heapify, heappush, heappop

def Dijkstra(grafo, origem, destino):
    inf = sys.maxsize
    nos = {
        'A':{'custo':inf, 'pred':[]},
        'B':{'custo':inf, 'pred':[]},
        'C':{'custo':inf, 'pred':[]},
        'D':{'custo':inf, 'pred':[]},
        'E':{'custo':inf, 'pred':[]},
        'E':{'custo':inf, 'pred':[]},
        'F':{'custo':inf, 'pred':[]},
        
    }
    nos[origem]['custo'] = 0
    visitados = []
    flag = origem
    for i in range(5):
        if (flag not in visitados):
            visitados.append(flag)
            minHeap = []
            for j in grafo[flag]:
                if (j not in visitados):
                    custo = nos[flag]['custo'] + grafo[flag][j]
                    if (custo < nos[j]['custo']):
                        nos[j]['custo'] = custo
                        nos[j]['pred'] = nos[flag]['pred'] + list(flag)
                    heappush(minHeap, (nos[j]['custo'], j))
        heapify(minHeap)
        flag = minHeap[0][1]
    print('Menor distância: %s' %(str(nos[destino]['custo'])))
    print('Menor caminho: %s' %(str(nos[destino]['pred'] + list(destino))))
 
