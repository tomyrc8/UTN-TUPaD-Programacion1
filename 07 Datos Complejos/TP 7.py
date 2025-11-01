# # ACTIVIDAD 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800

# precios_frutas["Banana"] = 1330
# precios_frutas["Manzana"] = 1700
# precios_frutas["Melón"] = 2800
# print(precios_frutas)

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

# frutas_sin_precios = ["Banana", "Ananá", "Melón", "Uva", "Naranja", "Manzana", "Pera"]

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


# def numeros_telefonicos():
#     # Se crea un diccionario vacío para guardar los contactos
#     lista_numeros_telefonicos = {}
#     # Se cargan los 5 contactos
#     for i in range(5):
#         nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
#         telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
#         lista_numeros_telefonicos[nombre] = telefono
#     # Se consulta por un nombre en particular
#     consulta = input("Ingrese el nombre que desea buscar: ")
#     # Se muestra el contacto por pantalla si es que existe
#     if consulta in lista_numeros_telefonicos:
#         print(f"El número de {consulta} es: {lista_numeros_telefonicos[consulta]}")
#     else:
#         print(f"No se encontró el contacto '{consulta}'.")
# numeros_telefonicos()

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

# Pedimos la frase al usuario
# frase = input("Ingrese una frase: ")
# # Separamos las palabras
# palabras = frase.split()
# # Usamos un set para obtener las palabras únicas
# palabras_unicas = set(palabras)
# # Creamos un diccionario para contar las repeticiones
# recuento = {}
# for palabra in palabras:
#     if palabra in recuento:
#         recuento[palabra] += 1
#     else:
#         recuento[palabra] = 1
# # Mostramos los resultados
# print("Palabras únicas:", palabras_unicas)
# print("Recuento:", recuento)

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

# alumnos = {}

# # Cargar los datos de 3 alumnos
# for i in range(3):
#     nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
#     n1 = float(input("Ingrese la primera nota: "))
#     n2 = float(input("Ingrese la segunda nota: "))
#     n3 = float(input("Ingrese la tercera nota: "))
    
#     # Guardamos las notas en una tupla
#     notas = (n1, n2, n3)
#     alumnos[nombre] = notas

# # Mostramos el promedio de cada alumno
# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"El promedio de {nombre} es: {promedio:.2f}")

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Conjuntos de estudiantes que aprobaron cada parcial
# parcial1 = {1, 2, 3, 4, 5}
# parcial2 = {4, 5, 6, 7}

# # Estudiantes que aprobaron ambos parciales (intersección)
# ambos = parcial1 & parcial2

# # Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
# solo_uno = parcial1 ^ parcial2

# # Estudiantes que aprobaron al menos uno (unión)
# al_menos_uno = parcial1 | parcial2

# # Mostramos los resultados
# print("Aprobaron ambos parciales:", ambos)
# print("Aprobaron solo uno de los dos:", solo_uno)
# print("Aprobaron al menos uno:", al_menos_uno)

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.

# Diccionario con productos y su stock inicial
# stock = {
#     "manzanas": 10,
#     "bananas": 5,
#     "naranjas": 8
# }

# # Mostramos el stock actual
# print("Stock actual:")
# for producto, cantidad in stock.items():
#     print(f"{producto}: {cantidad}")

# # Consultar producto
# producto = input("\nIngrese el nombre del producto que desea consultar: ").lower()

# # Si el producto existe en el diccionario
# if producto in stock:
#     print(f"El stock actual de {producto} es: {stock[producto]}")
    
#     # Preguntar si quiere agregar unidades
#     opcion = input("¿Desea agregar unidades? (s/n): ").lower()
#     if opcion == "s":
#         cantidad = int(input("Ingrese la cantidad a agregar: "))
#         stock[producto] += cantidad
#         print(f"Stock actualizado de {producto}: {stock[producto]}")

# # Si el producto no existe, se puede agregar
# else:
#     print(f"El producto '{producto}' no existe.")
#     opcion = input("¿Desea agregarlo al inventario? (s/n): ").lower()
#     if opcion == "s":
#         cantidad = int(input("Ingrese la cantidad inicial: "))
#         stock[producto] = cantidad
#         print(f"Producto '{producto}' agregado con {cantidad} unidades.")

# # Mostrar el stock final
# print("\nStock final actualizado:")
# for producto, cantidad in stock.items():
#     print(f"{producto}: {cantidad}")


#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora. 

# Diccionario donde las claves son tuplas (día, hora)
# agenda = {
#     ("lunes", "09:00"): "Reunión con el equipo",
#     ("martes", "14:00"): "Clase de programación",
#     ("miércoles", "10:30"): "Visita al cliente",
# }

# # Mostrar la agenda completa
# print("AGENDA SEMANAL:")
# for clave, evento in agenda.items():
#     print(f"{clave[0].capitalize()} a las {clave[1]} -> {evento}")

# # Consultar un día y hora
# print("\n--- CONSULTAR EVENTO ---")
# dia = input("Ingrese el día: ").lower()
# hora = input("Ingrese la hora (formato hh:mm): ")

# # Crear la tupla para buscar
# clave_busqueda = (dia, hora)

# # Verificar si existe un evento en esa fecha y hora
# if clave_busqueda in agenda:
#     print(f"\nEl evento agendado el {dia} a las {hora} es: {agenda[clave_busqueda]}")
# else:
#     print(f"\nNo hay ningún evento agendado el {dia} a las {hora}.")


#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

# Diccionario original: país → capital
# paises = {
#     "Argentina": "Buenos Aires",
#     "Brasil": "Brasilia",
#     "Chile": "Santiago",
#     "Uruguay": "Montevideo",
#     "Paraguay": "Asunción"
# }

# print("Diccionario original (País → Capital):")
# for pais, capital in paises.items():
#     print(f"{pais} → {capital}")

# # Crear un nuevo diccionario con las capitales como claves
# capitales = {capital: pais for pais, capital in paises.items()}

# print("\nDiccionario invertido (Capital → País):")
# for capital, pais in capitales.items():
#     print(f"{capital} → {pais}")