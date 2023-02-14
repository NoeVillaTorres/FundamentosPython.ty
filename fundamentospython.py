#esto es un comentario


if __name__=="__main__":
    print("=== Operadores aritmeticos====")
    print("operador de división entera (10//3): ",10//3)
    print("operador de potencias (5 ** 5 ): ",5 ** 5)
    print("operador cambio de signo (-5): ",-5)

    print("=== Operadores lógicos====")
    print("operador and (true and false):)",True and False)

#mostrar las tablas de verdad con operadores logicos

print("Tablas de verdad")

print("(true and True):)",True and True)
print("(true and false):)",True and False)
print("(false and True):)",False and True)
print("(false or false):)",False and False)

print("(true or true):)",True or True)
print("(true or false):)",True or False)
print("(false or false):)",False or False)
print("(false or true):)",True or False)

print("(true not true):)", not False)
print("(false not false):)",not True)

def nuevoTema(tema):
    print("\===Nuevo tema===/")

    nuevoTema("Variables")
    variable1=10
    variable2=34.2
    variable3="pepe"
    variable4="hola"

    print(variable1,variable2,variable3,variable4)
    