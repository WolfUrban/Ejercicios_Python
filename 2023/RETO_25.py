import keyboard
import sys ,os

comandoKONAMI =["flecha arriba","flecha arriba","flecha abajo","flecha abajo","flecha izquierda","flecha derecha","flecha izquierda","flecha derecha","b","a"]
comandoENTRADA = []
def on_key_press(event):
    if event.name == "enter":
        if comandoKONAMI == comandoENTRADA:
            print("comando konaim CORRECTO!!, para salir de la aplicacion presione 'esc' o vuelva a probar")
            comandoENTRADA.clear()
        else:
            os.system("cls")
            print(comandoENTRADA)
            print("Comando ingresado incorrecto, vuelva a ingresar el comando")
            comandoENTRADA.clear()
    else:
        print("Tecla presionada: {}".format(event.name))
        comandoENTRADA.append(event.name)

keyboard.on_press(on_key_press)

print(".......Prueba de Comando Konami..........")
# Mantén el programa en ejecución
keyboard.wait('esc')