valido = True

while(valido):
    n, *_ = map(int, input().split())

    if (n >= 0 and n <= 10):
        valido = False
        print(n, "valido")
    else:
        print("invalido")