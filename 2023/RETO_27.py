import time
def CuentaAtras(intervalo,numero):
    while numero > 0:
        print(numero)
        time.sleep(intervalo)
        numero -= 1

validarNumero = True
while validarNumero is not False:
    i = input("Ingrese Intervalo: ")
    Cuenta = input("Ingrese Cuenta: ")
    if i.isnumeric() and int(i) > 0:
        validarNumero = False
        CuentaAtras(int(i),int(Cuenta))
    else:
        print("Debe ingresar un valor valido")