"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
1-6, 2-5 y 3-4.
* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
se mostrará el mensaje: "ERROR: número incorrecto.".
if expresiones 
        instrucciones 
else:
    instrucciones
"""
Else
'Calcular cara opuesta
Select Case resultado
Case 1
 caraOpuesta = 6
Case 2
  caraOpuesta = 5
 Case 3
 caraOpuesta = 4
 Case 4
caraOpuesta = 3
Case 5
caraOpuesta = 2
Case 6
caraOpuesta = 1
End Select
