
'''
Tenemos dos monos, a y b, y los parámetros a_smile y b_smile indican
si cada uno esta sonriendo. Estaremos en problemas si ambos están
sonriendo o si ninguno de ellos lo esta haciendo. Regresa verdadero si
estamos en problemas.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

def monkey_trouble(a_smile, b_smile): #método que recibe dos booleanos
	return(a_smile and b_smile or (not a_smile and not b_smile)) #retorna true si a y b son verdaderos o
	#si a y b son falsos de lo contrario retorna false

print(monkey_trouble(True,False)) #imprime el booleano retornado por el método