# Classe que representa um nó individual da lista encadeada
class Node:
    def __init__(self, data):
        self.data = data      # Armazena o valor do nó
        self.next = None      # Ponteiro para o próximo nó (inicialmente None)

# Classe Stack (pilha) usando lista encadeada
class Stack:
    def __init__(self):
        self.top = None       # O topo da pilha começa como None (pilha vazia)
        self._size = 0        # Tamanho da pilha começa em 0

    # Adiciona um novo elemento no topo da pilha
    def push(self, data):
        new_node = Node(data)     # Cria um novo nó com o dado
        new_node.next = self.top  # Aponta o novo nó para o antigo topo
        self.top = new_node       # Atualiza o topo da pilha
        self._size += 1           # Aumenta o tamanho da pilha

    # Remove e retorna o elemento do topo da pilha
    def pop(self):
        if self.is_empty():               # Verifica se a pilha está vazia
            raise IndexError("pop from empty stack")
        data = self.top.data              # Pega o valor do topo
        self.top = self.top.next          # Move o topo para o próximo nó
        self._size -= 1                   # Diminui o tamanho da pilha
        return data                       # Retorna o valor removido

    # Retorna o valor do topo da pilha sem removê-lo
    def peek(self):
        if self.is_empty():               # Verifica se a pilha está vazia
            raise IndexError("peek from empty stack")
        return self.top.data              # Retorna o valor do topo

    # Verifica se a pilha está vazia
    def is_empty(self):
        return self.top is None           # Retorna True se não houver elementos

    # Retorna o número de elementos na pilha
    def size(self):
        return self._size                 # Retorna o tamanho da pilha


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())     # 30
print(s.pop())      # 30
print(s.size())     # 2
print(s.is_empty()) # False



##  🔍 Resumo:
##  Node: representa cada elemento da pilha com valor (data) e ponteiro para o próximo (next).
##  
##  Stack: gerencia os nós empilhando no topo e operando no estilo LIFO (último a entrar, primeiro a sair).