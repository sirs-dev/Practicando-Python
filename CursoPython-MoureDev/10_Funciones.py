### Functions ###


def my_function():
    print("Esto es una funcion")


my_function()


def sum_two_values(num1: int, num2: int) -> int:
    print(f"La suma de {num1} + {num2} es igual a {num1+num2}")


sum_two_values(int("4"), int("5"))


def sum_values(num1: int, num2: int):
    return num1 + num2


total = sum_values(2, 6)
print(total)


def print_name_lastname(name, lastname):
    print(f"{name} {lastname}")


print_name_lastname(lastname="Ruiz", name="Sergio")


def print_name_default(name, lastname, alias = "Sin alias"):
    print(f"{name} {lastname} {alias}")


print_name_default(lastname="Ruiz", name="Sergio")

def print_texts(*text):
    print(text)

print_texts("Hola", "Sergio", "Ruiz")