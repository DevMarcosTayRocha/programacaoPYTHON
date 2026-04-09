linhas, colunas = map(int, input().split())

tabuleiro = []

for i in range(linhas):
    tabuleiro.append([])
    for j in range(colunas):
        tabuleiro[i].append("*")

quant_fantasmas, *_ = map(int, input().split())

for _ in range(quant_fantasmas):
    x, y = map(int, input().split())
    tabuleiro[x-1][y-1] = "F"

x_pac, y_pac = map(int, input().split())
y_pac -= 1
x_pac -= 1
tabuleiro[x_pac][y_pac] = "P"

movimentos = input()

pontos = 0

def funcMov(eixo, valor):
    global x_pac
    global y_pac
    global tabuleiro
    global pontos
    global linhas
    global colunas
    
    print(x_pac)
    
    if tabuleiro[x_pac][y_pac] == 'P':
        tabuleiro[x_pac][y_pac] = ' '
        
    if eixo == 1 and valor == 1 y_pac < linhas - 1 and y_pac > 0:
        y_pac += valor
    
    if eixo == 2 and x_pac < colunas - 1 and x_pac > 0:
        x_pac += valor
    
    if tabuleiro[x_pac][y_pac] == '*':
        tabuleiro[x_pac][y_pac] = 'P'
        pontos +=1
        
    elif tabuleiro[x_pac][y_pac] == 'F':
        pontos = 0

for mov in movimentos:
    if mov == 'L':
        funcMov(1, 1)
        
    if mov == 'O':
        funcMov(1, -1)
        
    if mov == 'S':
        funcMov(2, 1)
        
    if mov == 'N':
        funcMov(2, -1)
        
for _ in range(linhas):
    print(tabuleiro[_])


print(movimentos)
print(pontos)
print(x_pac)