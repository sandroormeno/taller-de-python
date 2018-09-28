
print("Programa para calcular el factorial de un número.")
print("Ingrese un número:")
n = input()
j = 1
for i in range(1, int(n)+1): # más uno para contar con le número
	j = j * i
print("Factorial: " + str(j))
