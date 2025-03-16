## funcion simple
def saludar():
    print("hola")

saludar()

##funcion con parametros

def suma(a, b):
    resultado = a+b
    print("El resultado es: " + str(resultado))

suma(8, 13)

def datos(nom, apell, nac):
    print("tus datos son: {} {} {}".format(nom,apell,nac))

datos("fede", "bardo", "Argentino")

## funciones con argumentos

def suma(*args):
    resultado = 0
    for n in args:
        resultado = resultado + n
    print(str(resultado))

suma(5, 9, 3)
