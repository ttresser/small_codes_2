def menor_nome(lista):
	smaller = lista[0].strip()
	for j in lista:
		k = j.strip()
		if len(k) < len(smaller):
			smaller = k
	return smaller.capitalize()