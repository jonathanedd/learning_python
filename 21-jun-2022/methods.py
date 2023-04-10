#METODOS

#CAPITALIZE : convierte el primer caracter a mayúscula
title = "esto es un curso de python"
new_title = title.capitalize()
print(title)
print(new_title)

# CASEFOLD : Cualquier caracter de Mayúscula a minúscula (Mas agresivo)
texto = "Hola Esto Es Un Texto"
new_texto = texto.casefold()
print(texto)
print(new_texto)

#LOWER : Convierte todos los caracter en minúscula (Menos agresivo)
texto_lower = "Hola Esto Es Otro Texto"
new_texto_lower = texto_lower.lower()
print(new_texto_lower)

#UPPER : Converte todos los caracteres en Mayúscula
texto_upper = "Hola, Esto Es Texto Upper"
new_texto_upper = texto_upper.upper()
print(texto_upper)
print(new_texto_upper)

#TITLE: Cambia el primer caracter a Mayúscula dentro de un string
titulo = "Esto es un nuevo titulo"
new_titulo = titulo.title()
print(titulo)
print(new_titulo)

#COUNT : Encuentra o cuenta el numero de caracteres o palabras dentro del string
count = titulo.count("e")
print(count)

#FIND : Encuentra la posición de una palabra la primera vez
texto_find = "Welcome to my crib"
new_find = texto_find.find("crib")
print(new_find)

#ENDWITH: Si termina con ...  Devuelve un true: 
texto_end = "Hola, esto termina en?"
new_texto_end = texto_end.endswith("?")
print(new_texto_end)