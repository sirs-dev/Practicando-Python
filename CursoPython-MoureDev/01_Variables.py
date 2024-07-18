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

print(name, surname, alias, age)

# Solicita valores por consola
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print(nombre)
print(edad)

# Cambiamos su tipo de dato
nombre = 23
edad = "Prueba"
print(nombre)
print(edad)


###Exercises: Level 1###

##Declare a last name variable and assign a value to it
last_name = "Ruiz"

##Declare a full name variable and assign a value to it
full_name = "Sergio ivan ruiz santamaria"

##Declare a first name variable and assign a value to it
first_variable = "First variable"

##Declare a country variable and assign a value to it
country = "Colombia"

##Declare a city variable and assign a value to it
city = "Bogota"

##Declare an age variable and assign a value to it
age = 26

##Declare a year variable and assign a value to it
year = "2024"

##Declare a variable is_married and assign a value to it
is_married = "No"

##Declare a variable is_true and assign a value to it
is_true = True


##Declare a variable is_light_on and assign a value to it
is_light_on = False

##Declare multiple variable on one line

first_variable, second_variable, third_variable = "Primero", "Segundo", "Tercero"


###Exercises: Level 2###

# Check the data type of all your variables using type() built-in function
print(
    type(last_name),
    type(full_name),
    type(first_variable),
    type(country),
    type(city),
    type(age),
    type(year),
    type(is_married),
    type(is_true),
    type(is_light_on),
)

# Using the len() built-in function, find the length of your first name )
print(len(first_variable))

# Compare the length of your first name and your last name
print(len(first_variable) and len(full_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print(diff)

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

# Calculate num_one to the power of num_two and assign the value to a variable exp


# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
