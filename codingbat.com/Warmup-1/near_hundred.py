'''
Dado un entero n, regresar verdadero si esta entre 10 de 100 o 200
Nota: abs(num) calcula el valor absoluto de un número.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''

def near_hundred(n): #método que recibe entero
	return (abs(100-n)<=10 or abs(200-n)<=10) #regresa true si el absoluto de la resta de 100-n o 200-n es <=10

print(near_hundred(111)) #imprime lo regresado por el método