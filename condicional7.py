"""
Realiza un programa que calcule la potencia, para ello pide por teclado 
la base y el exponente. Pueden ocurrir tres cosas:
El exponente sea positivo, sólo tienes que imprimir la potencia.
 El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
if expresiones 
        instrucciones
else:
    instrucciones
"""
base = float(input("ingrese la base:"))
exponente =int(input("ingrese el exponente:"))
if exponente > 0:
    resultado = base **exponente
    print(f"el resutado es:{resultado}")
elif exponente == 0:
print("el resultado es:1")
else:
resultado =1/(base **(- exponente))
print(f"el resultad es:{resutado}")
