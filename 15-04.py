#print("hello world, welcome to Python")

#Pedir un nombre por consola y saludar!

#Python no necesita especificar el tipo de variable.

#nombre = input("Por favor, dígame su nombre: \n")
#print("Hola", nombre)
#entrada = ""

#entrada = input("Ingrese su nombre por favor : \n")

#print("Hola", entrada)

#entrada = int(input("Cuantos años tenes?? \n"))

#if entrada >= 18:
#   print("Acceso Autorizado")
#else:
#    print("Acceso Denegado")

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if i % 2== 0:
        print("el número", i, "es par")