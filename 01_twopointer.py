class Solution:
    def reverseWords(self, s):
        res = ''             # Aqui vamos guardar o resultado final
        l, r = 0, 0          # Dois "ponteiros" (índices) para marcar início e fim da palavra

        while r < len(s):   # Enquanto não chegarmos no fim da frase
            if s[r] != ' ':      # Se o caractere atual NÃO for um espaço...
                r += 1           # ...avança o fim da palavra (r)
            else:                # Se achou um espaço...
                res += s[l:r][::-1]  # Inverte a palavra entre l e r e adiciona no resultado
                res += ' '          # Adiciona o espaço depois da palavra
                r += 1              # Avança o ponteiro r para depois do espaço
                l = r              # Atualiza o início da próxima palavra

        res += s[l:r+1][::-1]  # Depois que o `while` termina, inverte a última palavra
        return res[1:]         # Retorna o resultado sem o primeiro espaço (caso tenha sobrado)


## O que esse código faz?
## Vamos usar o exemplo: "bom dia"

## Inicialmente:
## res = ''
## l = 0, r = 0
## A string é 'bom dia'

## A primeira palavra é 'bom'. O código vai aumentar r até achar o espaço depois de 'bom' (no índice 3).
## Quando encontra o espaço, ele pega a palavra entre l=0 e r=3 → 'bom', inverte: 'mob', e adiciona ao res.
## Também adiciona o espaço e atualiza l e r para o começo da próxima palavra.

## Repete o processo com 'dia' → inverte para 'aid'.
## No final, retorna: 'mob aid'.

## Sobre [::-1]
## Esse é um fatiamento com passo negativo. Ele inverte a string:
## Exemplo: 'casa'[::-1] resulta em 'asac'.

## Sobre res[1:]
## Se ao final sobrar um espaço desnecessário no começo, r
