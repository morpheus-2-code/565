lista_de_libros = ["Los_tres_mosqueteros", "El_quijote", "La_iliada", "La_divina_comedia", "El_principe"]


print("Bienvenido a la biblioteca")
print("1 para ver los libros")
print("2 para agregar un libro")
print("3 para eliminar un libro")

ingresar = int(input("Ingrese la opcion que desea: ")) 


if ingresar == 1:
    print("Los libros son: ", lista_de_libros)
elif ingresar == 2:
    libro = input("Ingrese el nombre del libro: ")
    lista_de_libros.append(libro)
    print("El libro ha sido agregado")
    print("Los libros son: ", lista_de_libros)
elif ingresar == 3:
    libro = input("Ingrese el nombre del libro: ")
    if libro in lista_de_libros:
        lista_de_libros.remove(libro)
        print("El libro ha sido eliminado")
        print("Los libros son: ", lista_de_libros)
    else:
        print("El libro no se encuentra en la lista")
else:
    print("Opcion no valida")

if lista_de_libros == [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]:
    print("La lista de libros esta llena, prueba gratis")
else:
    print("La lista de libros no esta llena, prueba poner más libros")



