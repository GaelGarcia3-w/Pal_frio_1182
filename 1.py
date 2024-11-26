def max_in_list(numbers):
    if not numbers:
        raise ValueError("La lista no puede estar vacía.")
    return max(numbers)


numeros = [8, 14, 2, 23, 5]
resultado = max_in_list(numeros)
print(f"El número más grande es: {resultado}")
