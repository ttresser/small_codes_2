def ordenada(lista1):
    lista = []
    lista += lista1
    fim = len(lista)
    for i in range(fim-1):
        pos_menor = i
        for j in range(i+1,fim):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor],lista[i]
    if lista == lista1:
        return True
    else:
        return False

num = [32,4,67,54,12,-8,-544,0,81,3,16,29,52,40]
print(ordenada(num))