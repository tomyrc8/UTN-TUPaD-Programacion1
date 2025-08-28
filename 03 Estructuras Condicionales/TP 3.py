# ACTIVIDAD 1)✔ Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# edad = int(input ("Ingrese su edad: "))
# if edad>=18:
#     print("Es mayor de edad")



# ACTIVIDAD 2)✔ Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# nota = int(input("Ingrese la nota de su exámen: "))
# if nota>=6:
#     print("Aprobado")
# else:
#     print("Desaprobado")



# ACTIVIDAD 3)✔ Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla
# "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. 

# num = int (input("Ingrese un número par: "))
# if num % 2 == 0:
#     print ("Ha ingresado un número par")
# else:
#     print ("Por favor, ingrese un número par")



# ACTIVIDAD 4)✔ Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# edad = int (input ("Ingrese su edad: "))
# if edad < 12:
#     print("Niño/a")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto/a")



# ACTIVIDAD 5)✔- Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una 
# contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar 
# la cantidad de elementos que tiene un iterable tal como una lista o un string. 

# contraseña = input("Ingrese una contraseña: ")
# if len(contraseña)>=8 and len(contraseña)<=14:
#     print ("Ha ingresado una contraseña correcta")
# else:
#    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



# ACTIVIDAD 6)✔- El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: 
# from statistics import mode, median, mean 
# mi_lista = [1,2,5,5,3] 
# mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
# mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
# la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

# import random 
# from statistics import mode, median, mean 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# if mean(numeros_aleatorios) > median(numeros_aleatorios) > mode(numeros_aleatorios):
#     print ("Hay sesgo positivo o a la derecha")
# elif mean(numeros_aleatorios) < median(numeros_aleatorios) < mode(numeros_aleatorios):
#     print ("Hay sesgo negativo o a la izquierda")
# elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
#     print("Sin sesgo")  
# else:
#     print ("No se puede determinar un sesgo claro")
# print(f"Media: {mean(numeros_aleatorios)}, Mediana: {median(numeros_aleatorios)}, Moda: {mode(numeros_aleatorios)}")



# ACTIVIDAD 7)✔-- Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# texto = input("Escribí una palabra o frase: ")
# ultima_letra = texto[-1].upper()
# if (ultima_letra == "A" or ultima_letra == "E" or ultima_letra == "I" or ultima_letra == "O" or ultima_letra == "U"):
#     print(texto + "!")
# else: 
#     print(texto)


# ACTIVIDAD 8)✔- Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir 
# el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python 
# para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# numero = int(input("Ingrese el numero 1 si quiere su nombre en mayuscula, el numero 2 si quiere su nombre en minuscula o el numero 3 si quiere su nombre con la primera letra mayúscula: "))
# if numero==1:
#     print(nombre.upper())
# elif numero==2:
#      print(nombre.lower())
# elif numero==3:
#     print(nombre.title())
# else:
#     print ("El numero ingresado no es correcto")



# ACTIVIDAD 9)✔ Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

# magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto: "))
# if magnitud_terremoto < 3:
#     print ("Según la escala de Richter el terromoto es considerado `Muy Leve`, es decir, imperceptible.")
# elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
#      print ("Según la escala de Richter El terromoto es considerado `Leve`, es decir, ligeramente perceptible.")
# elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
#      print ("Según la escala de Richter el terromoto es considerado `Moderado`, es decir, sentido por personas, pero generalmente no causa daños.")
# elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
#      print ("Según la escala de Richter el terromoto es considerado `Fuerte`, es decir, puede causar daños en estructuras débiles.")
# elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
#      print ("Según la escala de Richter el terromoto es considerado `Muy Fuerte`, es decir, puede causar daños significativos.")
# else:
#      print ("Según la escala de Richter el terromoto es considerado `Extremo`, es decir, puede causar graves daños a gran escala.")



