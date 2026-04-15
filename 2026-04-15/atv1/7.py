invalido = True

while (invalido):
    nome, senha = map(str, input().split())

    if (nome == senha):
        print("ERROR")
    else:
        invalido = False
        print("Cadastro realizado!")