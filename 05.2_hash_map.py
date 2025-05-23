



## Entrada
s = "loveleetcode"

##primeiro parte do codigo:
d = {}
for idx, ch in enumerate(s):
    if not d.get(ch):
        d[ch] = [idx, 1]
    else:
        d[ch][1] += 1
 ##Vamos ver o que acontece a cada letra:

##   idx	ch	Ação	dicionário d atualizado
##   0	l	Nova letra, salva índice e conta 1	{'l': [0, 1]}
##   1	o	Nova letra	{'l': [0, 1], 'o': [1, 1]}
##   2	v	Nova letra	{'l': [0, 1], 'o': [1, 1], 'v': [2, 1]}
##   3	e	Nova letra	{'l': [0, 1], 'o': [1, 1], 'v': [2, 1], 'e': [3, 1]}
##   4	l	Já existe, soma 1 na contagem	{'l': [0, 2], ...}
##   5	e	Já existe, soma 1	{'e': [3, 2], ...}
##   6	e	Já existe, soma 1	{'e': [3, 3], ...}
##   7	t	Nova letra	{'t': [7, 1], ...}
##   8	c	Nova letra	{'c': [8, 1], ...}
##   9	o	Já existe, soma 1	{'o': [1, 2], ...}
##   10	d	Nova letra	{'d': [10, 1], ...}
##   11	e	Já existe, soma 1	{'e': [3, 4], ...}


# Resultado do dicionário d ao final:
##{
##  'l': [0, 2],
##  'o': [1, 2],
##  'v': [2, 1],
##  'e': [3, 4],
##  't': [7, 1],
##  'c': [8, 1],
##  'd': [10, 1]
##}

## Segunda parte do código:

for ch, val in d.items():
    if val[1] == 1:
        
        return val[0]

## Aqui, o código vai checar qual letra teve val[1] == 1 (ou seja, apareceu só uma vez), na ordem de aparecimento no dicionário:
 
## 'l': [0, 2] → aparece 2 vezes → pula
 
## 'o': [1, 2] → aparece 2 vezes → pula
 
## 'v': [2, 1] → aparece 1 vez → ✅ retorno: 2



##   Saída:

2
## A letra 'v' foi a primeira letra única, e está no índice 2

