
print("Verificar si una palabra es un palíndromo")
print("Ingrese una palabra:")
palabra = input()
lista_de_letras = []
for i in range(len(palabra)):
	lista_de_letras.append(palabra[i])
lista_de_letras.reverse()
salida = ""
for i in range(len(lista_de_letras)):
	salida = salida + lista_de_letras[i]
if palabra == salida:
	print(palabra + " es palíndromo")
else:
	print(palabra + " NO es palíndromo")

