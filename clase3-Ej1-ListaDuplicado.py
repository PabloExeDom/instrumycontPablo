#!/usr/bin/env python3

x = [1, 2, 3]

def duplicar(lista):
	y = []
	for elemento in lista:
		y.append(2 * elemento)
	return y

print(x)
print(duplicar(x))
