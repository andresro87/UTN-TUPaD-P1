#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 

def factorial(numero):
    if numero == 0: 
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número: "))
for i in range(1,numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1: 
        return 1
    else:
        return fibonacci(posicion -1) + fibonacci(posicion -2)
    
posicion = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

for i in range(posicion + 1):
    print(f"En la posicion {i} el valor de la serie de Fibonacci es {fibonacci(i)}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def calcular_potencia(base,potencia):
    if potencia == 0:
        return 1
    elif potencia > 0:
        return base * calcular_potencia(base,potencia - 1)
    else:
        return 1 / calcular_potencia(base, - potencia) #en caso de que el exponente sea negativo

base = int(input("Ingrese un número como base: "))
potencia= int(input("Ingrese un número como potencia: "))
resultado = calcular_potencia(base,potencia)
print(f"{base} elevado a {potencia} es {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 

def conversor_binario(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return conversor_binario(decimal//2) + str(decimal%2)
    
decimal = int(input("Ingrese el número que desea convertir a binario: "))    
print(f"El número {decimal} en binario es {conversor_binario(decimal)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 
#Requisitos: 
#La solución debe ser recursiva. 
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]: #la primera y la ultima letra son distintas
        return False
    else:
        return es_palindromo(palabra[1:-1]) #el 1 represnta la segunda letra y el -1 la penultima

palabra = input("Ingrese la palabra que desea analizar: ")
resultado = es_palindromo(palabra)
if resultado == True:
    print("La palabra ingresada es un palíndromo")
else: 
    print("La palabra ingresada no es un palíndromo")

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 
#Restricciones: 
#No se puede convertir el número a string. 
#Usá operaciones matemáticas (%, //) y recursión. 
#Ejemplos: 
#suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
#suma_digitos(9)      → 9 
#suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(numero):
    if numero <= 0:
        return print("Ingrese un número entero positivo")
    elif numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero // 10)

numero = int(input("Ingrese el número del que desea obtener la suma de sus difgitos: "))

print(f"La suma de los digitos de {numero} es {suma_digitos(numero)}")

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide. 
#Ejemplos: 
#contar_bloques(1)   → 1         (1) 
#contar_bloques(2)   → 3         (2 + 1) 
#contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

def contar_bloques(numero):
    if numero == 1:
        return 1
    else:
        return numero + contar_bloques(numero-1)

bloques= int(input("Ingrese el número de bloques base: "))
print(f"El número de bloques que se necesitan para la piramide con base {bloques} es {contar_bloques(bloques)}")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número. 
#Ejemplos: 
#contar_digito(12233421, 2)   → 3   
#contar_digito(5555, 5)       → 4
#contar_digito(123456, 7)     → 0   

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        ultimo_digito = numero % 10  
        resto_del_numero = numero // 10  

        if ultimo_digito == digito:
            return 1 + contar_digito(resto_del_numero, digito)
        else:
            return contar_digito(resto_del_numero, digito)

numero = int(input("Ingrese un número que sera analizado: "))
digito = int(input("Ingrese el digito que desea ver cuantas veces se repite: "))
resultado = contar_digito(numero,digito)

print(f"El digito {digito} se repite {resultado} veces dentro del número {numero}")

#