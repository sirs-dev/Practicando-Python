"""
Este módulo muestra ejemplos básicos de variables y su impresión.
"""

my_string_variable = "This is a string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable)

print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "sergio", "mini", "shecho", 26

print(name, surname, alias, age )

#Solicita valores por consola
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print(nombre)
print(edad)

#Cambiamos su tipo de dato
nombre = 23
edad = "Prueba"
print(nombre)
print(edad)