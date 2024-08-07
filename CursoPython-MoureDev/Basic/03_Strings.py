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



## Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + 'Days' + 'Of' + 'Python')

## Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' + 'For' + 'All')

## Declare a variable named company and assign it to an initial value "Coding For All".
company = "coding for all"

## Print the variable company using print().
print(company)

## Print the length of the company string using len() method and print().
print(len(company))

## Change all the characters to uppercase letters using upper() method.
print(company.upper())

## Change all the characters to lowercase letters using lower() method.
print(company.lower())


## Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())




## Cut(slice) out the first word of Coding For All string.
print(company[0:6])


## Check if Coding For All string contains a word Coding using the method index, find or other methods.
if(company.find("coding") != -1):
    print("Si contiene la palabra coding")

## Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("coding", "Peace"))

## Change Python for Everyone to Python for All using the replace method or other methods.


## Split the string 'Coding For All' using space as the separator (split()) .
## "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
## What is the character at index 0 in the string Coding For All.
## What is the last index of the string Coding For All.
## What character is at index 10 in "Cod" 8 ** 6 = 262144ng For All.
## Use index to determine the position of the first occurrence of F in Coding For All.
## Use rfind to determine the position of the last occurrence of l in Coding For All People.
## Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
## Does ''Coding For All' start with a substring Coding?
## Does 'Coding For All' end with a substring coding?
## '   Coding For All      '  , remove the left and right trailing spaces in the given string.
## Which one of the following variables return True when we use the method isidentifier():
## 30DaysOfPython
## thirty_days_of_python
## The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
## Use the new line escape sequence to separate the following sentences.
## I am enjoying this challenge.
## I just wonder what is next.
## Use a tab escape sequence to write the following lines.
## Name      Age     Country   City
## Asabeneh  250     Finland   Helsinki
## Use the string formatting method to display the following:
## radius = 10
## area = 3.14 * radius ** 2
## The area of a circle with radius 10 is 314 meters square.
## Make the following using string formatting methods:
## 8 + 6 = 14
## 8 - 6 = 2
## 8 * 6 = 48
## 8 / 6 = 1.33
## 8 % 6 = 2
## 8 // 6 = 1
## 8 ** 6 = 262144