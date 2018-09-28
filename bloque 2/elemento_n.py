mi_lista = ["Sandro", "Renzo", "Malena", "Victor", "Rosa"]
print("Mi lista es :" + str(mi_lista))
print("¿qué índice quieres ver?")
n = input()
salida = mi_lista[int(n)]
print("El elemento " + str(n) + " de la lista es: " + salida)