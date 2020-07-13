def imprime_matriz(matriz):
    for lin in matriz:
        a = len(lin)
        for j in range(0, a - 1):
            print(lin[j], end = ' ')
        print(lin[a - 1])
