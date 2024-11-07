"""
La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
if expresiones
        instrucciones
else:
    instrucciones
    """
If duracionLlamada <= 5 Then
costo Llamada = duracionLlamada * 1
ElseIf duracionLlamada <= 8 Then
 costo Llamada = 5 + (duracionLlamada - 5) * 0.8
 ElseIf duracionLlamada <= 10 Then
costo Llamada = 5 + 3 * 0.8 + (duracionLlamada - 8) * 0.7
 Else
  costo Llamada = 5 + 3 * 0.8 + 2 * 0.7 + (duracionLlamada - 10) * 0.5