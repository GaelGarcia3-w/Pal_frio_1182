print()
print("Edgar gael Garcia Camacho 1182 3w:Pal_frio")
print()
def es_bisiesto(anio):
    
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False


anio = int(input("Ingresa un año para verificar si es bisiesto: "))


if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")
