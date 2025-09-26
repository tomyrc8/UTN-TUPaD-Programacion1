# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas. 

# ACTIVIDAD 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

# Lista con las notas de 10 estudiantes:
# notas = [1,4,8,9.5,6,7.5,5.5,10,8.5,2]

# # Cantidad de notas:
# cantidad_notas = len(notas)

# # Mostrar la lista completa de notas:
# print("Notas de los estudiantes:")
# for i in range (cantidad_notas):
#     print (notas[i])
    

# # Calcular el promedio:
# suma = 0
# suma = suma + notas[i]
# promedio = suma /cantidad_notas
# print (f"El promedio es igual a: {promedio}")

# # Encontrar la nota más alta y la más baja:
# maximo = notas[0]  # arranco suponiendo que la primera es la mayor
# minimo = notas[0]  # y también la menor
# for i in range(cantidad_notas):
#     if notas[i] > maximo:
#         maximo = notas[i]
#     if notas[i] < minimo:
#         minimo = notas[i]
# print("Nota más alta:", maximo)
# print("Nota más baja:", minimo)


# ACTIVIDAD 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

# Crear la lista y cargar 5 productos ingresados por el usuario:
# productos = []
# for i in range(5):
#     prod = input(f"Ingrese el producto {i+1}: ")
#     productos.append(prod)   # agrego cada producto a la lista

# # Mostrar la lista ordenada alfabéticamente:
# print("\nLista ordenada alfabéticamente:")

# # Usamos sorted() que devuelve una nueva lista ordenada:
# lista_ordenada = sorted(productos)
# for i in range(len(lista_ordenada)):
#     print(lista_ordenada[i])

# # Preguntar al usuario qué producto desea eliminar:
# eliminar = input("\nIngrese el producto que desea eliminar: ")

# # verificamos si el producto está en la lista original:
# if eliminar in productos:
#     productos.remove(eliminar)   # lo elimina de la lista
#     print("\nLista actualizada después de eliminar el producto:")
#     for i in range(len(productos)):
#         print(productos[i])
# else:
#     print(f"\nEl producto '{eliminar}' no se encuentra en la lista.")


# ACTIVIDAD 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

# import random

# # Generar lista con 15 números enteros al azar entre 1 y 100:
# numeros = []
# for i in range(15):
#     num = random.randint(1, 100)  # Número al azar entre 1 y 100
#     numeros.append(num) # Le digo que cada numero se vaya agregando a la lista "numeros"

# # Separar en listas de pares e impares:
# pares = []
# impares = []

# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         pares.append(numeros[i])     # si es par lo agrego a la lista de pares
#     else:
#         impares.append(numeros[i])   # si es impar lo agrego a la lista de impares

# # Mostrar la lista completa:
# print("Lista generada con 15 números al azar:")
# for i in range(len(numeros)):
#     print(numeros[i])

# # Mostrar los pares:
# print("Números pares:")
# for i in range(len(pares)):
#     print(pares[i])

# # Mostrar los impares:
# print("Números impares:")
# for i in range(len(impares)):
#     print(impares[i])

# # Mostrar cuántos números tiene cada lista:
# print("Cantidad de números pares:", len(pares))
# print("Cantidad de números impares:", len(impares))



# ACTIVIDAD 4) Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

# Lista inicial con valores repetidos:
# valores = [5, 2, 8, 5, 2, 9, 1, 8, 3, 9, 4]

# # Crear nueva lista sin elementos repetidos:
# valores_sin_repetidos = []

# for i in range(len(valores)):
#     if valores[i] not in valores_sin_repetidos:
#         valores_sin_repetidos.append(valores[i])  # agrego solo si no está aún

# # Mostrar lista original:
# print("Lista original:")
# for i in range(len(valores)):
#     print(valores[i])

# # Mostrar lista sin repetidos:
# print("\nLista sin elementos repetidos:")
# for i in range(len(valores_sin_repetidos)):
#     print(valores_sin_repetidos[i])


# # ACTIVIDAD 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# # • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# # • Mostrar la lista final actualizada. 

# # ACTIVIDAD 5

# # Lista inicial con nombres de 8 estudiantes:
# estudiantes = ["Ana", "Juan", "Luis", "María", "Pedro", "Lucía", "Sofía", "Tomás"]

