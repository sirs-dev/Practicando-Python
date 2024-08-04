### Class ###


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def walk(self):
        print(f"{self.name} {self.lastname} esta caminando")


my_person = Person("Sergio", "Ruiz")
print(f"Mi nombre es {my_person.name} y mi apellido es {my_person.lastname}")

my_person.walk()
