mercosur = {"Arentina" : "Buenos Aires",
			"Brasil" : "Brasilia",
			"Paraguay": "Asunción",
			"Uruguay" : "Montevideo",
			"Venezuela" : "Caracas",
			"Bolivia" : "Sucre",
			"Chile" : "Santiago", 
			"Colombia": "Bogotá", 
			"Ecuador" : "Quito",
			"Perú": "Lima"}
paises = mercosur.keys()
print("Los paises del Mercosur son :" + str(paises))
print("¿Cuál es la capital de:?")
pais = input()
print("Capital de " + str(pais) + " es " + str(mercosur.get(pais)))