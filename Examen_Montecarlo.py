
import math
import random


def punto_aleatorio(a, b):
    
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)
    return x, y


def en_elipse(x, y, a, b):
    
    return x * x / (a * a) + y * y / (b * b) <= 1


def en_hiperbola(x, y, c, d):
    
    return x * x / (c * c) - y * y / (d * d) >= 1


def leer_positivo(mensaje, tipo=float):
    
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un número positivo.")
        except ValueError:
            print("  Entrada inválida, escriba un número.")


def area_exacta_interseccion(a, b, c, d, pasos=200000):
    if c >= a:
        return 0.0
    h = (a - c) / pasos
    total = 0.0
    for i in range(pasos):
        x = c + (i + 0.5) * h
        y_elipse = b * math.sqrt(max(0.0, 1 - x * x / (a * a)))
        y_hiper  = d * math.sqrt(max(0.0, x * x / (c * c) - 1))
        total += 2 * min(y_elipse, y_hiper) * h
    return 2 * total


def main():
    print(" Área de la intersección Elipse-Hipérbola")
    a = leer_positivo("a (semieje de la elipse en x): ")
    b = leer_positivo("b (semieje de la elipse en y): ")
    c = leer_positivo("c (constante de la hipérbola, x): ")
    d = leer_positivo("d (constante de la hipérbola, y): ")
    n = leer_positivo("Cantidad de puntos aleatorios: ", int)

    
    puntos_elipse       = 0
    puntos_interseccion = 0

    for _ in range(n):
        x, y = punto_aleatorio(a, b)
        if en_elipse(x, y, a, b):
            puntos_elipse += 1
            if en_hiperbola(x, y, c, d):
                puntos_interseccion += 1

    
    if puntos_elipse == 0:
        print("\nNingún punto cayó en la elipse; use más puntos.")
        return

    
    area_elipse = math.pi * a * b
    area_mc     = area_elipse * puntos_interseccion / puntos_elipse
    pct_elipse  = puntos_interseccion / puntos_elipse * 100


    print("\nResultados")
    print(f"Puntos generados (rectangulo)             : {n}")
    print(f"Puntos dentro de la elipse                : {puntos_elipse}")
    print(f"Puntos en la interseccion elipse-hiperbola: {puntos_interseccion}")
    print(f"La interseccion representa el             : {pct_elipse:.2f}% del area de la elipse")

    print(f"\narea de la elipse (formula pi*a*b)        : {area_elipse:.4f}")
    print(f"Area aproximada de la interseccion (MC)   : {area_mc:.4f}")

    
    area_ref = area_exacta_interseccion(a, b, c, d)
    print(f"Area de referencia (integracion numerica) : {area_ref:.4f}")

    if area_ref > 0:
        error_pct = (area_mc - area_ref) / area_ref * 100
        signo = "MAYOR" if error_pct >= 0 else "MENOR"
        print(f"El area de Montecarlo es {abs(error_pct):.2f}% {signo} que la de referencia.")
    else:
        print("La hiperbola no se intersecta con la elipse (c >= a): area = 0.")


if __name__ == "__main__":
    main()
