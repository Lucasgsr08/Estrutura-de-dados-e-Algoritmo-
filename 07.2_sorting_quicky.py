# Função principal de ordenação usando o algoritmo Quick Sort
def quicksort(arr, left, right):
    # Se ainda há mais de um elemento entre os índices left e right
    if left < right:
        print(arr[left:right+1])  # Mostra a sublista atual que está sendo processada
        # Usamos right+1 porque o Python ignora o último índice em slices

        # Chama a função de partição que escolhe o pivô e reorganiza os elementos
        pi = partition(arr, left, right)

        # Aplica o quicksort recursivamente na sublista à esquerda do pivô
        quicksort(arr, left, pi - 1)

        # Aplica o quicksort recursivamente na sublista à direita do pivô
        quicksort(arr, pi + 1, right)

# Função que organiza os elementos ao redor do pivô e retorna sua posição final
def partition(arr, left, right):
    pivot = arr[right]  # Define o último elemento da sublista como pivô

    i = left - 1  # Índice do menor valor encontrado, começa fora da faixa útil

    # Percorre os elementos da sublista, excluindo o pivô
    for j in range(left, right):
        # Se o elemento atual é menor ou igual ao pivô, ele deve ir para a esquerda
        if arr[j] <= pivot:
            i += 1  # Avança o índice do menor valor
            arr[i], arr[j] = arr[j], arr[i]  # Troca os elementos de posição

    # Coloca o pivô no lugar certo, entre menores e maiores
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1  # Retorna o índice onde o pivô foi colocado

# Lista de exemplo a ser ordenada
arr = [0, 3, 6, 7, 8, 4, 2, 1, 5]

# Chamada da função quicksort informando os índices inicial e final da lista
quicksort(arr, 0, len(arr) - 1)
