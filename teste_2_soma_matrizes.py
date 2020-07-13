def dimensoes(matriz):
    col0 = matriz[0]
    min0 = len(col0)
    for linha in matriz:
        tam = len(linha)
        if tam < min0:
            min0 = tam
    dim = [len(matriz), min0]
    return dim

def soma_matrizes(m1, m2):
    soma = []
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)
    if dim1[0] == dim2[0] and dim1[1] == dim2[1]:
        for j in range(0, dim1[0]):
            linha = []
            for k in range(0, dim1[1]):
                x = m1[j][k] + m2[j][k]
                linha.append(x)
            soma.append(linha)
        return soma
    else:
        return False
