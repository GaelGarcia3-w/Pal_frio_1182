print()
print("Edgar gael Garcia Camacho 1182 3w:Pal_frio")
print()
def filtrar_palabras(palabras, n):
    if not palabras:
        raise ValueError("La lista de palabras no puede estar vacía.")
    if n < 0:
        raise ValueError("El número de caracteres debe ser un entero no negativo.")
    return [palabra for palabra in palabras if len(palabra) > n]


palabras = ["sol", "mariposa", "montaña", "cielo", "paz"]
n = 4
resultado = filtrar_palabras(palabras, n)
print(f"Palabras con más de {n} caracteres: {resultado}")

