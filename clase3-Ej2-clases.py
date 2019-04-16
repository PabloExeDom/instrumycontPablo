#!/usr/bin/env python3

class MiLista:

	def __init__(self, contenido):
		self.contenido = contenido #contenido se vuelve un atributo de la variable
	
	def duplicar(self):	#lo que ingresa es self
		y = []
		for elemento in self.contenido:	#aca uso el contenido de self
			y.append(2 * elemento)
		return y
		
	def largo(self):	#lo que ingresa es self
		return len(self.contenido)


x = MiLista([1, 2, 3, 4, 5]) # Ahora tiene el atributo duplicar


print(x.duplicar())
print(x.largo())
