#%%
import heapq  # Importa o módulo heapq para usar uma fila de prioridade (min heap)

# Função que implementa o algoritmo de Dijkstra
def dijkstra(graph, start):
    # Inicializa o heap com distância 0 para o nó inicial
    min_heap = [(0, start)]

    # Inicializa todas as distâncias como infinito
    distances = {node: float('inf') for node in graph}

    # Define a distância inicial como 0
    distances[start] = 0

    # Enquanto houver nós na fila de prioridade
    while min_heap:
        # Remove o nó com menor distância da fila
        current_distance, current_node = heapq.heappop(min_heap)

        # Se a distância atual for maior do que a já registrada, pula (foi atualizada antes)
        if current_distance > distances[current_node]:
            continue

        # Percorre todos os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            # Calcula a nova distância até o vizinho
            distance = current_distance + weight

            # Se essa nova distância for menor do que a atual registrada
            if distance < distances[neighbor]:
                # Atualiza a distância
                distances[neighbor] = distance

                # Adiciona o vizinho à fila com sua nova distância
                heapq.heappush(min_heap, (distance, neighbor))

    # Retorna o dicionário com as menores distâncias até cada nó
    return distances

# Exemplo de grafo representado como dicionário de dicionários
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Exemplo de chamada da função
resultado = dijkstra(graph, 'A')
print(resultado)  # Mostra as menores distâncias a partir do nó 'A'


{    'A': 0,
    'B': 1,
    'C': 3,
    'D': 4
}





        ## Explicação geral: ##

## Objetivo: Encontrar o menor caminho de um nó inicial para todos os outros em um grafo com pesos positivos.
 
## Estrutura usada: Min-heap (fila de prioridade com heapq) e um dicionário de distâncias.

## Complexidade: O algoritmo é eficiente para grafos esparsos: O((V + E) * log V) com heap.
# %%
