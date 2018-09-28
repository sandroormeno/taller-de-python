
#un número primo es un número natural mayor que 1 
#que tiene únicamente dos divisores distintos: él mismo y el 1.​​
num = 1
for p in range(2, 30):# a partir de dos
	for div in range(2, p):
	    if p % div != 0: # el módulo (%) de devuelve el resto de la división
	    	#div no es divisor de p, p puede ser Número primo
	        continue
	    else:
	    	#div es divisor de p, p  no es un número primo
	        break #ya NO es necesario buscar más divisores
	else:
		#El bucle ha terminado
        #El número que estábamos comprobando es primo
	    print (str(num) + " : " + str(p))
	    num = num + 1
