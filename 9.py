print()
print("Edgar Gael Garcia Camacho 1182 3w:Pal_frio")
print()
def contar_vocales(palabra):
    
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    
    for letra in palabra.lower():  
        if letra in vocales: 
            vocales[letra] += 1  
    
    return vocales


palabra = input("Ingresa una palabra: ")


resultado = contar_vocales(palabra)


print(f"\nLa palabra '{palabra}' contiene:")
for vocal, cantidad in resultado.items():
    print(f"- {vocal}: {cantidad}")
