def dimensoes(matriz):
    col0 = matriz[0]
    max0 = len(col0)
    for linha in matriz:
        tam = len(linha)
        if tam > max0:
            max0 = tam
    dim = [len(matriz), max0]
    return dim

def sao_multiplicaveis(m1, m2):
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)
    if dim2[0] == dim1[1]:
        apr = True
    else:
        apr = False
    return apr
