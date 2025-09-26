# ACTIVIDAD 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

# num = 0 # Se inicializa la variable num en 0
# while num <= 100: # Se crea un ciclo while donde, si num es menor o igual a 100, se cumpla la instruccion siguiente.
#     print (num) # Se pide mostrar por pantalla el valor de num en el momento.
#     num = num+1 # A ese valor de num se le suma 1 y se guarda nuevamente en la variable num para volver a iniciar el ciclo hasta que "num" sea mayor que 100.


# ACTIVIDAD 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

# num = int(input("Ingrese un número entero: ")) # Se le pide un numero entero al usuario.
# if num == 0: # Por si el número es 0 se guarda en la variable "cant_digitos" que el numero ingresado tenga 1 digito.
#     cant_digitos = 1 
# else:
#     cant_digitos = 0 # De lo contrario, es decir si el número no es cero, se arrancca con el contador de digitos en 0. 
#     num = abs(num)  # Por si el numero ingresado es negativo se usa abs(num) para trabajar solo con el valor positivo.
#     while num > 0: # Mientras num sea mayor que 0, seguimos dividiendo.
#         num = num // 10   # Cada vez que divido entre 10 (división entera //), se borra un dígito.
#         cant_digitos += 1 # Al mismo tiempo, sumo 1 al contador (cant_digitos)
# print("La cantidad de dígitos es:", cant_digitos) # Cuando el bucle termina, el contador guarda cuántos dígitos tenía el número


# ACTIVIDAD 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

# Pedir dos números al usuario:
# num1 = int(input("Ingrese el primer número: ")) 
# num2 = int(input("Ingrese el segundo número: "))
# # Asegurar que num1 sea el menor y num2 el mayor:
# if num1 > num2: 
#     num1, num2 = num2, num1
# # Se inicializa la variable "suma" en 0:
# suma = 0
# # Se recorren los números entre num1 y num2 (excluyendo los dos) y se le va sumando 1:
# for i in range(num1 + 1, num2):
#     suma = suma + i
# # Se muestra por pantalla la suma de los numeros comprendidos entre num1 y num2:
# print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)


# ACTIVIDAD 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

# Se inicializa la variable "suma" en 0:
# suma = 0
# # Se crea el ciclo While con una condicion que siempre se cumpla para asegurar que se ejecute siempre la instruccion siguiente. En dicha instruccion se le pide al usuario que ingrese un numero y se guarda dentro de la variable "num". Si el número es distinto de 0, se suma al acumulador suma, que comienza en 0 y se va actualizando en cada vuelta.
# while True:
#     num = int(input("Ingrese un número entero (0 para terminar): "))
#     if num == 0:
#         break # El ciclo se va a frenar/romper si el usuario ingresa el "0" como numero.
#     suma = suma + num
# # Se muestra por pantalla la suma acumulada al romperse el ciclo:
# print("La suma total acumulada es:", suma)


# ACTIVIDAD 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

# import random # Importa el módulo 'random' para generar números aleatorios
# numero_secreto = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9 y lo guarda en "numero_secreto"
# intentos = 0 # Inicializa el contador de intentos en 0
# print("Adivina el número secreto entre 0 y 9") # Muestra por pantalla un mensaje para el usuario
# while True:  # Empieza un bucle infinito; se repetirá hasta que usemos 'break'
#     num = int(input("Ingresa tu número: ")) # Pide al usuario un número, lo convierte a entero y lo guarda en 'num'
#     intentos += 1 # Aumenta el contador de intentos en 1 cada vez que el usuario prueba
#     if num == numero_secreto: # Comprueba si el número ingresado es igual al secreto
#         print("¡Correcto! El número era", numero_secreto) # Si acierta, informa el número secreto
#         print("Lo lograste en", intentos, "intentos")  # Informa cuántos intentos hizo el usuario
#         break  # Rompe el bucle una vez que adivina.
#     else: # Si no acierta se muestra por pantalla un mensaje que diga que es incorrecto que intente nuevamente.
#         print("Incorrecto, intenta de nuevo.")


