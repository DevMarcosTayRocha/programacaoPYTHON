# conversao entre tipos de dados

# string
nome = input("Qual o seu nome? ")
print(nome)
print(type(nome))

# inteiro
idade = int(input("Quantos anos você tem? "))
print(idade)
print(type(idade))

#float
nota = float(input("Qual foi a sua nota final? "))
print(nota)
print(type(nota))

# "S" ou qualquer coisa
matriculado_str = input("Você esta matriculado?")
matriculado_bool = matriculado_str.lower() == "s"
print(matriculado_bool)
print(type(matriculado_bool))