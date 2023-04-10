# Data Type: Es un item o elemento que define el tipo y el rango de valores que pueden tomar:
# Numbers - strings - booleans
# Variables: Un nombre que tiene un valor asignado

#VARIABLES
income = 480
Income = 470
income = 470 # Imprime este valor porque a income se le asigno un nuevo valor. 
print(income, Income)

# No se pueden definir variables que empiecen con numeros.
# En python no hay constante, Todo es Variable, Las constantes como tal no existen
# Per no significa que no podamos trabajar con constantes:

# la variable es mayuscula es una convención para definir una Constanre
EDAD = 20
print(EDAD)
EDAD = 25
print(EDAD) # Sin embargo imprime el nuevo valor asignado en EDAD = 25 

# Lo veremos mas Adelante.
from enum import Enum
class color(Enum):
    RED = 1
    green = 2
print(color.RED.value)

# NUMEROS ENTEROS
numero = 8444
numero_a = -52146
print(type(numero)) # Imprime clase int que significa entero
print(type(numero_a)) # Tipo o clase entero

numero_c = 789.25
print(type(numero_c)) # Clase float 

# NUMEROS COMPLEJOS - COMPLEX
numero_d = complex(10,20) # 10 + 20j 
print(numero_d)
print(type(numero_d)) # Clase complex

#BOOLEANS: Tipos de datos que nos permiten elejir entre dos opciones, si es verdadero o falso
# En python los booleanos empiezan con la primera letra en Mayusculo : True / False, Esto porque las clases empiezan con mayúscula.
print(True)
print(False)

name = "Jhonatan"
print(type(name)) # Y asi para las las diferentes comillas '' , "", """ """  
quote = """
this is a great
quote
"""
print(type(quote))

random_string = "I am batman" 
print(len(random_string)) # len() es la función que imprime todos los caracteres incluyendo los espacios.

batman = "Bruce Wayne"
first = batman[0] #indexing
print(first)  #Imprime la B de la variable batman.

incognit = batman[5]
print(incognit) #Imprime el caracter espacio

print(batman[len(batman) - 1]) #mprime el último caracter debido a que len(batman) - 1 representa el ultimo caracter del string
print(batman[-1]) #Forma mas sencilla de hacer

#STRINGS
#Los strings son inmutables, No se pueden mutar. Excepto que a la variable se le asigne otro valor 
last_name = "Ordonez"
print(last_name)

last_name = "Mesa"
print(last_name)

#Pero No se pueden mutar los valores strings dentro de las variables
string = "Inmutability"
# string[0] = "O"  TypeError: 'str' object does not support item assignment
print(string)

