print()
print("Edgar Gael Garcia Camacho 1182 3w : Pal_frio")
print()
def mas_larga(palabras):
    if not palabras:
        raise ValueError("La lista no puede estar vacía.")
    palabra_mas_larga = palabras[0]  
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga


palabras = ["pollo", "polloloco", "pollolizto", "pollerialoscamperos"]
resultado = mas_larga(palabras)
print(f"La palabra más larga es: {resultado}")
