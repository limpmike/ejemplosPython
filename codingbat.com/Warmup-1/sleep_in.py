def sleep_in(weekday, vacation): #método que recibe weekday y vacation
	if not weekday or vacation: #comprueba si no es weekday o vacation
		return True  #retorna true
	else: #si es weekday o no es vacation
		return False #retorna falso 

print(sleep_in(True,False)) #impresión del valor retornado del método sleep_in