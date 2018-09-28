yo = {"Nombre": 0, "Distrito":0, "Mascota":0 }
print("Mi diccionario :" + str(yo))
print("Póngale su nombre :" )
nombre = input()
yo["Nombre"] = str(nombre)
print("Póngale su distrito :" )
distrito = input()
yo["Distrito"] = str(distrito)
print("Póngale su mascota :" )
mascota = input()
yo["Mascota"] = str(mascota)
print("Mi diccionario :" + str(yo))
print("Añada una clave :" )
clave = input()
mas = { str(clave): 0 }
print("Añada un valor a la clave :" )
valor = input()
mas[str(clave)] = str(valor)
yo.update(mas)
print("Mi diccionario :" + str(yo))





