def soma_matrizes(a, b):
    c = []
    for j in range(len(a)):
        c0 = []
        for k in range(len(a[0])):
            c1 = a[j][k] + b[j][k]
            c0.append(c1)
        c.append(c0)
    return c

def multi_matrizes(a, b):
    c = []
    for i in range(len(a)):
        c[i] = []
    m = 0
    while m < len(a):
        for j in range(len(a)):
            c2 = 0
            for k in range(len(a[0])):
                c1 = a[j][k] * b[k][j]
                c2 += c1
            c[j].append(c2)
        m += 1

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[10,20,30],[40,50,60],[70,80,90]]
print(soma_matrizes(a,b))
