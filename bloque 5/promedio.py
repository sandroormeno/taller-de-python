
print("Programa que calcula el promedio de 5 números")
numeros = []
for i in range(5):
	print("Ingresa número (" + str(i+1) + "):")
	num = input()
	numeros.append(int(num))
print("Lista de números :" + str(numeros))
num = 0
for i in range(len(numeros)):
	num =  num + numeros[i]
salida = float(num/len(numeros))
print("Promedio de números :" + str(salida))
