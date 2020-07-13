def busca(lista, elemento):
	primeiro = 0
	ultimo = len(lista) - 1
	t = True
	while t and primeiro <= ultimo:
		media = (primeiro + ultimo) // 2
		if lista[media] == elemento:
			t = False
			print(media)
			return media
		elif lista[media] > elemento:
			print(media)
			ultimo = media - 1
		elif lista[media] < elemento:
			print(media)
			primeiro = media + 1
	if t:
		return False