#fatiamento de listas
# list slicing

# lista[inicio:fim:passo]
# indices comecam no 0
# valores negativos contam de tras pra frente

#lista
numeros = [0,1,2,3,4,5,6,7,8,9]
print(numeros)

# do indice 2 ate o 5 (inclui o 2 / exclui o 5)

print(numeros[2:5])

# omitindo o inicio
print(numeros[:4])

# omitindo o final
print(numeros[6:])

# passo
print(numeros[2:7:2])

# copia
copia = numeros[:]
print(numeros)
print(copia)

# indices negativos
print(numeros[0]) # primeiro
print(numeros[-1]) # ultimo
print(numeros[-3:]) # antepenultimo ate o final
print(numeros[::-1]) # ordem inversa

inverso = numeros[::-1]
print(inverso)

# modificando parte da lista
numeros[2:5] = [20,30,40]
print(numeros)

# removendo elementos com slice
del numeros[0:2]
print("del numeros[0:2]", numeros)

# list (mutavel), tuple(imutavel), strings
a = [101, "Fulano", True, 8.50]
b = (101, "Fulano", True, 8.50)

nome = "Luiz Rodrigues"
print(nome[0])
print(nome[-1])
print(nome[:4])
print(nome[-2:])
print(nome[::-1])

separandoNome = nome.split()
print(separandoNome)