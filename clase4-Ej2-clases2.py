#!/usr/bin/env python3

class MiClase:
	
	def __init__(self, value):
		self._value = value


@property	
def get_value(self):
	return self._value

def set_value(self, value):
	if not isinstance(value, float):
		raise ValueError
	self._value = value




c = MiClase(8)

c.set_value('hola')

print(c.get_value())
