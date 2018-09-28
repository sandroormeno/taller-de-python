def factorial(n):
	j = 1
	for i in range(1, int(n)+1): # más uno para contar con le número
		j = j * i
	print("Factorial: " + str(j))

print("Programa para calcular el factorial de un número.")
numero = input("Ingrese un número: ")
factorial(numero)

