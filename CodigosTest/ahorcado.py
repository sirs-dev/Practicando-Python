# Description: Juego del ahorcado

#Se importan librerias
import random


# Se crea una lista de palabras de animales
palabras = [
    "perro", "gato", "leon", "tigre", "elefante", "jirafa", "cebra", "mono", "oso", "pato",
    "aguila", "gallina", "ganso", "pavo", "pajaro", "loro", "paloma", "colibri", "cuervo",
    "buitre", "halcon", "aguila", "pez", "tiburon", "ballena", "delfin", "pulpo", "calamar",
    "cangrejo", "langosta", "camaron", "caracol", "babosa", "cucaracha", "araña", "escorpion",
    "alacran", "abeja", "avispa", "mosca", "mosquito", "mariposa", "polilla", "libelula",
    "grillo", "saltamontes"
]


palabraAdivinar = random.choice(palabras) # Se elige una palabra aleatoria de la lista
palabraAdivinar = palabraAdivinar.upper() # Se convierte la palabra a mayusculas

# Se crea una lista con los caracteres de la palabra a adivinar
palabraGuiones = []
for i in range(len(palabraAdivinar)):
    palabraGuiones.append("_")

print("Vamos a jugar al ahorcado, adivina la palabra!!")
letra = input("Ingresa una letra\n")

letra = letra.upper() # Se convierte la letra a mayusculas


for index, letraPalabra in enumerate(palabraAdivinar):
    if letra == letraPalabra:
        palabraGuiones[index] = letra

print(" ".join(palabraGuiones))