# ACTIVIDAD 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# Periodo del año: Desde el 21 de diciembre hasta el 20 de marzo (incluidos).
# Estación en el hemisferio norte: Invierno.
# Estación en el hemisferio sur: Verano.

# Periodo del año: Desde el 21 de marzo hasta el 20 de junio (incluidos).
# Estación en el hemisferio norte: Primavera
# Estación en el hemisferio sur: Otoño

# Periodo del año: Desde el 21 de junio hasta el 20 de septiembre (incluidos)
# Estación en el hemisferio norte: Verano
# Estación en el hemisferio sur: Invierno

# Periodo del año: Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)
# Estación en el hemisferio norte: Otoño
# Estación en el hemisferio sur: Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es 
# y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se 
# encuentra en otoño, invierno, primavera o verano. 

# hemisferio = input ("¿En qué hemisferio se encuentra? N/S: ").upper()
# mes = (input ("Indique el mes del año: ")).upper()
# dia = int(input("¿Qué día es? "))

# if hemisferio == "S":
#     if (mes == "DICIEMBRE") and  31>= dia >= 21:
#         print ("Es Verano")
#     elif (mes == "DICIEMBRE") and  21> dia >= 1:
#         print ("Es Primavera") 
#     elif (mes == "MARZO") and  31 >= dia >= 21:
#         print ("Es Otoño")
#     elif (mes == "MARZO") and  21> dia >= 1:
#         print ("Es Verano")    
#     elif (mes == "JUNIO") and 30 >= dia >= 21:
#         print ("Es Invierno")    
#     elif (mes == "JUNIO") and  21> dia >= 1:
#         print ("Es Otoño")
#     elif (mes == "SEPTIEMBRE") and 30 >= dia >= 21:
#         print ("Es Primavera")
#     elif (mes == "SEPTIEMBRE") and  21> dia >= 1:
#         print ("Es Invierno")
#     elif (mes == "ENERO" or  mes == "FEBRERO") and  dia <= 31:
#         print ("Es Verano")
#     elif (mes == "ABRIL" or  mes == "MAYO") and dia <= 31:
#         print ("Es Otoño")
#     elif (mes == "JULIO" or  mes == "AGOSTO") and dia <= 31:
#         print ("Es Invierno")
#     elif (mes == "OCTUBRE" or  mes == "NOVIEMBRE") and dia <= 31:
#         print ("Es Primavera")
#     else:
#         print ("Mes o dia inválido")

# if hemisferio == "N":
#     if (mes == "DICIEMBRE") and  31>= dia >= 21:
#         print ("Es Invierno")
#     elif (mes == "DICIEMBRE") and  21> dia >= 1:
#         print ("Es Otoño") 
#     elif (mes == "MARZO") and  31 >= dia >= 21:
#         print ("Es Primavera")
#     elif (mes == "MARZO") and  21> dia >= 1:
#         print ("Es Invierno")    
#     elif (mes == "JUNIO") and 30 >= dia >= 21:
#         print ("Es Verano")    
#     elif (mes == "JUNIO") and  21> dia >= 1:
#         print ("Es Primavera")
#     elif (mes == "SEPTIEMBRE") and 30 >= dia >= 21:
#         print ("Es Otoño")
#     elif (mes == "SEPTIEMBRE") and  21> dia >= 1:
#         print ("Es Verano")
#     elif (mes == "ENERO" or  mes == "FEBRERO") and  dia <= 31:
#         print ("Es Invierno")
#     elif (mes == "ABRIL" or  mes == "MAYO") and dia <= 31:
#         print ("Es Primavera")
#     elif (mes == "JULIO" or  mes == "AGOSTO") and dia <= 31:
#         print ("Es Verano")
#     elif (mes == "OCTUBRE" or  mes == "NOVIEMBRE") and dia <= 31:
#         print ("Es Otoño")
#     else:
#         print ("Mes o dia inválido")
# else:
#     print ("Hemisferio inválido")       