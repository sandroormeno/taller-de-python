print("Programa para encriptar una oración")
texto = 'lo que mas me importa'
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