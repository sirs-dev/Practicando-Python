### Dictionaries ###

my_dictionary = dict()
my_other_dict = {}

my_other_dict = {
    "Nombre": "Sergio",
    "Apellido": "Ruiz",
    "Edad": 26,
    "Lenguajes": ["Python", "Java", "Go"],
    "Lista": [0, 1, 2, 2],
}

my_other_dict["Nombre"] = "Ivan"
print(my_other_dict)
print(my_other_dict["Lista"])

print(my_other_dict["Lenguajes"][0])

print(my_other_dict.get("Lenguajes"))
print(my_other_dict.keys())
print(my_other_dict.values())
print(my_other_dict.items())
print(list(my_other_dict.values()))

