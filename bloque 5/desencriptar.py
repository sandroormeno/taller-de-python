print("Programa para desencriptar un texto encriptado")
encriptado = 'l< q@+ m#s m+ -mp<rt#'
mi_texto= []
for i in encriptado:
    mi_texto.append(i)
#
origen = ["a", "e","i", "o", "u"]
clave = ["#", "+","-", "<", "@"]
#
desencriptado =[]
for i in encriptado:
    if i in  clave:
        #print(origen.index(i))
        desencriptado.append(origen[clave.index(i)])
    else:
        desencriptado.append(i)
#
salida = ""
for i in desencriptado:
    salida += i
print(salida)