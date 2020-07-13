def mais_curto(lista):
	small = lista[0].strip()
	for j in lista:
		k = j.strip()
		if len(k) < len(small):
			small = k
	return small.capitalize()

def menor_string(lista):
	smaller = lista[0].lower()
	for j in lista:
		k = j.lower()
		if k < smaller:
			smaller = j
	return smaller