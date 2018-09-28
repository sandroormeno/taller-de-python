import sys
# Elevar a la  potencia x a la y = x**y
# raiz cuadrada de x**0.5 --> (1/2)
hipotenusa = ((float(sys.argv[1])**2) + (float(sys.argv[2])**2))**0.5
print ("Hipotenusa:" + str(hipotenusa))