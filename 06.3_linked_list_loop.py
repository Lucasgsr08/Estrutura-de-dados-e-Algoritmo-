# Definição da estrutura básica de um nó da lista ligada (comentado no print)
# class ListNode:
#     def __init__(self, x):
#         self.val = x       # valor do nó
#         self.next = None   # ponteiro para o próximo nó

# Classe que contém a solução
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Função para verificar se há ciclo na lista
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Inicializamos dois ponteiros: slow (devagar) e fast (rápido), ambos no início da lista
        slow = head
        fast = head

        # Enquanto fast não chegar ao fim da lista e houver um próximo nó
        while fast and fast.next:
            # slow anda 1 passo por vez
            slow = slow.next
            # fast anda 2 passos por vez
            fast = fast.next.next

            # Se os dois ponteiros se encontrarem, há um ciclo
            if slow == fast:
                return True

        # Se o loop terminar, não há ciclo
        return False


##  Resumo visual:

##  slow: caminha nó por nó.
  
##  fast: pula dois nós por vez.
  
##  Se a lista tiver um ciclo, fast e slow vão se encontrar.
  
##  Se fast chegar ao final (None), então não há ciclo.