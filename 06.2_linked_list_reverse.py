class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = None(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None                # Começa sem nó anterior
        current = self.head        # Começa do primeiro nó

        while current:            # Enquanto não chegar no fim
            next_node = current.next  # Guarda o próximo nó
            current.next = prev       # Inverte a seta
            prev = current            # Avança o "anterior"
            current = next_node       # Avança o atual

        self.head = prev          # Atualiza o início da lista



