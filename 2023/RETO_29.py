def CaracterCifrado(palabra1 : str,palabra2 : str):
    # Verificamos si alguna de las palabras está vacía
    if not palabra1 or not palabra2:
        print("Los argumentos no pueden estar vacíos")
        return
    
    listResultado = []
    separadorUno = list(palabra1)
    separadorDos = list(palabra2)
    
    # Verificamos si las palabras tienen la misma longitud
    if len(separadorUno) != len(separadorDos):
        print("Las palabras tienen que contener el mismo largo")
        return
    
    for indice,valor in enumerate(separadorDos):        
        if valor != separadorUno[indice]:
            listResultado.append(valor)
    
    print(listResultado)

CaracterCifrado("","");