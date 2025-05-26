# Merge Sort: algoritmo de ordenação do tipo "dividir para conquistar"
# A ideia principal é dividir a lista em partes menores, ordenar essas partes e depois juntá-las em ordem

def merge_sort(arr):
    # Caso base: se a lista tiver 1 ou 0 elementos, já está ordenada
    if len(arr) <= 1:
        return arr

    # Divide a lista em duas metades
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]

    # Aplica merge_sort recursivamente em cada metade
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

    # Junta as duas metades ordenadas
    return merge(esquerda_ordenada, direita_ordenada)

# Função que junta duas listas ordenadas em uma única lista ordenada
def merge(esquerda, direita):
    resultado = []  # Lista que irá conter o resultado da junção
    i = j = 0  # Índices para percorrer esquerda e direita

    # Compara os elementos das duas listas e adiciona o menor ao resultado
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona o que restou da lista esquerda (se sobrou algo)
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    # Adiciona o que restou da lista direita (se sobrou algo)
    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado  # Retorna a lista final ordenada

# Exemplo de uso:
arr = [5, 2, 9, 1, 3, 6, 4, 8, 7]
ordenada = merge_sort(arr)
print("Lista ordenada:", ordenada)




                ##  Como funciona o Merge Sort:##
##  Divide a lista ao meio, recursivamente, até que cada sublista tenha 1 ou 0 elementos.
##  
##  Conquista: ao voltar da recursão, as sublistas são mescladas (merge) de forma ordenada.
##  
##  Isso garante que o resultado final seja uma lista totalmente ordenada.