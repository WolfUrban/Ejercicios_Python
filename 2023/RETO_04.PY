fibonacci=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,233,377,610,987]

def ValidarPrimo(numero):
    for i in range(2,int(numero)):
        if (int(numero)%i)==0:
            return "No es primo"
    return "Es primo"

def ValidarFibonacci(numero):
    if fibonacci.count(int(numero)):
        return "fibonacci"
    else:
        return "no es fibonacci"

def ValidarPar(numero):
    if int(numero)%2 ==0:
        return "Par"
    else:
        return "es impar"
    
text = input("Ingrese Numero: ")


par = ValidarPar(text)
primo = ValidarPrimo(text)
fibo = ValidarFibonacci(text)

print(f"{text} {primo}, {fibo} y {par}")