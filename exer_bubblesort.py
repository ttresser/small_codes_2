def bolha(lista):
	fim = len(lista)
	for j in range(fim - 1, 0, -1):
		for k in range(j):
			if lista[k] > lista[k + 1]:
				lista[k], lista[k + 1] = lista[k + 1], lista[k]
				print(lista)
	return lista