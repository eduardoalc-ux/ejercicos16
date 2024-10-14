# variante 1
# 1: suma de dos numeros 
a=10
b=20
suma = a + b 
print (f" la suma de {a} y {b} es: {suma}" )
#----------------------------------------------------
#2: concatenacion de cadenas 
cadena1= "hola"
cadena2= "mundo" 
resultado = cadena1 + " " + cadena2
print (resultado)
#----------------------------------------------------
#3:calcular el area de un rectangulo 
base = 5
altura = 10
area = base * altura 
print (f"  el area del rectangulo es : {area}  ")
#--------------------------------------------------------
#4:  comprobar si un numero es par o impar 
num = 7
if num % 2 = 0:
resultado = "par"
else:
resultado = "impar"
print (f"el numero {num} es  {resultado}: ")
#---------------------------------------------------------
#5: calcular factorial de un numero 
num = 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
resultado = factorial(num)
print(resultado)

#--------------------------------------------------------------
#6: encontar el numero mas grannde de una lista 
numeros= [1,2,3,4,5]
numero_grande = max (numeros)
print ("el numero mas grande es:", numero_grande)
#--------------------------------------------------------------
#7: Convertir grados Celsius a Fahrenheit
celsius = 25
fahrenheit = celsius * (9/5) + 32
print (f"{celsius} grados celsius son {fahrenheit} grados fahrenheit. ")
#---------------------------------------------------------------
#8: verificar si un numero es primo 
num = 7
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
resultado = es_primo(num)
print(resultado)

#-------------------------------------------------------------------
#9: cuantas veces aparece un caracter en una cadena 
cadena "programación"
caracter "o"
cantidad =
cadena.count(caracter)
print (f"el caracter {caracter} aparece {cantidad} veces en la {cadena}:")
#-----------------------------------------------------------------------------
#10
lista = [1, 2, 3, 4, 5]
resultado = sum(lista)
print(resultado)  
#---------------------------------------------------------------------------------
#11

inicio = 1
fin = 10
numeros_pares = [numero for numero in range(inicio, fin + 1) if numero % 2 == 0]
print(numeros_pares) 
#------------------------------------------------------------------------------------
#12
# Valores a utilizar
lista = [1, 2, 3, 4, 5]
promedio = sum(lista) / len(lista)
print(promedio)  
#-----------------------------------------------------------------------------------
#13r
cadena = "Python"
cadena_invertida = cadena[::-1]
print(cadena_invertida) 
#----------------------------------------------------------------------------------
#14
lista = [10, 20, 30, 40, 50]
numero_mas_pequeno = min(lista)
print(numero_mas_pequeno) 
#--------------------------------------------------------------------------------------------
#15
palabra = "radar"
es_palindromo = palabra == palabra[::-1]
print(es_palindromo)  
#---------------------------------------------------------------------------
#16
oracion = "Hola mundo"
numero_de_palabras = len(oracion.split())
print(numero_de_palabras)  
#-----------------------------------------------------------------------------
#17
base = 2
exponente = 3
resultado = base ** exponente
print(resultado)  # Resultado esperado: 8
#----------------------------------------------------------------------------------
#18
kilometros = 5
millas = kilometros * 0.621371
print(millas)
#---------------------------------------------------------------------
#19
lista = [1, 2, 3, 4, 5]
lista_cuadrados = [numero ** 2 for numero in lista]
print(lista_cuadrados)
#-------------------------------------------------------------------
#20
lista = [5, 3, 1, 4, 2]
lista_ordenada = sorted(lista)
print(lista_ordenada)
#-------------------------------------------------------------------
#21
lista = [1, 2, 3, 4, 5]
contador = len(lista)
print(contador)
#-------------------------------------------------------------------------
#22
numero = 1234
suma_digitos = sum(int(digito) for digito in str(numero))
print(suma_digitos)
#---------------------------------
#23
cadena = "python"
cadena_mayusculas = cadena.upper()
print(cadena_mayusculas)
#-------------------------------------------------------
#24
lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista))
lista_sin_duplicados.sort()
print(lista_sin_duplicados)
#-------------------------------------------------------
#25
cadena = "hola mundo"
vocales = "aeiouáéíóú"
contador_vocales = sum(1 for letra in cadena.lower() if letra in vocales)
print(contador_vocales)
#-------------------------------------------------------
#26
n = 5
fibonacci = [0, 1]
while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci[:n])
#-------------------------------------------------------
#27
cadena = " hola mundo "
cadena_sin_espacios = cadena.replace(" ", "")
print(cadena_sin_espacios)
#-------------------------------------------------------
#28
inicio = 1
fin = 10
cantidad_impares = sum(1 for numero in range(inicio, fin + 1) if numero % 2 != 0)
print(cantidad_impares)
#-------------------------------------------------------
#29
diccionario = {"a": 1, "b": 2, "c": 3}
diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}
print(diccionario_invertido)
#-------------------------------------------------------
#30
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print(longitud)
#-------------------------------------------------------
#31
diccionario = {1: "a", 2: "b", 3: "c"}
suma_claves = sum(diccionario.keys()
print(suma_claves)

#-------------------------------------------------------
#32
lista = ["python", "java", "c++"]
lista_mayusculas = [cadena.upper() for cadena in lista]
print(lista_mayusculas)








       



