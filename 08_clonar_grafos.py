# Classe que representa um nó de um grafo
class Node:
    def __init__(self, val, neighbors=None):
        self.val = val  # Valor do nó
        self.neighbors = neighbors if neighbors is not None else []  # Lista de vizinhos

def clone_graph(node):
    # Dicionário para armazenar os nós clonados {original: cópia}
    visitado = {}

    # Função auxiliar recursiva para clonar o grafo
    def dfs(n):
        if n in visitado:
            return visitado[n]  # Retorna a cópia já criada

        # Cria um novo nó com o mesmo valor
        copia = Node(n.val)
        visitado[n] = copia  # Armazena a cópia no dicionário

        # Clona todos os vizinhos do nó atual recursivamente
        for vizinho in n.neighbors:
            copia.neighbors.append(dfs(vizinho))  # Adiciona vizinho clonado

        return copia

    # Caso o grafo esteja vazio
    return dfs(node) if node else None

# -----------------------------
# 🧪 EXEMPLO DE USO:

# Criando grafo original:
#   1 -- 2
#   |    |
#   4 -- 3

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

# Clonando o grafo
clonado = clone_graph(n1)

# Função para imprimir grafo (para verificação)
def imprimir_grafo(node, visitados=set()):
    if node in visitados:
        return
    visitados.add(node)
    print(f"Nó {node.val} -> {[viz.val for viz in node.neighbors]}")
    for vizinho in node.neighbors:
        imprimir_grafo(vizinho, visitados)

# Mostrando o grafo clonado
print("Grafo clonado:")
imprimir_grafo(clonado)


## 📝 Explicação geral:
## Cada nó é um objeto com valor (val) e lista de vizinhos (neighbors).
## 
## A função clone_graph usa DFS (busca em profundidade) com memorização (dicionário) para evitar ciclos infinitos.
## 
## O grafo pode ter ciclos e conexões bidirecionais, e o algoritmo lida com isso corretamente.