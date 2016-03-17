
''' 
Dados 2 enteros, a y b, retorna True si uno de ellos es 10 o si su suma es 10.
makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True'''

def makes10(a,b): #método que recibe dos enteros
	return(a==10 or b==10 or a+b==10) #retorna true si a o b son igual a 10 o si la suma de ambos es igual a 10
 #retorna false si no se cumple alguna condición anterior
print(makes10(1,9)) #imprime el valor regresado por el método