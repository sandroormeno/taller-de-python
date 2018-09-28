yo = {"Nombre": "Sandro", "Distrito": "LA Molina" , "Mascota":"lulu" }
print("Mi diccionario :" + str(yo))
print("Cuál clave quire borrar : "  + str(yo.keys()) )
clave_borrar = input()
yo. pop(clave_borrar)
print("Mi diccionario final:" + str(yo))

