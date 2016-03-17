'''
Dados dos enteros, retorna su suma. A menos que los dos valores sean el mismo, entonces retorna el doble
de su suma.
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double(a, b): #método que recibe dos enteros
	if(a!=b): #si a es diferente de b
		return a+b #regresa suma de a+b
	else: #si a y b son iguales
		return (a+b)*2 #regresa el doble de a+b

print(sum_double(2,2)) #impresión del valor retornado por el método