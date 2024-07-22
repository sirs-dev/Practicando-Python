### Aritmetics Operators ###
print(3 + 4)    # Addition
print(3 - 4)    # Subtraction
print(2 * 2)    # Multiplication
print(2 / 2)    # Division
print(10 % 4)   # Modulus
print(10 // 4)  # Floor division
print(3 ** 4)   # Exponentiation

print("Hola " + "Sergio")
print("Hola " * 5)

### Assignment Operators
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 > 4)
print(3 == 4)
print(3 != 4)


### Assignment Operators
print("Hola" and "Sergio")
print("Hola" or "Sergio")
print("Hola" not in "Sergio")

## Declare your age as integer variable
age = 26

## Declare your height as a float variable
height = 1.78

## Declare a variable that store a complex number
number_complex = (4 + 8j)

## Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
##     Enter base: 20
##     Enter height: 10
##     The area of the triangle is 100
base = float(input("Ingresa la base: \n"))
height = float(input("Ingresa la altura: \n"))
area = 0.5 * base * height
print(f"El area del triangulo es {area}")

## Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
##     Enter side a: 5
##     Enter side b: 4
##     Enter side c: 3
##     The perimeter of the triangle is 12
a = float(input("Ingresa lado a : \n"))
b = float(input("Ingresa lado b : \n"))
c = float(input("Ingresa la c : \n"))
perimeter = a + b + c
print(f"El perimeto del triangulo es {perimeter}")

## Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Ingresa Ingresa el lardo del rectangulo : \n"))
width = float(input("Ingresa Ingresa el ancho del rectangulo : \n"))

area = length * width
perimeter = 2 * (length + width)
print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimeter}")


## Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input("Ingresa el radio del circulo")
area = 3.14 * radius * radius
circunference = 2 * 3,14 * radius

print(f"El area del circulo es {area} y la circunferencia es {circunference}")

## Calculate the slope, x-intercept and y-intercept of y = 2x -2
pendiente = 2
interseccion_y = -2
interseccion_x = -interseccion_y / pendiente

print(f"Pendiente (m): {pendiente}")
print(f"Intersección con el eje x: {interseccion_x}")
print(f"Intersección con el eje y: {interseccion_y}")





## Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
## Compare the slopes in tasks 8 and 9.
## Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
## Find the length of 'python' and 'dragon' and make a falsy comparison statement.
## Use and operator to check if 'on' is found in both 'python' and 'dragon'
## I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
## There is no 'on' in both dragon and python
## Find the length of the text python and convert the value to float and convert it to string
## Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
## Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
## Check if type of '10' is equal to type of 10
## Check if int('9.8') is equal to 10
## Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
## Enter hours: 40
## Enter rate per hour: 28
## Your weekly earning is 1120
## Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
## Enter number of years you have lived: 100
## You have lived for 3153600000 seconds.
## Write a Python script that displays the following table
##     1 1 1 1 1
##     2 1 2 4 8
##     3 1 3 9 27
##     4 1 4 16 64
##     5 1 5 25 125