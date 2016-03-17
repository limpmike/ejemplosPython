
'''
Dado un entero m, retorna la diferencia absoluta entre n y 21, excepto cuando n sea mayor de 21 
retorna el doble de la diferencia absoluta 
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0'''

def diff21(n): #método que recibe un entero n
	if(n<21): #si n es menor que 21
		return 21-n #retornamos 21 menos el entero n
	else: #de lo contrario n es >=21
		return (n-21)*2 #retornamos el entero n menos 21 multiplicado por dos para obtener el doble
		#poniendo la resta dentro de paréntesis para que no afecte el orden de las operaciones

print(diff21(22)) #impresión del entero retornado por el método