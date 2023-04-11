#EJERCICIO: 1 Crea un string del primer caracter, del caracter del medio y el caracter final
string1 = "James"
new_string1 = string1[0] + string1[2] + string1[-1]
print(new_string1)

#EJERCICIO 2 : crea un caracter hecho de los tres caracteres del medio
str1 = "JhonDipPeta"
new_str1 = str1[4:-4]
print(new_str1)

#EJERCICIO 3 : Dados dos string, s1 y s2. Escribe un programa para crear un nuevo string s3 agregando s2 en el medio de s1
s1 = "Ault"
s2 = "Kelly"

s3 = (s1[0:2]) + (s2[0:]) + (s1[2:])
print(s3)

resultName = f"{s1[0:2]}{s2[0:]}{s1[2:]}"
print(resultName)


#EJERCICIO 4: Crea un nuevo string hecho del primer caracter de cada string existente, el del medio y del final
s1 = "America"
s2 = "Japan"

new = s1[0:1] + s2[0:1] + s1[-4] + s2[2:len(s2)]
print(new)

#EJERCICIO 5 : Convertir todo el texto a capitalize
text = """IT was a special pleasure to see things eaten, to see things blackened and changed. 
With the brass nozzle in his fists, with this great python spitting its venomous kerosene upon the world, 
the blood pounded in his head, and his hands were the hands of some amazing conductor playing all the 
symphonies of blazing and burning to bring down the tatters and charcoal ruins of history.-"""
faren = "FAHRENHEIT 451"

new_text = text.capitalize()
new_faren = faren.capitalize()

final_text = f"{new_text} {new_faren}"
print(final_text)