#print("hola")
#entrada = ""
#print(entrada)

#entrada = input("Ingrese su nombre por favor: \n")
#print(entrada)

#entrada = int(input("Cuantos años tienes ??\n"))
#print(entrada)

#print("Tienes", entrada, "años y el año que viene vas a tener", int(entrada)+1)

#if entrada >=18:
#    print("Puedes pasar")
#else:
#    print("No puedes pasar")
numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numeros)):
    if i % 2 ==0:
        print("El número", i, "es número par")
    else:
        print("El número", i, "es número impar")