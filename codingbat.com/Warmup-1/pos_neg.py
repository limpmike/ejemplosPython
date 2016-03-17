'''
Dados 2 enteros, retornar True si uno es negativo y uno es positivo. Excepto si el parametro
"negative" es Verdadero, entonces retorna true si ambos son negativos.
pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''

def pos_neg(a, b, negative): #método que recibe dos enteros y un booleano
	if(not negative): #si no es negativo
		return (a<0 and b>=0 or a>=0 and b<0) #regresa true si a es - y b  es + o igual que cero (lo mismo para b)
	else: #de lo contrario
	  	return (a<0 and b<0) #retorna true si a y b son negativos
 
print (pos_neg(-4,5,True)) #imprime lo regresado por el método
