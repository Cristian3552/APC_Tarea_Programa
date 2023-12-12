#El proposito de este programa es resolver operaciones matematicas basicas y demostrar funciones de python que nos ayudan en la conversion de variables y contar la cantidad de letras de alguna frase
#Programa de Operaciones basicas y Tipos de datos
#Separacion
print("OPERACIONES BASICAS MATH")
#Suma
a = int(input("Numero 1:"))
b = int(input("Numero 2:"))
s = a+b
print("la suma es:",s)
#Resta
a = float(input("Numero 1:"))
b = float(input("Numero 2:"))
r = a-b
print("la resta es:",r)
#Multiplicacion
a = int(input("Numero 1:"))
b = int(input("Numero 2:"))
m = a*b
print("la multiplicacion es:",m)
#Division
a = float(input("Numero 1:"))
b = float(input("Numero 2:"))
d = a/b
print("la division es:",d)


###############################################################
#Separacion
print("MANIPULACION DE CADENAS DE TEXTO")
#Ejercicio 2 #Este programa tiene la finalidad de contar la cantidad de letras y mostrar el resultado en la variable X
c = "Cristian Lara Chacón"
#Eliminar los espacios y contar la longitud
x = len(c)
x1 = len(c.replace(" ", "",))
#Longitud de letras con espacios
print(x)
#Longitud de letras sin espacios
print(x1)


################################################################
#Ejercicio 3
print("CONVERSION DE TIPOS DE DATOS")
v = 20
b = 2.4
# De entero a flotante
print(v)
print(float(v))
# De Flotante a entero
print(b)
print(int(b))




