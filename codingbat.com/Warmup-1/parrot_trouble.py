
'''
Tenemos a un loro hablador ruidoso. El parámetro hour(hora) 
es la hora actual en el rango de 0..23. Estaremos en problemas
si el loro esta hablando y la hora es antes de las 7 o después de
las 20. Regresa verdadero si estamos en problemas.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
'''

def parrot_trouble(talking, hour): #método que recibe booleano y entero
	if(talking and (hour<7 or hour>20)): #si esta hablando y hora es menor que 7 o la hora es mayor que 20
		return True #retornamos True
	else: #si no esta hablando
		return False #retornamos False

print(parrot_trouble(False,21)) #impresión del Booleano retornado por el método