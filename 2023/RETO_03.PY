import random
import string



choice_Mayuscula = input("Contraseña con mayuscula? SI/NO: ").upper()
choice_Numeros = input("Contraseña con Numeros? SI/NO: ").upper()
choice_Simbolos = input("Contraseña con Simpolos especiales? SI/NO: ").upper()

caracteres = string.ascii_letters + string.digits + string.punctuation

hola = ""
for i in range(0,12):
    if choice_Mayuscula == "SI" and choice_Numeros == "SI" and choice_Simbolos == "SI":
        hola += random.choice(caracteres)
    elif choice_Mayuscula == "SI" and choice_Numeros == "SI" and choice_Simbolos == "NO":
        hola += random.choice(string.ascii_letters+string.digits)
    elif choice_Mayuscula == "SI" and choice_Numeros == "NO" and choice_Simbolos == "NO":
        hola += random.choice(string.ascii_letters)
    elif choice_Mayuscula == "SI" and choice_Numeros == "NO" and choice_Simbolos == "SI":
        hola += random.choice(string.ascii_letters+string.punctuation)        
    elif choice_Mayuscula == "NO" and choice_Numeros == "SI" and choice_Simbolos == "NO":
        hola += random.choice(string.digits)
    elif choice_Mayuscula == "NO" and choice_Numeros == "SI" and choice_Simbolos == "SI":        
        hola += random.choice(string.digits+string.punctuation)
    elif choice_Mayuscula == "NO" and choice_Numeros == "NO" and choice_Simbolos == "SI":
        hola += random.choice(string.punctuation)
    else:
        print("Debe seleccionar una opcion valida")
        break


print("Su Contraseña es: "+hola)
