def maiusculas(frase):
	frase1 = ''
	for j in range(0, len(frase)):
		for k in range(65,91):
			if ord(frase[j]) == k:
				frase1 += frase[j]
	return frase1