##Dada uma string s, encontre o índice do primeiro caractere que não se repete. 
##Se não houver tal caractere, retorne -1.

##Input: "leetcode"       → Output: 0  → ('l' aparece só uma vez, e é o primeiro)
##Input: "loveleetcode"   → Output: 2  → ('v' aparece só uma vez, e é o primeiro não repetido)
##Input: "aabb"           → Output: -1 → (todos os caracteres são repetidos)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Criamos um dicionário vazio para armazenar informações sobre cada letra
        # A chave será a letra, e o valor será uma lista: [índice da primeira vez que apareceu, contador de ocorrências]
        d = {}

        # Usamos enumerate para percorrer a string com índice (idx) e caractere (ch)
        for idx, ch in enumerate(s):
            # Se o caractere ainda não apareceu no dicionário
            if not d.get(ch):
                # Armazenamos o índice e colocamos a contagem como 1
                d[ch] = [idx, 1]
            else:
                # Se o caractere já está no dicionário, aumentamos a contagem
                d[ch][1] += 1

        # Agora vamos procurar a primeira letra que apareceu só uma vez
        for ch, val in d.items():
            # Se a contagem for exatamente 1, significa que essa letra é única
            if val[1] == 1:
                # Retornamos o índice onde essa letra apareceu pela primeira vez
                return val[0]

        # Se nenhuma letra for única, retornamos -1
        return -1




