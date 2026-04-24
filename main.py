def addmultiplenumbers(numbers):
    # Suma todos los números de la lista
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
    # Verifica si es entero y par
    if isinstance(num, int) and num % 2 == 0:
        return True
    else:
        return False

def isitaninteger(num):
    # Verifica si es entero
    return isinstance(num, int)

def main():
    print("¡Hola, bienvenido a tu calculadora mejorada!")
    # Ejemplo de uso interactivo
    lista = [2, 4, 6]
    print("Suma:", addmultiplenumbers(lista))
    print("Multiplicaciones:", multiplymultiplenumbers(lista))
    print("¿Es par 4?:", isiteven(4))
    print("¿Es entero 4.5?:", isitaninteger(4.5))

if __name__ == "__main__":
    main()
