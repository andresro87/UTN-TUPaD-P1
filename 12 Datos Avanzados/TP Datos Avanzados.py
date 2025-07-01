#1) Dado el diccionario precios_frutas 
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#1450} 
#Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 

precios_frutas ['Banana']= 1330
precios_frutas ['Manzana']= 1700
precios_frutas ['Melón'] = 2800

print(precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios. 

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


#4) Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 

contactos = {}
for palabra in range(5):
    nombre = input("Ingresa el nombre del contacto: ")
    numero = input("Ingresa el número telefonico del contacto: ")
    contactos[nombre] = numero

consultar_nombre = input("Ingrese el nombre para consultar el número de telefono: ")
if consultar_nombre in contactos:
    print(f"El número de {consultar_nombre} es: {contactos[consultar_nombre]}")
else:
    print(f"No se encontró un contacto con el nombre {consultar_nombre}")


#5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

frase = frase.lower()

palabras = frase.split()

palabras_unicas = set(palabras)

print("Palabras únicas:")
print(palabras_unicas)

frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras[palabra] + 1
    else:
        frecuencia_palabras[palabra] = 1

print("Frecuencia de cada palabra:")

for palabra in frecuencia_palabras:
    print(f"{palabra} :{frecuencia_palabras[palabra]}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 

notas_alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = int(input("Ingrese la primera nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercera nota: "))
    notas_alumnos[nombre] = (nota1, nota2, nota3)

for alumno in notas_alumnos:
    notas = notas_alumnos[alumno]
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(f"El promedio de {alumno} es: {promedio}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora. 

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores.