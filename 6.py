print()
print("Edgar Gael Garcia Camacho 1182 3w :Pal_frio")
print()
def calcular_edad(anio_actual, anio_nacimiento):
    return anio_actual - anio_nacimiento

#Solicitar el año en curso
anio_actual = int(input("Ingresa el año en curso: "))

#Inicializar lista para almacenar la información
personas = []

#Solicitar datos de las tres personas
for i in range(3):
    print(f"\nPersona {i + 1}:")
    nombre = input("Ingresa el nombre: ")
    anio_nacimiento = int(input("Ingresa el año de nacimiento: "))
    edad = calcular_edad(anio_actual, anio_nacimiento)
    personas.append((nombre, edad))

#Imprimir los resultados
print("\nEdades durante el año en curso:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} años en {anio_actual}.")
