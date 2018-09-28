
def palintromo(test):
	lista_de_letras = []
	for i in range(len(test)):
		lista_de_letras.append(test[i])
	lista_de_letras.reverse()
	salida = ""
	for i in range(len(lista_de_letras)):
		salida = salida + lista_de_letras[i]
	if test == salida:
		print(test + " es palíndromo")
	else:
		print(test + " NO es palíndromo")


print("Verificar si una palabra es un palíndromo")
palabra = input("Ingrese una palabra: ")
palintromo(palabra)

