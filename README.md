# Pal_frio_1182
Edgar Gael Garcia Camacho 3-W

# #1

print()

print("Edgar Gael Garcia Camacho 1182 3w :Pal frio")

print()

def max_in_list(numbers):
    
  if not numbers:
  
  raise ValueError("La lista no puede estar vacía.")

  return max(numbers)


numeros = [8, 14, 2, 23, 5]

resultado = max_in_list(numeros)

print(f"El número más grande es: {resultado}")

![image](https://github.com/user-attachments/assets/d85ee9cf-9c71-4180-a94c-544e623892be) ![image](https://github.com/user-attachments/assets/a98797bc-a661-41b4-8fd9-b1bbe5449776)

# #2

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

print(f"La palabra más larga es: {resultado}")**

![image](https://github.com/user-attachments/assets/9ea35e23-0921-4fdd-8aa3-3e11526779b9)

![image](https://github.com/user-attachments/assets/df28719a-353c-43c3-912e-8db301ab7df7)

# #3

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

![image](https://github.com/user-attachments/assets/299e52b8-bb63-4021-a892-a3f595715597) ![image](https://github.com/user-attachments/assets/447c68d8-7ff4-45d8-94e7-55ab446c6f37)

# #4

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

![image](https://github.com/user-attachments/assets/9723d54c-61c7-46f5-9bc8-95bbfe7b64f7) ![image](https://github.com/user-attachments/assets/d5a85def-d3a3-4167-b9ec-43b0b131c299)

# #5

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

![image](https://github.com/user-attachments/assets/f207ca47-afa1-4a92-9ea2-18ccf9d80931) ![image](https://github.com/user-attachments/assets/60a3af96-cab2-4726-b204-e0c5a1eb890d)

# #6

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

![image](https://github.com/user-attachments/assets/c8add8d8-535c-490c-9ec3-cc05c78197a7) ![image](https://github.com/user-attachments/assets/8d8fef60-bd91-4593-a397-2d5d791c8c8e)

# #7

print()

print("Edgar Gael Garcia Camacho 1182 3w:Pal_frio")

print()

#Solicitar edades al usuario

edades = tuple(int(input(f"Ingresa la edad de la persona {i + 1}: ")) for i in range(10))

#Contar las edades superiores a 20

cantidad_mayores_20 = sum(1 for edad in edades if edad > 20)

#Imprimir el resultado

print(f"La cantidad de personas con edades superiores a 20 es: {cantidad_mayores_20}")

![image](https://github.com/user-attachments/assets/73f1bd16-9b40-40f2-9b26-d21216cb3447) ![image](https://github.com/user-attachments/assets/4c49a0c8-725e-491b-873f-6a1b41d3dbce)

# #8

print()

print("Edgar Gael Garcia Camacho 1182 3:Pal_frio")

print()

#Definir una lista de nombres

nombres = ["Ana", "Luis", "Andrea", "Miguel", "Alberto", "Carla", "Álvaro", "Lucía"]

#Contar los nombres que comienzan con "a" o "A"

cantidad_con_a = sum(1 for nombre in nombres if nombre.lower().startswith("a"))

#Imprimir el resultado

print(f"La cantidad de nombres que comienzan con 'a' es: {cantidad_con_a}")

![image](https://github.com/user-attachments/assets/a9cdad9e-b43b-466c-a161-f62b1fe271f6) ![image](https://github.com/user-attachments/assets/08e79ba5-fac7-430a-8caf-7b065065a3da)

# #9


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
 
![image](https://github.com/user-attachments/assets/ab2d11d2-6802-407b-a22f-9cb2b0e2f0f6) ![image](https://github.com/user-attachments/assets/b611ef4c-cfed-4f65-a20b-aa046bb469d2)

 # #10

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

![image](https://github.com/user-attachments/assets/3dd245d4-5688-4cde-98b3-0f3e612ecd65) ![image](https://github.com/user-attachments/assets/a358ac77-ae4b-432a-a30e-03a8ffd67bb9) ![image](https://github.com/user-attachments/assets/040da9c5-5e78-49b1-a986-d81e24a20809)






