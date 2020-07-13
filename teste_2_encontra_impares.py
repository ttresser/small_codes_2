def encontra_impares(lista):
	impares = []
	if len(lista) == 1:
		if lista[0] % 2 != 0:
			return lista[0:1]
		else:
			return []
	elif lista[0] % 2 != 0:
		impares.extend(lista[0:1])
	impares.extend(encontra_impares(lista[1:]))
		
	return impares