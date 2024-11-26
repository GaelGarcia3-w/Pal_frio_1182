print()
print("Edgar gael Garcia Camacho 1182 3w:Pal_frio")
print()
def contar_mayusculas(cadena):
    mayusculas = 0
    for caracter in cadena:
        if caracter.isupper():  
            mayusculas += 1
    return mayusculas


cadena = input("Por favor, ingresa una cadena de texto: ")
cantidad_mayusculas = contar_mayusculas(cadena)


print(f"La cadena ingresada contiene {cantidad_mayusculas} letra(s) mayúscula(s).")
