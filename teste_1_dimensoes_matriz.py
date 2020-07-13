def dimensoes(matriz):
    col0 = matriz[0]
    max = len(col0)
    for linha in matriz:
        tam = len(linha)
        if tam > max:
            max = tam
    col = max
    lin = len(matriz)
#    return str(lin) + 'X' + str(col)
    print(str(lin) + 'X' + str(col))
