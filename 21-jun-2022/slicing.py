# SLICING
#ITERAR SSTRINGS : Cuando algo es iterable tiene indices
# a = hola : 0 1 2 3 ndices - Al revés seria -1 -2 -3 -4 
# a[0:3] = Obtendriamos hol , el último caracter no lo va a tomar / string[start:end]

# desde el índice 0 hasta el índice 3 (no incluido)
# lo que significa que se incluyen los caracteres en las posiciones 0, 1, 2 y 3
my_string = "This is my string!"
print(my_string[0:4]) 
print(my_string[1:7])
print(my_string[8:len(my_string)]) #imprime desde la posicion 8 hasta el final o resto del string: my string!

#Obtener la última posición de algún iterable (string)
iterable = "Hey there, I am coding in Pyhton"
print(iterable[-1])
print(iterable[:3]) # Desde el comienzo hasta la posicion 3 (No incluido)
print(iterable[26:len(iterable)]) #Imprime la ultima palabra del string
print(iterable[26:]) # Desde la posicion 26 P hasta el final: Python
print(iterable[::2]) #Imprime el Indice 0 y los caracteres de 2 en 2 : 2 4 6 8 10 etc



#CONCATENAR
#Forma de concatenar 1
name = "Carla"
last_name = "Jimenez"
full_name = name + " " + last_name 
print(full_name)

#Forma de concatenar 2 : la f al comienzo del string significa format
full_name = f"My full name is {name} {last_name}"
print(full_name)

#Forma de concatenar 3: Posición 0 = name y posición 1 = last_name, como se define en las llaves
full_name_2 = "My full name is {0} {1}".format(name, last_name)
full_name_3 = "My full name is {nombre} {apellido}".format(nombre=name, apellido=last_name)
print(full_name_2)
print(full_name_3)

#Forma de concatenar 4 : STRING TEMPLATES
from string import Template

t = Template("My name is $nombre")
nombre = t.substitute({
    "nombre": "Jhonatan"
})
print(nombre)
