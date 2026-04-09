import datetime

start = datetime.datetime.now()

linhas, colunas = map(int, input().split())

tabuleiro = []

for i in range(linhas):
    tabuleiro.append([])
    for _ in range(colunas):
        tabuleiro[i].append("*")

quant_fantasmas = list(map(int, input().split()))[0]

for _ in range(quant_fantasmas):
    x, y = map(int, input().split())
    tabuleiro[x-1][y-1] = "F"

x_pac, y_pac = map(int, input().split())

y_pac -= 1
x_pac -= 1

tabuleiro[x_pac][y_pac] = "P"

movimentos = input()

pontos = 0

for mov in movimentos:
    if tabuleiro[x_pac][y_pac] == 'P':
        tabuleiro[x_pac][y_pac] = ' '
    
    if mov == 'L':
        if y_pac < linhas - 1:
            y_pac +=1
    if mov == 'O':
        if y_pac > 0:
            y_pac -=1
    if mov == 'S':
        if x_pac < colunas - 1:
            x_pac +=1
    if mov == 'N':
        if x_pac > 0:
            x_pac -=1
    
    if tabuleiro[x_pac][y_pac] == '*':
        tabuleiro[x_pac][y_pac] = 'P'
        pontos +=1
    elif tabuleiro[x_pac][y_pac] == 'F':
        pontos = 0

# for _ in range(linhas):
#     print(tabuleiro[_])

# print(movimentos)
print(pontos)


end = datetime.datetime.now()

print(end - start)