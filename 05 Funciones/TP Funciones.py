# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre1 = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre1)
print(saludo)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.
import math 
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2 
    return area


def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio 
    return perimetro

radio = (float(input("Ingrese el radio del círculo: ")))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del circulo es {area} y el perimetro es {perimetro}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

segundos = int(input("Ingrese la cantidad de segundos que desea convertir en horas: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas} horas.")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{i} * {numero} = {resultado}")

tabla = int(input("Ingrese el número del que desea ver la tabla: ")) 
tabla_multiplicar(tabla)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara

def operaciones_basicas(a, b):
    if b == 0:
        return "Ingrese un número distinto de 0"
    else:
        suma = a + b
        resta = a - b
        multiplicacion= a * b
        division = a // b 
    return (suma,resta,multiplicacion,division)
    

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

tupla = (operaciones_basicas(a,b))
print(f"Suma: {tupla[0]}")
print(f"Resta: {tupla[1]}")
print(f"Multiplicación: {tupla[2]}")
print(f"División entera: {tupla[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    indice_masa_corporal= peso / (altura**2)
    return indice_masa_corporal

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso,altura)
print(f"El indice de masa corporal es {imc:.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

temperatura = float(input("Ingrese la temperatura en grados celsius: "))
farenheit = celsius_a_fahrenheit(temperatura)

print(f"La temperatura en grados Farenheit es {farenheit:.2f}")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a,b,c)
print (f"El promedio entre los tres números ingresados es {promedio:.2f}")