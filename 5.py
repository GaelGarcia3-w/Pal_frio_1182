print()
print("Edgar Gael Garcia Camacho 1182 3w :Pal_frio")
print()
def binario_a_entero(binario):
    try:
        return int(binario, 2)  
    except ValueError:
        raise ValueError("El valor ingresado no es un número binario válido.")

binario = input("Por favor, ingresa un número binario: ")

try:
    entero = binario_a_entero(binario)
    print(f"El número binario {binario} convertido a entero es: {entero}")
except ValueError as e:
    print(e)
