A, taxaA = map(float, input().split())
B, taxaB = map(float, input().split())

anos = 0

while (B > A):
    A *= 1 + taxaA
    B *= 1 + taxaB
    anos += 1

print(anos)