print()
print("Edgar Gael Garcia Camacho 1182 3w:Pal_frio")
print()
#Solicitar edades al usuario
edades = tuple(int(input(f"Ingresa la edad de la persona {i + 1}: ")) for i in range(10))

#Contar las edades superiores a 20
cantidad_mayores_20 = sum(1 for edad in edades if edad > 20)

#Imprimir el resultado
print(f"La cantidad de personas con edades superiores a 20 es: {cantidad_mayores_20}")
