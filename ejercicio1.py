usuario="Nameless"
contraseña="1234"
usuario_ingresado=""
contraseña_ingresado=""

usuario_ingresado=input("Ingrese su nombre de usuario: ")
contraseña_ingresada=input("Ingrese su contraseña: ")

if usuario_ingresado==usuario and contraseña_ingresada==contraseña:
    print("Bienvenido al sistema")
elif usuario_ingresado==usuario and contraseña_ingresada!=contraseña:
    print("Contraseña incorrecta")
    print("Primer numero es 1")
elif usuario_ingresado != usuario and contraseña_ingresada != contraseña:
    print("Usuario y contraseña incorrectos")
