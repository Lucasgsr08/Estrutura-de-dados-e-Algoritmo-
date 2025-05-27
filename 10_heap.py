# Classe que representa uma Min Heap (estrutura onde o menor valor sempre fica no topo)
class Minheap:
    def __init__(self):
        self.heap = []  # Inicializa a heap como uma lista vazia

    # Retorna o índice do filho à esquerda do nó na posição 'index'
    def _left_child_index(self, index):
        return 2 * index + 1

    # Retorna o índice do filho à direita do nó na posição 'index'
    def _right_child_index(self, index):
        return 2 * index + 2

    # Retorna o índice do pai do nó na posição 'index'
    def _parent_index(self, index):
        return (index - 1) // 2

    # Sobe um valor no heap até que a propriedade do heap seja restaurada (menor no topo)
    def _heapify_up(self, index):
        if index == 0:
            return  # Já está no topo, nada a fazer

        parent_index = self._parent_index(index)
        # Se o valor atual for menor que o do pai, troca
        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Continua subindo o valor se necessário
            self._heapify_up(parent_index)

    # Desce um valor no heap para restaurar a propriedade do heap (menor no topo)
    def _heapify_down(self, index):
        size = len(self.heap)

        left_index = self._left_child_index(index)
        right_index = self._right_child_index(index)

        smallest_index = index  # Começa assumindo que o menor é o próprio índice atual

        # Verifica se o filho da esquerda existe e é menor
        if left_index < size and self.heap[left_index] < self.heap[smallest_index]:
            smallest_index = left_index
        
        # Verifica se o filho da direita existe e é ainda menor
        if right_index < size and self.heap[right_index] < self.heap[smallest_index]:
            smallest_index = right_index

        # Se o menor valor não for o atual, troca e continua descendo
        if smallest_index != index:
            self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
            self._heapify_down(smallest_index)

    # Insere um novo valor na heap
    def insert(self, value):
        self.heap.append(value)                  # Adiciona o valor no final da lista
        self._heapify_up(len(self.heap) - 1)     # Sobe o valor até a posição correta

    # Remove e retorna o menor valor (raiz da heap)
    def pop_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()  # Se houver apenas um elemento, remove e retorna

        root = self.heap[0]               # Guarda o menor valor (topo)
        self.heap[0] = self.heap.pop()    # Substitui o topo pelo último valor
        self._heapify_down(0)             # Desce o valor do topo até a posição correta
        return root                       # Retorna o menor valor removido

    # Exibe a heap atual
    def display(self):
        print("Heap atual:", self.heap)

# Testa a classe Minheap
if __name__ == "__main__":
    min_heap = Minheap()            # Cria uma nova heap
    min_heap.insert(0)              # Insere vários valores
    min_heap.insert(1)
    min_heap.insert(2)
    min_heap.insert(3)
    min_heap.insert(4)
    min_heap.insert(5)
    min_heap.insert(6)
    
    print(min_heap.pop_min())       # Remove e imprime o menor valor da heap
    min_heap.display()              # Mostra o estado atual da heap
