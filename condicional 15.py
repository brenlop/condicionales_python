"""
Juego Piedra Papel y Tijera
 Programa que lea las opciones de 2 jugadores, y muestra el resultado
 Empate, gana jugador 1 o gana jugador 2
 Si introducimos una opción que no coindica con piedra, papel o tijera
 Diga que opción Incorrecta
 if expresiones 
         instrucciones 
else:
    instrucciones
"""
Sub Main()
        'Declaración de variables
        Dim jugador1, jugador2 As String
        Dim opciones() As String = {"Piedra", "Papel", "Tijera"}
        Dim resultados(,) As String = {{"Empate", "Gana Jugador 2", "Gana Jugador 1"}, _
                                        {"Gana Jugador 1", "Empate", "Gana Jugador 2"}, _
                                        {"Gana Jugador 2", "Gana Jugador 1", "Empate"}}

        'Pedir opciones de los jugadores
        Console.Write("Jugador 1, ingrese su opción (Piedra, Papel, Tijera): ")
        jugador1 = Console.ReadLine()
        Console.Write("Jugador 2, ingrese su opción (Piedra, Papel, Tijera): ")
        jugador2 = Console.ReadLine()
        


