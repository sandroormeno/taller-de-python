print("Programa que calcula el promedio de notas")
archivo = open("notas.csv", "r") 
promedios = {}
for line in archivo: 
	las_lineas = line
	los_datos = las_lineas.split(",")# split corta un string con un caracter "," 
	sumatoria = 0
	for i in range(1, len(los_datos)):
		sumatoria = sumatoria + int(los_datos[i])
	promedios[str(los_datos[0])] = sumatoria/(len(los_datos)-1)# -1 es para obtener el numero de notas
print(promedios)
for key in sorted(promedios, reverse=True): # reverse invierte el orden
    print (str(key) + " : " + str(promedios[key]))
