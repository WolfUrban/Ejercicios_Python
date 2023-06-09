

palabraUno = input("Ingrese la 1ra palabra:")

palabraDos = input("Ingrese la 2da palabra:")

def ValidarPalabra(Valor1,Valor2):

    if Valor1 == Valor2:
        return "No se puede Usar las mismas Palabras"

    if len(Valor1) != len(Valor2):        
        return False
    
    caracteresPalabra1 = list(Valor1)
    caracteresPalabra2 = list(Valor2)

    caracteresPalabra1.sort()
    caracteresPalabra2.sort()

    return caracteresPalabra1 == caracteresPalabra2


print(ValidarPalabra(palabraUno,palabraDos))
