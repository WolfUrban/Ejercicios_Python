def obtener_puntuacion(puntos):
    if puntos == 0:
        return "Love"
    elif puntos == 1:
        return 15
    elif puntos == 2:
        return 30
    elif puntos == 3:
        return 40
    else:
        return "Deuce"


def determinar_ganador(juego):
    puntuacion_p1 = 0
    puntuacion_p2 = 0

    for punto in juego:
        if punto == "P1":
            puntuacion_p1 += 1
        elif punto == "P2":
            puntuacion_p2 += 1

        if puntuacion_p1 >= 4 and puntuacion_p1 - puntuacion_p2 >= 2:
            return "Ha ganado el P1"
        elif puntuacion_p2 >= 4 and puntuacion_p2 - puntuacion_p1 >= 2:
            return "Ha ganado el P2"

        if puntuacion_p1 >= 3 and puntuacion_p2 >= 3:
            if puntuacion_p1 == puntuacion_p2:
                return "Deuce"
            elif puntuacion_p1 > puntuacion_p2:
                return "Ventaja P1"
            else:
                return "Ventaja P2"

        print(f'{obtener_puntuacion(puntuacion_p1)} - {obtener_puntuacion(puntuacion_p2)}')

    return "El juego no ha finalizado"

# Ejemplo de uso
secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
resultado = determinar_ganador(secuencia)
print(resultado)
