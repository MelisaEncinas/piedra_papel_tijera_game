import random

def obtener_eleccion_usuario():
    """Obtiene y valida la elección del usuario."""
    opciones = ["piedra", "papel", "tijera"]
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in opciones:
        eleccion = input("Opción no válida. Por favor, elige de nuevo: ").lower()
    return eleccion

def obtener_eleccion_computadora():
    """Genera y devuelve la elección de la computadora."""
    opciones = ["piedra", "papel", "tijera"]
    eleccion = random.choice(opciones)
    print(f"Yo eligió: {eleccion}")
    return eleccion

def determinar_ganador(usuario, computadora):
    """Determina el ganador en base a las elecciones del usuario y la computadora."""
    if usuario == computadora:
        return "Es un empate!"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste. ¡Yo gané!"

def jugar():
    """Función principal para ejecutar el juego."""
    print("--- Bienvenido al juego Piedra, Papel o Tijera!---")
    opc_usuario = obtener_eleccion_usuario()
    opc_computadora = obtener_eleccion_computadora()
    resultado = determinar_ganador(opc_usuario, opc_computadora)
    print(resultado)

if __name__ == "__main__":
    jugar()
