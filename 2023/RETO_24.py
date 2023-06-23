abd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def CifrarCesar(texto,cuadrantee):
    palabraCesar = ""
    txt = str(texto).upper()
    for i in txt:
        if i in abd:
            indice = (abd.index(i) + int(cuadrantee)) % len(abd)
            palabraCesar += abd[indice]
    return palabraCesar

def DecifrarCesar(texto,cuadrantee):
    palabraCesar = ""
    txt = str(texto).upper()
    for i in txt:
        if i in abd:
            indice = (abd.index(i) + int(cuadrantee)) % len(abd)
            palabraCesar += abd[indice]
    return palabraCesar

palabraCESAR = input("Ingrese una palabra: ")
cuadrante = input("Ingrese cuadrante: ")


h = CifrarCesar(texto=palabraCESAR,cuadrantee= cuadrante)
g = CifrarCesar(texto=h,cuadrantee= -int(cuadrante))
print(h)
print(g)