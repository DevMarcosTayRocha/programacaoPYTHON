# variaveis
# operador de atribuição

nome = "Alice"
sobrenome = "Smith"
idade = 30
altura = 1.75
matriculado = True

# saida de dados

print("Nome:", nome)
print("Sobrenome:", sobrenome)

# tipos de dados

print(type(nome))
print(type(idade))
print(type(altura))
print(type(matriculado))

# entrada de dados

nome_usuario = input("Digite seu nome: ")
sobrenome_usuario = input("Digite seu sobrenome: ")
nome_completo = nome_usuario + " " + sobrenome_usuario # concatenacao de strings
print("Olá,", nome_completo)

# f-strings (strings formatadas / interpolação de strings)

print(f"Nome, {nome_usuario} {sobrenome_usuario } tem {idade} anos e mede {altura} metros.")