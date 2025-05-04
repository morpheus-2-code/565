#Programa para convertir diferentes unidades de medida 


print("Bienvenido al convertidor de unidades")
print("1 para convertir de kilometros a millas")
print("2 para convertir de millas a kilometros")
print("3 para convertir de grados celsius a fahrenheit")
print("4 para convertir de fahrenheit a grados celsius")

convertir = int(input("Ingrese la opcion que desea: "))
if convertir == 1:
    
    kilometros = float(input("Ingrese la cantidad de kilometros: "))
    if kilometros < 0:
        print("La cantidad de kilometros no puede ser negativa")
    else:
        millas = kilometros * 0.621371
        print("La cantidad de millas es: ", millas)

elif convertir == 2:  

    millas = float(input("Ingrese la cantidad de millas: "))
    if millas < 0:
        print("La cantidad de millas no puede ser negativa")
    else:
        kilometros = millas / 0.621371
        print("La cantidad de kilometros es: ", kilometros)
elif convertir == 3:
    
    celsius = float(input("Ingrese la cantidad de grados celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    if fahrenheit <= 32:
        print("La cantidad de grados fahrenheit es: ", fahrenheit)
        print("La temperatura es fria")
    elif 68 <= fahrenheit <= 77:
        print("La cantidad de grados fahrenheit es: ", fahrenheit)
        print("La temperatura es templada")
    elif fahrenheit >= 97:
        print("La cantidad de grados fahrenheit es: ", fahrenheit)
        print("La temperatura es caliente")
    else:
        print("Error")
elif convertir == 4:
    fahrenheit = float(input("Ingrese la cantidad de grados fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    if celsius <= 0:
        print("La cantidad de grados celsius es: ", celsius)
        print("La temperatura es fria")
    elif 15 <= celsius <= 25:
        print("La cantidad de grados celsius es: ", celsius)
        print("La temperatura es templada")
    elif celsius >= 25:
        print("La cantidad de grados celsius es: ", celsius)
        print("La temperatura es caliente")
    else:
        print("Error")
else:
    print("Opcion no valida")




    