class Triangulo:
	def __init__ (self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	
	def perimetro(self):
		return self.a + self.b + self.c
	
	def tipo_lado(self):
		if self.a == self.b and self.b == self.c:
			tipo = 'equilátero'
		elif self.a == self.b or self.b == self.c or self.a == self.c:
			tipo = 'isósceles'
		else:
			tipo = 'escaleno'
		return tipo
	
	def retangulo(self):
		if (self.a ** 2) == (self.b ** 2) + (self.c ** 2) or (self.b ** 2) == (self.c ** 2) + (self.a ** 2) or (self.c ** 2) == (self.a ** 2) + (self.b ** 2):
			status = True
		else:
			status = False
		return status
	
	def semelhantes(self, tr):
		if (self.a/tr.a) == (self.b/tr.b) == (self.c/tr.c) or (self.c/tr.a) == (self.a/tr.b) == (self.b/tr.c) or (self.b/tr.a) == (self.c/tr.b) == (self.a/tr.c):
			sem = True
		else:
			sem = False
		return sem