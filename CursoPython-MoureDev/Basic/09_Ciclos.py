### Loops ###

### While ###

variable = 0

while variable < 10:
    print(variable)
    variable += 1
else:
    print("El valor es mayor a 10")

variable = 0
while variable < 10:
    print(variable)
    variable += 1
    if variable == 5:
        break

print("####### Iterar una lista")
my_list = [25, 23, 54, 12, 20, 21, 43]

for item in my_list:
    print(item)

print("####### Iterar una tupla")
my_tuple = ("Sergio", "Ruiz", 26, 1.26, "Sergio")
for item in my_tuple:
    print(item)

print("####### Iterar una set")
my_other_set = {"Sergio", "Ruiz", 1.81, 26}
for item in my_other_set:
    print(item)


print("####### Iterar un diccionario")
my_other_dict = {
    "Nombre": "Sergio",
    "Apellido": "Ruiz",
    "Edad": 26,
    "Lenguajes": ["Python", "Java", "Go"],
    "Lista": [0, 1, 2, 2],
}

for item in my_other_dict.values():
    print(item)