# # Mostrar la lista inicial:
# print("Lista de estudiantes presentes:")
# for i in range(len(estudiantes)):
#     print(estudiantes[i])

# # Preguntar al usuario si quiere agregar o eliminar un estudiante:
# accion = input("\n¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

# if accion == "agregar":
#     nuevo = input("Ingrese el nombre del nuevo estudiante: ")
#     estudiantes.append(nuevo)   # agregamos el nuevo estudiante
#     print(f"\nSe agregó a {nuevo} a la lista.")

# elif accion == "eliminar":
#     eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
#     if eliminar in estudiantes:
#         estudiantes.remove(eliminar)  # eliminamos si está en la lista
#         print(f"\nSe eliminó a {eliminar} de la lista.")
#     else:
#         print(f"\nEl estudiante '{eliminar}' no se encuentra en la lista.")

# else:
#     print("\nOpción no válida. No se realizaron cambios.")

# # Mostrar la lista final actualizada:
# print("\nLista final de estudiantes:")
# for i in range(len(estudiantes)):
#     print(estudiantes[i])


# # ACTIVIDAD 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# # último pasa a ser el primero). 

# # Lista inicial con 7 números:
# numeros = [10, 20, 30, 40, 50, 60, 70]

# # Mostrar lista original:
# print("Lista original:")
# for i in range(len(numeros)):
#     print(numeros[i])

# # Rotar los elementos una posición a la derecha:
# # Guardamos el último elemento:
# ultimo = numeros[-1]

# # Movemos cada elemento una posición hacia la derecha:
# for i in range(len(numeros)-1, 0, -1):
#     numeros[i] = numeros[i-1]

# # Ponemos el último elemento en la primera posición:
# numeros[0] = ultimo

# # Mostrar lista después de rotar:
# print("\nLista después de rotar una posición a la derecha:")
# for i in range(len(numeros)):
#     print(numeros[i])


# # ACTIVIDAD 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# # semana. 
# # • Calcular el promedio de las mínimas y el de las máximas. 
# # • Mostrar en qué día se registró la mayor amplitud térmica. 

# # Matriz 7x2 con temperaturas mínimas y máximas de una semana:
# # Cada sublista representa un día: [mínima, máxima]:
# temperaturas = [
#     [15, 25],  # Lunes
#     [13, 22],  # Martes
#     [16, 27],  # Miércoles
#     [14, 24],  # Jueves
#     [12, 23],  # Viernes
#     [17, 28],  # Sábado
#     [15, 26]   # Domingo
# ]

# # Calcular promedio de mínimas y máximas:
# suma_min = 0
# suma_max = 0

# for i in range(len(temperaturas)):
#     suma_min += temperaturas[i][0]  # suma de mínimas
#     suma_max += temperaturas[i][1]  # suma de máximas

# promedio_min = suma_min / len(temperaturas)
# promedio_max = suma_max / len(temperaturas)

# print(f"Promedio de temperaturas mínimas: {promedio_min}")
# print(f"Promedio de temperaturas máximas: {promedio_max}")

# # Calcular el día con mayor amplitud térmica:
# # Amplitud térmica = máxima - mínima:
# mayor_amplitud = 0
# dia_mayor_amplitud = 0

# for i in range(len(temperaturas)):
#     amplitud = temperaturas[i][1] - temperaturas[i][0]
#     if amplitud > mayor_amplitud:
#         mayor_amplitud = amplitud
#         dia_mayor_amplitud = i  # guardamos el índice del día

# # Mostrar la información:
# dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# print(f"\nEl día con mayor amplitud térmica es {dias_semana[dia_mayor_amplitud]} con {mayor_amplitud}°C")


# # ACTIVIDAD 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# # • Mostrar el promedio de cada estudiante. 
# # • Mostrar el promedio de cada materia. 

# # Matriz 5x3: 5 estudiantes, 3 materias:
# # Cada sublista representa las notas de un estudiante en 3 materias
# notas = [
#     [8, 7, 9],   # Estudiante 1
#     [6, 8, 7],   # Estudiante 2
#     [9, 10, 8],  # Estudiante 3
#     [7, 6, 7],   # Estudiante 4
#     [8, 9, 6]    # Estudiante 5
# ]

