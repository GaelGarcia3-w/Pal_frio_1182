print()
print("Edgar Gael Garcia Camacho 1182 3:Pal_frio")
print()
#Definir una lista de nombres
nombres = ["Ana", "Luis", "Andrea", "Miguel", "Alberto", "Carla", "Álvaro", "Lucía"]

#Contar los nombres que comienzan con "a" o "A"
cantidad_con_a = sum(1 for nombre in nombres if nombre.lower().startswith("a"))

#Imprimir el resultado
print(f"La cantidad de nombres que comienzan con 'a' es: {cantidad_con_a}")
