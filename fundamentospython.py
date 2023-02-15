#esto es un comentario

def nuevoTema(tema):
    print("\n===",tema,"===\n")


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
nuevoTema("Variables")
variable1=10
variable2=34.2
variable3="pepe"
variable4="hola"

print(nuevoTema,variable1,variable2,variable3,variable4)
nuevoTema("Enteros")
w=125
x=549848696
y=-345
z=0b0110011
h=0xffa #entero en hexadecimal

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))
nuevoTema("flotantes")
x=1652.5
y=0.0656652
print(x,type(x))
print(y,type(y))
nuevoTema("Numeros imaginarios")
x=-46j
y=12+45j
z=2j
print(x,type(x))
print(y,type(y))
print(z,type(z))

nuevoTema("Listas")
a=[10,20.5,"python list"]
print(a)
a=["lista2",46,16.3j]
print(a)

nuevoTema("Tuplas")
t=(25,"tupla",5.6)
print(t)
print(t[1])
t[0]="Modificado"
print(t)
nuevoTema("Conjuntos")
c={50,20,18,4,8,50}
print(c)
nuevoTema("Conjuntos")
d={1:"valor1","2":45}
print(d, type(d))