# # Promedio de cada estudiante:
# print("Promedio de cada estudiante:")
# for i in range(len(notas)):
#     suma = 0
#     for j in range(len(notas[i])):
#         suma += notas[i][j]  # sumamos las notas del estudiante i
#     promedio = suma / len(notas[i])
#     print(f"Estudiante {i+1}: {promedio}")

# # Promedio de cada materia:
# print("\nPromedio de cada materia:")
# cantidad_materias = len(notas[0])
# for j in range(cantidad_materias):
#     suma_materia = 0
#     for i in range(len(notas)):
#         suma_materia += notas[i][j]  # sumamos las notas de la materia j
#     promedio_materia = suma_materia / len(notas)
#     print(f"Materia {j+1}: {promedio_materia}")

# # ACTIVIDAD 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# # • Inicializarlo con guiones "-" representando casillas vacías. 
# # • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# # • Mostrar el tablero después de cada jugada. 

# # Inicializar tablero 3x3 con "-":
# tablero = []
# for i in range(3):
#     fila = []
#     for j in range(3):
#         fila.append("-")   # cada casilla vacía
#     tablero.append(fila)

# # Función para mostrar el tablero:
# def mostrar_tablero(tab):
#     for i in range(len(tab)):
#         for j in range(len(tab[i])):
#             print(tab[i][j], end=" ")
#         print()  # salto de línea por fila

# # Mostrar tablero inicial:
# print("Tablero inicial:")
# mostrar_tablero(tablero)

# # Simulación de jugadas de dos jugadores:
# for turno in range(9):  # máximo 9 jugadas
#     jugador = "X" if turno % 2 == 0 else "O"
#     print(f"\nTurno del jugador {jugador}:")
    
#     # Pedir fila y columna (0, 1 o 2):
#     fila = int(input("Ingrese la fila (0-2): "))
#     columna = int(input("Ingrese la columna (0-2): "))
    
#     # Colocar ficha si la casilla está vacía:
#     if tablero[fila][columna] == "-":
#         tablero[fila][columna] = jugador
#     else:
#         print("Casilla ocupada, elija otra posición.")
#         continue  # repetir el turno
    
#     # Mostrar tablero actualizado:
#     mostrar_tablero(tablero)

# # ACTIVIDAD 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# # • Mostrar el total vendido por cada producto. 
# # • Mostrar el día con mayores ventas totales. 
# # • Indicar cuál fue el producto más vendido en la semana.

# # Matriz 4x7: 4 productos, 7 días:
# # Cada sublista representa un producto con ventas diarias:
# ventas = [
#     [10, 12, 8, 15, 9, 7, 11],  # Producto 1
#     [5, 7, 6, 8, 7, 5, 6],      # Producto 2
#     [20, 18, 22, 19, 21, 20, 23], # Producto 3
#     [12, 10, 11, 14, 13, 15, 12]  # Producto 4
# ]

# # Total vendido por cada producto:
# print("Total vendido por cada producto:")
# totales_producto = []  # guardamos los totales para usar después
# for i in range(len(ventas)):
#     total = 0
#     for j in range(len(ventas[i])):
#         total += ventas[i][j]
#     totales_producto.append(total)
#     print(f"Producto {i+1}: {total} unidades")

# # Total vendido por cada día:
# totales_dia = []
# for j in range(7):
#     suma_dia = 0
#     for i in range(len(ventas)):
#         suma_dia += ventas[i][j]
#     totales_dia.append(suma_dia)

# # Encontrar el día con mayores ventas totales:
# mayor_ventas = totales_dia[0]
# dia_mayor_ventas = 0
# for i in range(1, len(totales_dia)):
#     if totales_dia[i] > mayor_ventas:
#         mayor_ventas = totales_dia[i]
#         dia_mayor_ventas = i

# print(f"\nEl día con mayores ventas totales fue el día {dia_mayor_ventas+1} con {mayor_ventas} unidades")

# # Producto más vendido en la semana:
# mayor_producto = totales_producto[0]
# indice_producto = 0
# for i in range(1, len(totales_producto)):
#     if totales_producto[i] > mayor_producto:
#         mayor_producto = totales_producto[i]
#         indice_producto = i

# print(f"El producto más vendido en la semana fue el Producto {indice_producto+1} con {mayor_producto} unidades")
