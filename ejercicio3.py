


print("ejemplo: 2.5, que serian 2 minutos y 30 segundos")
duracion_de_cancion = float(input("Ingrese la duracion de la cancion en minutos: "))

if duracion_de_cancion >= 2.5 and duracion_de_cancion <= 4.5:
    print("La cancion es de una duracion aceptable")
else:
    print("La cancion es de una duracion no aceptable")


genero_musical = str(input("Ingrese el genero musical: "))
if genero_musical == "rock" or genero_musical == "pop" or genero_musical == "indie":
    print("El genero musical es aceptable")
else:
    print("El genero musical no es aceptable")



año_lanzamiento = int(input("Ingrese el año de lanzamiento: "))
if año_lanzamiento >= 2010:
    print("La fecha de lanzamiento es aceptable")
else:
    print("La fecha de lanzamiento no es aceptable")

if (2.5 <= duracion_de_cancion <= 4.5) and (genero_musical in ["rock", "pop", "indie"]) and (año_lanzamiento >= 2010):
    print("La cancion cumple con todos los requisitos y sera incluida en la playlist")
else:
    print("La cancion no cumple con todos los requisitos y no sera incluida en la playlist")