#STRING: Es una cadena de caracteres, se pueden usar comillas simples y dobles. Asi como triples 
print(""" Hola mundo """)
print(''' Hello world ''')
print(" Hola mundo ")
print(' Hello world ')

#Se pueden imprimir numeros
print(50)
print(1000)
print(3.1416)

#Imprimir numeros y letras al mismo tiempo
print(50,1000,"Hello world")
print("Hello",  end=" ") #El end=" " junta el string "Hello" con el print de abajo: "World" = "Hello World"
print("World")

#Salto de linea con back slash se saca alt + 92 \n
print("Salto \n")
print("De linea")

#Comentarios de varias lineas, con triple comillas, Al no estar asociado a una variable, lo toma como comentario y no un string
"""
print(50)
print(1000)
print(3.1416)
"""
#DOCSTRINGS: Se usa para documentar que hace una función y normalmente se usa con triple comilla """ Coment """
# TODO: Comentario para cosas que se necesitan hacer
