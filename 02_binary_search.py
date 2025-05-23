## Função de busca binária: procura um número (n) dentro de uma lista ordenada (nums)
def binary_search(nums, n):
    ## Define os índices de início (lo) e fim (hi) da busca
    lo = 0
    hi = len(nums)
    ## Contador de passos (quantas vezes o laço rodou)
    steps = 0

    ## Enquanto ainda houver espaço entre lo e hi
    while lo < hi:
        ## Conta um passo a mais
        steps += 1
        ## Calcula o índice do meio da lista atual
        mid = int((lo + hi) / 2)

        ## Se o número no meio é o que buscamos, imprime os passos e retorna o índice
        if nums[mid] == n:
            print("step:", steps)
            return mid
        ## Se o número no meio é menor que o que buscamos, descartamos a metade da esquerda
        elif nums[mid] < n:
            lo = mid + 1
        ## Caso contrário, descartamos a metade da direita
        else:
            hi = mid

    ## Se não encontrar o número, retorna -1
    return -1

## Testes com listas ordenadas de diferentes tamanhos
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

## Chama a função para buscar o número 3 dentro da lista d
binary_search(d, 3)



## 🔍 Como funciona passo a passo (exemplo com d = [1, 2, ..., 40] e n = 3):
## Calcula o meio da lista: mid = (0 + 40) / 2 = 20. Verifica o valor d[20] = 21.
## Como 21 > 3, ignora tudo à direita (21 pra frente).
## Novo meio: entre 0 e 20 → mid = 10, d[10] = 11 → ainda maior.
## Novo meio: entre 0 e 10 → mid = 5, d[5] = 6 → ainda maior.
## Novo meio: entre 0 e 5 → mid = 2, d[2] = 3 → achou o valor!
## ⏱ Isso tudo em 4 passos (bem mais rápido que testar 1 por 1 até 40!).