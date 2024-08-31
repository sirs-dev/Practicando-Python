### Challengues ###

# 1.
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


print("mani"[::-1])

def fizzbuzz():
    for item in range(1, 101):
        if item % 3 == 0 and item % 5 == 0:
            print("fizzbuzz")
        elif item % 3 == 0:
            print("fizz")
        elif item % 5 == 0:
            print("Buzz")
        else:
            print(item)




# 2.
# Escribe una funcion que reciba dos palabras (String) y retorne
# verdadero o falso (Bool) segun sean o no anagramas.
# - Un Anagrama consiste en formar una palabra reordenando TODAS
# las letras de otra palabra inicial.
# - NO hace falta comprobar que ambas palabras existan.
# - Dos palabras exactamente iguales no son anagrama.

def anagrama(firstword, secondword):
    if firstword.lower() == secondword.lower():
     return False
    return sorted(firstword.lower()) == sorted(secondword.lower())

    


# 3.
# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
# la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13 ...


def fibonacci():
    num1 = 0
    num2 = 1
    count = 0
    while count < 50:
        print(num1)
        num1, num2 = num2, num1 + num2
        count += 1




# 4.
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.


def is_prime():
    num = 0
    while(num <= 100):
        if num < 2:
            return False
        elif num == 2:
            return True

# 5 
# Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje
# que lo haga de forma automatica con logica desarrollada.
# Si le pasamos "Hola mundo" nos deberia devolver "odnum aloH"


def word_reversed(word):
    reversed_word = ""
    for index in range(len(word)-1, -1, -1):
        reversed_word += word[index]
    print(reversed_word)



word_reversed("Hola mundo")


