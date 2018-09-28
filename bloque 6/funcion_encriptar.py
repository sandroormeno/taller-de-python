
def encriptar(texto):
	mi_texto= []
	for i in texto:
	    mi_texto.append(i)
	#
	origen = ["a", "e","i", "o", "u"]
	clave = ["#", "+","-", "<", "@"]
	#
	encriptado =[]
	for i in mi_texto:
	    if i in  origen:
	        #print(origen.index(i))
	        encriptado.append(clave[origen.index(i)])
	    else:
	        encriptado.append(i)
	#
	salida = ""
	for i in encriptado:
	    salida += i
	print(salida)
#
#
#
print("Programa para encriptar una oración")
pa_encriptar = input("Ingrese una oración: ")
encriptar(pa_encriptar)