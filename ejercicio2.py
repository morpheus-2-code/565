descuento_estudiante = (0.15)
descuento_cliente_frecuente = (0.10)
estudiante = ()
frecuente = ()
precio = ()
precio_final=()

print("Ingrese solo numeros")
precio = float(input("Cual es el precio del articulo:"))


estudiante = input("Usted es estudiante?:").lower() #para que el "si" lo tenga como minuscula
if estudiante == "si":
    frecuente = input("Usted es cliente frecuente?:").lower() #lo mismo que en la linea 9
    if frecuente == "si":
        precio_final = precio * (1 - (descuento_estudiante))
        print("El precio final es:", precio_final)
        print("El descuento es:", (descuento_estudiante)*100, "%")
        print("El precio sin descuento es:", precio)
    elif frecuente == "no":
        precio_final = precio * (1 - descuento_estudiante)
        print("El precio final es:", precio_final)
        print("El descuento es:", descuento_estudiante*100, "%")
        print("El precio sin descuento es:", precio)
    else:
        print("Opcion no valida")
elif estudiante == "no":
    frecuente = input("Usted es cliente frecuente?:").lower()
    if frecuente == "si":
        precio_final = precio * (1 - descuento_cliente_frecuente)
        print("El precio final es:", precio_final)
        print("El descuento es:", descuento_cliente_frecuente*100, "%")
        print("El precio sin descuento es:", precio)
    elif frecuente == "no":
        precio_final = precio
        print("El precio final es:", precio_final)
        print("No tiene descuento")
    else:
        print("Opcion no valida")
else: #si se pone algo diferente a lo que se dice sale esto menos en el de pedir precio
    print("Opcion no valida")
   
    
    
 