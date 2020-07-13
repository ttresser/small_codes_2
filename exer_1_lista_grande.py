def lista_grande(n):
	import numpy as np
	lista = []
	for j in np.random.randint(-1000, 1000, n):
		lista.append(j)
	return lista
