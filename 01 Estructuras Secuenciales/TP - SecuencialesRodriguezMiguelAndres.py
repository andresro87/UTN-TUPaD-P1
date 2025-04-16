#ejercicio1
print("Hola mundo!!")

#ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!!")

#ejercicio 3
nombre =  input("Ingrese su nombre: ")
apellido =  input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar =  input("Ingrese su lugar de residencia: ")
print(f"Hola mi nombre es {nombre} {apellido}, tengo {edad} y vivo en {lugar}")

#ejercicio 4
import math
radio = float(input("Ingrese el radio de un círculo: ")) ##se puede hacer asi o convertir el string a float en la siguente linea
area = math.pi* radio**2
perimetro = 2*math.pi*radio
print(f"El area del círculo es {area:.2f} y su perímetro es {perimetro:.2f}")

#ejercicio 5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Los segundos ingresados equivalen a {horas:.2f} horas")

#ejercicio 6 // se puede hacer de manera secuencial pero es más largo el procedimiento
numero = int(input("Ingrese el número del cual quiere obtener su tabla "))
for i in range(1,11):
 resultado = numero * i 
 print (f"{numero} * {i} = {resultado} " )

#Ejercicio 7
num1 = int(input("Ingrese un número distinto de 0: "))
num2 = int(input("Ingrese un segundo número distinto de 0: "))
if num1 == 0 or num2 == 0:
    print("Error: Ingrese un número distinto de 0 ")
else:
 suma = num1 + num2
 resta = num1 - num2
 div = num1/ num2
 multi = num1 * num2
print(f"El resultado de la suma entre los mismos es {suma}")
print(f"El resultado de la resta entre los mismos es {resta}")
print(f"El resultado del producto entre los mismos es {multi}")
print(f"El resultado de la división entre los mismos es {div:.2f}")

#Ejercicio 8  
peso = int(input("Ingrese su peso en KG: "))
altura= int(input("Ingrese su altura en centimetros: "))
altura = altura/100
imc = peso / altura**2
print(f"Su Indice de Masa Corporal o IMC es {imc:.2f}")

#ejercicio 9
celcius = int(input("Ingrese la temperatura en Celcius: "))
farenheid = float(9/5 * celcius + 32)
print (f"La temperatura en grados Farenheid es {farenheid:.2f}")

#Ejercicio 10
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print (f"El promedio de los números ingresados es: {promedio} ")