# ACTIVIDAD 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

# Se inicializa la variable "num" en 0.
# Se utiliza un ciclo for donde le indica al programa que:
# 100 sea el valor inicial. Comienza desde el 100.
# -1  sea el valor final. Se frena antes de llegar a -1 (es decir, incluye el 0).
# -2  indica que cada iteración se resta 2 para que solo sean numeros pares.
# Por utilo se muestra la secuencia de numeros pares en pantalla.
# num = 0 
# for num in range (100, -1, -2): 
#     print (num)


# ACTIVIDAD 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

# num = int (input ("Ingresa un numero positivo: ")) # Se solicita al usuario que ingrese un número entero positivo
# sumatoria = 0 # Se inicializa la variable "sumatoria" en 0, que almacenará la suma total.
# if num < 0: # Se valida si el número ingresado es negativo y en el caso de serlo le imprime un mensaje en pantalla para que vuelva a ingresar otro numero que, esta vez, sea positivo.
#     print ("Ingresaste un numero negativo. Por favor ingresa un numero positivo")
# else: # En el caso de que el numero ingresado no sea negativo ya sabemos que es positivo por lo tanto creamos el ciclo for.
#     for cont in range (0, num): # En el ciclo for hacemos correr el ciclo desde el numero 0 hasta el numero ingresado por el usuario, es decir, no lo va a contar.
#         sumatoria = sumatoria + cont # En cada iteración se va acumulando el valor de "cont" en la variable "sumatoria"
#     print ("La suma de todos los numeros comprendidos entre 0 y el numero ingresado es igual a ", sumatoria) # Al finalizar el ciclo, se muestra el resultado final de la suma


# ACTIVIDAD 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

# Se inicializan los contadores en 0:
# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# # Se define la cantidad de números a ingresar (se puede cambiar para probar más rápido):
# cantidad = 100
# # Se crea el bucle que pide al usuario ingresar la cantidad de números especificada:
# for i in range(cantidad):
#     num = int(input("Ingrese un número: "))
# # Se cuentan los pares e impares:
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# # Se cuentan los positivos y negativos (el 0 no se cuenta como ninguno):
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
# # Se muestran los resultados finales:
# print("Cantidad de números pares:", pares)
# print("Cantidad de números impares:", impares)
# print("Cantidad de números positivos:", positivos)
# print("Cantidad de números negativos:", negativos)


# ACTIVIDAD 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

# Se define la cantidad de números a ingresar:
# cantidad = 100
# # Se inicializa la variable "suma" en "0" que va a ser la que acumule la suma:
# suma = 0
# # Se crea un bucle que se repite "cantidad" de veces:
# for i in range(cantidad):
#     # Se le pide al usuario que ingrese un número entero:
#     num = int(input("Ingrese un número: "))
#     # Se suma el número ingresado al acumulador "suma":
#     suma = suma + num 
# # Se calcula la media dividiendo la suma total entre la cantidad de números:
# media = suma / cantidad
# # Se muestra el resultado en pantalla:
# print("La media de los números ingresados es igual a:", media)


# ACTIVIDAD 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Se pide al usuario que ingrese un número entero positivo:
# num = int(input("Ingresa un número positivo: "))
# # Se inicializa la variable "invertido" en "0", que guardará el número al revés:
# invertido = 0
# # Se guarda el número original en otra variable para no perderlo:
# num_original = num
# # Se usa un bucle while que se ejecuta mientras "num" sea mayor que 0:
# while num > 0:
#     # Se obtiene el último dígito del número usando el módulo 10:
#     digito = num % 10
#     # Se agrega ese dígito al número invertido, desplazando los dígitos anteriores:
#     invertido = invertido * 10 + digito
#     # Se elimina el último dígito del número original usando división entera:
#     num = num // 10
# # Se muestra el resultado final al usuario
# print("El número", num_original, "invertido es:", invertido)

