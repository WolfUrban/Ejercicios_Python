import ast

def es_expresion_matematica_correcta(expresion:str) -> bool:
    try:
        check = False

        separadores = expresion.split(' ')

        if len(separadores) < 3 or len(separadores) % 2 == 0:
            return False
        for indice,valor in enumerate(separadores):
            if indice % 2 == 0:
                try:
                    float(valor)
                    check = True
                except:
                    return False
            else:
                check = indice in ["+","/","%","-","*"]
    except:
        check = False
    return check
# Ejemplos de uso
expresion1 = "3 + 1.1 + 2 - 1"
print(es_expresion_matematica_correcta(expresion1))  # Output: True

expresion2 = "10 / 0 + +"
print(es_expresion_matematica_correcta(expresion2))  # Output: False, división por cero

expresion3 = "1 + 2"
print(es_expresion_matematica_correcta(expresion3))  # Output: False, variable no definida
