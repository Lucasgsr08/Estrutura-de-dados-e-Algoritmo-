                    ######OBJETIVO DO CÓDIGO########




##Encontrar o maior pedaço (substring) da string s que tem no máximo 2 letras iguais.
##Exemplo:
##Entrada: 'abcabcabc'
##Substring válida mais longa: 'abcab' (porque nenhuma letra aparece 3 vezes)


## Define a classe Solution com o método maximumLengthSubstring
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        ## l = início da janela, r = fim da janela (começam em 0)
        l, r = 0, 0

        ## _max guarda o maior tamanho encontrado
        _max = 1

        ## Dicionário que conta quantas vezes cada letra apareceu
        counter = {}

        ## Inicializa a contagem com a primeira letra da string
        counter[s[0]] = 1

        ## Enquanto ainda não chegou no fim da string
        while r < len(s) - 1:

            ## Move o ponteiro da direita (r) para a direita
            r += 1

            ## Se a letra já apareceu, soma +1 no contador
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                ## Se é a primeira vez que aparece, inicia com 1
                counter[s[r]] = 1

            ## Enquanto a letra atual apareceu 3 vezes:
            while counter[s[r]] == 3:
                ## Diminui a contagem da letra à esquerda (l)
                counter[s[l]] -= 1
                ## Move o ponteiro da esquerda para frente
                l += 1

            ## Atualiza o maior tamanho (_max) com o tamanho da janela atual
            _max = max(_max, r - l + 1)

        ## Retorna o maior tamanho de substring válida
        return _max
