## Uma linked list é uma forma de organizar dados em sequência, mas diferente de uma lista comum (list do Python), os elementos não ficam em posições fixas na memória. Em vez disso, cada item aponta para o próximo.
## 
## Analogia simples:
## Pense em um trem, onde cada vagão tem:
## 
## Um valor (por exemplo: "3", "7", "15")
## 
## Um acoplamento que leva ao próximo vagão.


# Define o que é um "nó"
class Node:
    def __init__(self, data):
        self.data = data      # Armazena o valor
        self.next = None      # Ponteiro para o próximo nó

# Cria a estrutura da Linked List
class LinkedList:
    def __init__(self):
        self.head = None      # Começa sem nenhum nó

    # Adiciona um valor no final da lista
    def append(self, data):
        new_node = Node(data)  # Cria um novo nó com o valor

        if self.head is None:
            self.head = new_node  # Se a lista está vazia, esse será o primeiro
        else:
            current = self.head   # Começa do início
            while current.next:   # Vai até o último nó
                current = current.next
            current.next = new_node  # Adiciona o novo nó ao final

    # Exibe a lista
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

lista = LinkedList()
lista.append(10)
lista.append(20)
lista.append(30)

lista.display()
# Saída esperada: 10 -> 20 -> 30 -> None
