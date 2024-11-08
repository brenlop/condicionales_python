"""
Escribe un programa que pida un número entero entre uno y doce e imprima el 
número de días que tiene el mes correspondiente.
 Si introducimos otro número nos da un error.
 if expresiones 
         instrucciones 
else:
    instrucciones 
"""
 Else
            'Mostrar días del mes
            Select Case mes
                Case 1, 3, 5, 7, 8, 10, 12
                    Console.WriteLine("El mes " & mes & " tiene 31 días.")
                Case 4, 6, 9, 11
                    Console.WriteLine("El mes " & mes & " tiene 30 días.")
                Case 2
                    Console.WriteLine("El mes " & mes & " tiene 28 días.")
            End Select
        End If

        Console.ReadKey()
    End Sub
End Module

