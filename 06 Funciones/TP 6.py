# ACTIVIDAD 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Creacion de funcion:
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# Programa Principal:
# imprimir_hola_mundo()

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y 
# devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá 
# devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al 
# usuario.

# Creacion de funcion:
# def saludar_usuario(nombre):
#     return f"Hola {nombre}!"

# Programa Principal:
# nombre = input ("Ingrese su nombre: ")
# saludo = saludar_usuario(nombre)
# print(saludo)

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que 
# reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Creacion de funcion:
# def informacion_personal(nombre, apellido, edad, residencia):
#     print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa Principal:
# nombre = input ("Ingrese su nombre: ")
# apellido = input ("Ingrese su apellido: ")
# edad = int(input ("Ingrese su edad: "))
# residencia = input ("Ingrese su residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
# devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar 
# los resultados.

# import math
# Creacion de funcion:
# def calcular_area_circulo(radio):
#     return math.pi*radio*radio

# def calcular_perimetro_circulo(radio):
#     return 2*math.pi*radio

# Programa Principal:
# radio = float(input ("Ingrese el radio de una circunferencia: "))
# print(f"El área del círculo es: {calcular_area_circulo(radio)}")
# print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos 
# como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y 
# mostrar el resultado usando esta función

# Creacion de funcion:
# def segundos_a_horas(segundos):
#     return (segundos/3600)

# Programa Principal:
# segundos = float(input ("Ingrese la cantidad de segundos que quiere convertir en horas: "))
# print (f"La cantidad de segundos ingresada equivale a {segundos_a_horas(segundos)} horas.")

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro
# y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y 
# llamar a la función.

# Creacion de funcion:
# def tabla_multiplicar(numero):
#     print(f"Tabla de multiplicar del {numero}:")
#     for i in range (1,11):
#         print (f"{numero} x {i} = {numero * i}.")

# Programa Principal:
# numero = int(input ("Ingrese un número: "))
# tabla_multiplicar(numero)

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los 
# resultados de forma clara.

# Creacion de funcion:
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b
#     return (suma, resta, multiplicacion,division)

# Programa Principal:
# a = float (input ("Ingrese un número: "))
# b = float (input ("Ingrese otro número: "))
# resultados = operaciones_basicas(a, b)
# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicación: {resultados[2]}")
# print(f"División: {resultados[3]}")

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y 
# la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y 
# llamar a la función para mostrar el resultado con dos decimales.

# Creacion de funcion:
# def calcular_imc(peso, altura):
#     return peso / (altura * altura)

# Programa Principal:
# peso = float (input("Ingrese su peso corporal en kg: "))
# altura = float (input("Ingrese su altura en metros: "))
# imc = calcular_imc(peso, altura)
# print (f"El IMC de la persona es: {imc:.2f} kg/m².")

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en 
# grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y 
# mostrar el resultado usando la función.

# Creacion de funcion:
# def celsius_a_fahrenheit(celsius):
#     return celsius * (9 / 5) + 32

# Programa Principal:
# celsius = float (input("Ingrese una temperatura en grados celcius: "))
# conversion = celsius_a_fahrenheit(celsius)
# print (f"La temperatura ingresada en grados celsius equivale a {conversion}° fahrenheit.")

#-----------------------------------------------------------------------------------------------------
# ACTIVIDAD 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como 
# parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado 
# usando esta función.

# Creacion de funcion:
# def calcular_promedio(a, b, c):
#     return (a + b + c) / 3

# Programa Principal:
# a = float(input("Ingrese un primer número: "))
# b = float(input("Ingrese un segundo número: "))
# c = float(input("Ingrese un tercer número: "))
# promedio = calcular_promedio(a, b, c)
# print (f"El promedio de los números ingresados es igual a: {promedio}.")
