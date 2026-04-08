linhas, colunas = map(int, input().split())

array = []

for _ in range(linhas):
    linha = list(map(int, input().split()))
    array.extend(linha)

print(array)