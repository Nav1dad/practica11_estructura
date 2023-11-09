
import ejercicio1

radio_circulo = 5
area_circulo = ejercicio1.area_circulo(radio_circulo)
perimetro_circulo = ejercicio1.perimetro_circulo(radio_circulo)

print(f'Círculo - Área: {area_circulo}, Perímetro: {perimetro_circulo}')

base_rectangulo = 4
altura_rectangulo = 6
area_rectangulo = ejercicio1.area_rectangulo(base_rectangulo, altura_rectangulo)
perimetro_rectangulo = ejercicio1.perimetro_rectangulo(base_rectangulo, altura_rectangulo)

print(f'Rectángulo - Área: {area_rectangulo}, Perímetro: {perimetro_rectangulo}')

base_triangulo = 3
altura_triangulo = 8
area_triangulo = ejercicio1.area_triangulo(base_triangulo, altura_triangulo)
perimetro_triangulo = ejercicio1.perimetro_triangulo(5, 7, 8)

print(f'Triángulo - Área: {area_triangulo}, Perímetro: {perimetro_triangulo}')
