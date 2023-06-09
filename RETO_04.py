class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
def calcular_area_poligono(poligono):
    tipo_poligono = type(poligono).__name__
    
    if tipo_poligono == 'Triangulo':
        base = poligono.base
        altura = poligono.altura
        area = (base * altura) / 2
    elif tipo_poligono == 'Cuadrado':
        lado = poligono.lado
        area = lado * lado
    elif tipo_poligono == 'Rectangulo':
        base = poligono.base
        altura = poligono.altura
        area = base * altura
    else:
        raise ValueError("Polígono no soportado.")
    
    return area

triangulo = Triangulo(5, 3)
area_tri = calcular_area_poligono(triangulo)
print("Área del triángulo:", area_tri)

cuadrado = Cuadrado(4)
area_cuad = calcular_area_poligono(cuadrado)
print("Área del cuadrado:", area_cuad)

rectangulo = Rectangulo(6, 8)
area_rect = calcular_area_poligono(rectangulo)
print("Área del rectángulo:", area_rect)