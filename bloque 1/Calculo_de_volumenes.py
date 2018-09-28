#import math
#math.pi
# de un circulo = pi*r**2
# volumen de cilindro = pi*r**2*altura
print("Para calcular el volumen de un cilindro")
print("introduzca el radio:")
radio = input()
print("introduzca la altura:")
altura = input()
print("altura:" + altura + "  radio:" + radio )
pi = 3.1415
volumen = float(radio)*float(altura)*2*pi
print ("Volumen: {0:.2f} m3" .format(volumen))