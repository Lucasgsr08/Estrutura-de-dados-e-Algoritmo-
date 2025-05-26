# Função bubble sort com otimização: para mais eficiência, ela para se a lista já estiver ordenada
def bubble(nums):
    size = len(nums)  # Calcula o tamanho da lista

    # Faz várias passagens pela lista (máx. igual ao número de elementos)
    for _ in nums:
        is_sorted = True  # Assume que a lista já está ordenada no início da passagem

        print(nums)  # Mostra o estado atual da lista a cada laço externo (passada)

        # Percorre os elementos até o penúltimo
        for i in range(size - 1):
            # Se o elemento atual for maior que o próximo, troca
            if nums[i] > nums[i + 1]:
                is_sorted = False  # Marca que houve troca (então ainda não está ordenada)
                # Troca de posição usando desembrulhamento de tupla
                nums[i + 1], nums[i] = nums[i], nums[i + 1]

        # Se não houve nenhuma troca nesta passada, a lista já está ordenada
        if is_sorted:
            return  # Sai da função mais cedo (otimização)


bubble([5, 4, 3, 2, 1])
