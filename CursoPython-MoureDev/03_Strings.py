my_string = "Este es un string"
my_second_string = 'Este es el segundo string'

print(len(my_string))
print(len(my_second_string))

print(my_string + " " + my_second_string)

print("Este es un string \n con salto de linea")

print("\tEste es un string con tabulacion")


#Format Strings
name, lastname, age = "Sergio", "Ruiz", 26
print("Mi nombre es {} {} y tengo {} años".format(name, lastname, age))
print("Mi nombre es %s %s y tengo %d años" %(name, lastname, age))
print(f"Mi nombre es {name} {lastname} y tengo {age} años")

#Unpacking Character
name = "Sergio"
a, b, c, d, e, f = name ##Extraemos los caracteres para asignar a una variable
print(f"{a}{b}{c}{d}{e}{f}")

#Slicing String
languaje = "Python"
print(languaje)
strin_slice = languaje[1:3]
print(strin_slice)
strin_slice = languaje[-2]
print(strin_slice)
strin_slice = languaje[::-1]
print(strin_slice)
strin_slice = languaje[0:4:2]
print(strin_slice)

#functions
name_brother = "santiago"
print(name_brother.capitalize())
print(name_brother.count("a"))
print(name_brother.endswith("a"))
print(name_brother.endswith("o"))
print(name_brother.startswith("s"))
print(name_brother.find("a"))
print(name_brother.isnumeric())
print(name_brother.lower())
print(name_brother.upper())
print(name_brother.upper().isupper())