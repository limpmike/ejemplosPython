'''
El parámetro weekday(día entre semana) es verdadero si es un día entre semana, y el parámetro vacation
es verdadero si estamos de vacaciones. Nos quedamos a dormir si no es un día entre semana o estamos de vacaciones.
Regresamos verdadero si nos quedamos a dormir.
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation): #método que recibe weekday y vacation
	if not weekday or vacation: #comprueba si no es weekday o vacation
		return True  #retorna true
	else: #si es weekday o no es vacation
		return False #retorna falso 

print(sleep_in(True,False)) #impresión del valor retornado del método sleep_in