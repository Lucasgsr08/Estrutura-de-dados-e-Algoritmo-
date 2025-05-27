class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)# Define uma classe chamada stack (pilha)
class stack:
    
    # Método construtor: inicializa uma lista vazia chamada items para armazenar os elementos da pilha
    def __init__(self):
        self.items = []

    # Método para empilhar (adicionar) um item ao topo da pilha
    def push(self, item):
        self.items.append(item)  # Usa o método append da lista para adicionar o item no final

    # Método para desempilhar (remover) o item do topo da pilha
    def pop(self):
        if not self.is_empty():  # Verifica se a pilha não está vazia
            return self.items.pop()  # Remove e retorna o último item da lista (topo da pilha)
        raise IndexError("pop from empty stack")  # Gera um erro se tentar desempilhar uma pilha vazia

    # Método para visualizar o item do topo da pilha sem removê-lo
    def peek(self):
        if not self.is_empty():  # Verifica se a pilha não está vazia
            return self.items[-1]  # Retorna o último item da lista (topo da pilha)
        raise IndexError("peek from empty stack")  # Gera um erro se tentar ver o topo de uma pilha vazia

    # Método para verificar se a pilha está vazia
    def is_empty(self):
        return len(self.items) == 0  # Retorna True se a lista estiver vazia, senão False

    # Método para retornar o tamanho atual da pilha
    def size(self):
        return len(self.items)  # Retorna o número de elementos dentro da lista (tamanho da pilha)



##  📌 Resumo:
##  Essa classe simula o comportamento de uma pilha (estrutura LIFO – Last In, First Out).
##  
##  Os métodos principais são:
##  
##  push: adiciona ao topo
##  
##  pop: remove do topo
##  
##  peek: visualiza o topo
##  
##  is_empty: verifica se está vazia
##  
##  size: retorna o tamanho atual da pilha

