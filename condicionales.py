"""
condicionales if:
    evaluan expresiones booleanas

estructura:
    if expresion:
       instrecciones

     if expresion:
       instrucciones
    else:
        instrucciones

if expresion:
        instrucciones
elif expresion:
        instrucciones
    else:
        instruciones
 """

 print("programa que verfica si un numero es positivo")
 num = int(input("ingresa un numero:"))
 # preguntar el numero es mayor a 0:
 if num > 0:
 print("el numero es positivo")
else:
    print("el numero es negativo")
print("fin del programa")

print("programa que verificar si un numero es par")
num = int(input("ingresa un numero:"))
if num % 2 == 0:
    print("es un numero par")
 else:
    print("es un numero impar")
