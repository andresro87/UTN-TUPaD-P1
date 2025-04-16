#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0,101): #definimos a la variable iteradora como numero y el rango de 0 hasta 101 para incluir el 100
    print(numero)           

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

numero_entero = int(input("Ingrese un número entero ")) #pedimos el número al usuario
numero_entero = abs(numero_entero) # se usa esta funcion para cambiar el número a positivo en caso que se ingrese un negativo
contador = 0 #inicializamos la variable contador
if numero_entero == 0: # esta condición sirve en caso de que el usuario ingrese 0
    contador = 1
    print(f"La cantidad de digitos es {contador}")
while numero_entero != 0: #  comenzamos el bucle
    numero_entero = numero_entero // 10 
    contador += 1
print(f"La cantidad de digitos es {contador}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.
print("Ingrese dos números enteros de menor a mayor")
numero1 = int(input("Ingrese el primer número entero ")) #pedimos al usuario que ingrese las dos primeras variables 
numero2 = int(input("Ingrese el segundo número entero "))
sumatoria = 0   #en esta variable se guardará el resultado de la suma entre los números ingresados
iterador = 0    #variable iteradora
for iterador in range(numero1 + 1,numero2):
    sumatoria = sumatoria + iterador  #tambien se puede hacer sumatoria += iterador
print(f"La suma de los números comprendidos entre {numero1} y {numero2} es {sumatoria}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

numeroEntero = int(input("Ingrese un número o 0 para finalizar "))
suma = 0
while numeroEntero != 0 :
    suma = suma + numeroEntero
    numeroEntero = int(input("Ingrese otro número o 0 para finalizar "))
print(f"La suma de los numeros ingresados es {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random #importamos la función random para el número aleatorio
num = int(input("Ingrese el número que intenta adivinar ")) #el usuario ingresa el número por pantalla
intentos = 1
numero_aleatorio = random.randint(1, 9) #randint se utiliza para numeros aleatorios enteros
while num != numero_aleatorio :
    intentos = intentos + 1 
    num = int(input("No adivino el número, ingrese otro número "))
print (f"Usted adivinó el número, la cantidad de intestos fue {intentos}")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 

for numeros in range (100, 0, -2):
    print(f"{numeros}")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

numero_positivo = int(input("Ingrese un número "))
numero_positivo = abs(numero_positivo) #utilizamos esta funcion en caso de que se ingrese un número negativo
suma = 0 
iterador = 0
for iterador in range(0,numero_positivo +1 ):
    suma = suma + iterador 
print(f"La suma de todos los números entre 0 y el número que usted ingreso es {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

pares = 0
impares = 0
negativos = 0
positivos = 0 
iterador = 0 
cantidad_a_procesar = 10 
for iterador in range (0,cantidad_a_procesar):
    numero = int(input("Ingrese un número "))
    if numero % 2 == 0 : 
        pares += 1
    else:
        impares += 1
    if numero > 0 :
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Cantidad de números pares {pares}")
print(f"Cantidad de números impares {impares}")
print(f"Cantidad de números negativos {negativos}")
print(f"Cantidad de números positivos {positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).

cantidad_a_procesar = 10
iterador = 0
acumulador = 0
for iterador in range(cantidad_a_procesar):
    numero = int(input("Ingrese un número "))
    acumulador = acumulador + numero
media = acumulador / cantidad_a_procesar
print(f"La media de los números ingresados es {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero = int(input("Ingrese el número del cual quiere invertir su orden "))
numero = abs(numero) #en caso de que el numero ingresado sea negativo
numero_invertido = 0
ultimo_digito = 0
while numero != 0 : 
    ultimo_digito = numero % 10 #utilizamos la función módulo para dividir y tomar el último digito
    numero_invertido = numero_invertido *10 + ultimo_digito #almacenamos en la variable los números tomados anteriormente
    numero = numero // 10 #dividimos por 10 al número original para quitarle el último dígito
print(f"El número invertido es {numero_invertido}")
