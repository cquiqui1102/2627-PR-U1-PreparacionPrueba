# Desarrolla un programa que en Python que solicite dos números decimales y muestre el resultado de las cuatro operaciones aritméticas básicas:
# suma, resta, multiplicación y división.

def sumar(numero1: float, numero2: float) -> float:
    suma: float= numero1 + numero2
    return suma


def restar(numero1: float, numero2: float) -> float:
    resta: float= numero1 - numero2
    return resta


def multiplicar(numero1: float, numero2: float) -> float:
    multiplicacion: float= numero1 * numero2
    return multiplicacion


def dividir(numero1: float, numero2: float) -> float:    
    if numero2 != 0:
        division = numero1 / numero2
        return division
    else:
        return "no válida"

def main():
    """Función principal"""

    # Entrada
    numero1 = float(input("Introduzca un primer número: "))
    numero2 = float(input("Introduzca un segundo número: "))

    # Salida
    print(f"Los cálculos con los siguientes números ({numero1} y {numero2}) son: ")
    print(f"Suma: {sumar(numero1, numero2)}")
    print(f"Resta: {restar(numero1, numero2)}")
    print(f"Multiplicación: {multiplicar(numero1, numero2)}")
    print(f"División: {dividir(numero1, numero2)}")
    
if __name__ == "__main__":
    main()