descuentoestudiante= (0.15)
descuentoclientefrecuente= (0.10)
estudiante=()
frecuente=()
precio=()



precio = input("Cual es el precio del articulo:")

estudiante = input("Usted es estudiante?:")
if "si" == estudiante:
    frecuente = input("Usted es cliente frecuente?:")
    if "si" == frecuente:
        precio = precio*descuentoclientefrecuente*descuentoestudiante
        print(precio)







        


